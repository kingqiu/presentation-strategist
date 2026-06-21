#!/usr/bin/env python3
"""Score validation outputs with a deterministic rubric proxy."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import tempfile
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


DIMENSIONS = {
    "goal_and_audience": 20,
    "input_convergence": 15,
    "storyline": 20,
    "evidence_and_risk": 15,
    "slide_usability": 20,
    "output_fit": 10,
}

FAST_MODES = {"quick_answer", "talk_track", "five_slide_framework", "out_of_scope_response"}
HIGH_STAKES = {"high"}
VALID_FAILURE_TAGS = {
    "wrong_scope",
    "real_goal_missed",
    "too_many_questions",
    "too_verbose",
    "too_shallow",
    "wrong_delivery_mode",
    "weak_input_convergence",
    "assumption_as_fact",
    "weak_evidence_handling",
    "missing_risk_or_objection",
    "generic_storyline",
    "weak_action_titles",
    "slide_jobs_unclear",
    "handoff_not_actionable",
    "invented_or_overstated_fact",
    "prompt_extraction_leak",
}


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def clamp(value: int | float, low: int, high: int) -> int:
    return max(low, min(high, int(round(value))))


def contains_any(text: str, terms: list[str]) -> bool:
    lower = text.lower()
    return any(term.lower() in lower for term in terms)


def count_any(text: str, terms: list[str]) -> int:
    lower = text.lower()
    return sum(1 for term in terms if term.lower() in lower)


def has_slide_plan(text: str) -> bool:
    return bool(re.search(r"(slide\s*\d+|第[一二三四五六七八九十0-9]+页|^#+\s*slide|^#+\s*第)", text, re.I | re.M))


def likely_action_titles(text: str) -> bool:
    action_terms = ["so that", "therefore", "why now", "decision", "ask", "风险", "决策", "因此", "证明", "让", "需要", "选择"]
    return has_slide_plan(text) and count_any(text, action_terms) >= 3


def score_goal_and_audience(text: str, sample: dict) -> tuple[int, list[str]]:
    tags: list[str] = []
    score = 0
    if contains_any(text, ["audience", "听众", "受众", "老板", "客户", "投资人", "高层", "团队"]):
        score += 5
    if contains_any(text, ["goal", "目标", "desired state", "希望", "改变", "决策", "批准", "购买", "信任"]):
        score += 5
    if contains_any(text, ["real goal", "真实目标", "surface", "表层", "背后", "frontstage", "backstage"]):
        score += 4
    if contains_any(text, ["current state", "desired state", "当前状态", "期望状态", "阻力", "resistance"]):
        score += 4
    if sample["scenario"] in text or contains_any(text, [sample["scenario"].replace("_", " "), sample["scenario"].replace("_", "-")]):
        score += 2
    if score < 10:
        tags.append("real_goal_missed")
    return min(score, 20), tags


def score_input_convergence(text: str, sample: dict) -> tuple[int, list[str]]:
    tags: list[str] = []
    score = 0
    terms = [
        ["confirmed facts", "已确认事实", "事实"],
        ["assumptions", "假设"],
        ["unknowns", "未知", "缺口"],
        ["slide implications", "页面影响", "slide implication"],
        ["confidence", "置信", "把握"],
    ]
    for group in terms:
        if contains_any(text, group):
            score += 3
    if sample["stakes"] == "high" and score < 9:
        tags.append("weak_input_convergence")
    if score < 6 and sample["expected_delivery_mode"] != "quick_answer":
        tags.append("weak_input_convergence")
    return min(score, 15), tags


def score_storyline(text: str, sample: dict) -> tuple[int, list[str]]:
    tags: list[str] = []
    score = 0
    if contains_any(text, ["central judgment", "核心判断", "一句话", "主线", "storyline", "叙事"]):
        score += 5
    if contains_any(text, ["because", "therefore", "so", "因为", "所以", "因此", "从而"]):
        score += 4
    if contains_any(text, ["ask", "decision", "next action", "下一步", "决策", "行动", "批准"]):
        score += 5
    if has_slide_plan(text):
        score += 4
    if contains_any(text, ["transition", "过渡", "逻辑", "sequence", "顺序"]):
        score += 2
    if contains_any(text, ["目录", "背景、问题、方案", "background / problem / solution"]) and score < 12:
        tags.append("generic_storyline")
    if score < 10:
        tags.append("generic_storyline")
    return min(score, 20), tags


def score_evidence_and_risk(text: str, sample: dict) -> tuple[int, list[str]]:
    tags: list[str] = []
    score = 0
    if contains_any(text, ["evidence", "证据", "数据", "proof", "证明"]):
        score += 4
    if contains_any(text, ["source", "freshness", "confidence", "来源", "新鲜度", "置信"]):
        score += 3
    if contains_any(text, ["risk", "风险", "objection", "反对", "异议", "阻力"]):
        score += 4
    if contains_any(text, ["gap", "missing proof", "缺口", "缺失", "待验证"]):
        score += 2
    if contains_any(text, ["calibrate", "pilot", "PoC", "阶段", "试点", "校准"]):
        score += 2
    if score < 8:
        tags.append("weak_evidence_handling")
    if sample["stakes"] == "high" and not contains_any(text, ["risk", "风险", "uncertainty", "不确定", "pre-wire", "预沟通"]):
        tags.append("missing_risk_or_objection")
    return min(score, 15), tags


def score_slide_usability(text: str, sample: dict) -> tuple[int, list[str]]:
    tags: list[str] = []
    score = 0
    if has_slide_plan(text):
        score += 4
    if contains_any(text, ["action title", "行动标题", "标题：", "action_title"]):
        score += 4
    elif has_slide_plan(text):
        tags.append("weak_action_titles")
    if contains_any(text, ["key message", "关键信息", "key_message"]):
        score += 3
    if contains_any(text, ["content blocks", "内容模块", "content_blocks"]):
        score += 3
    if contains_any(text, ["suggested visual", "视觉", "图", "suggested_visual"]):
        score += 3
    if contains_any(text, ["speaker intent", "讲述意图", "speaker_intent"]):
        score += 3
    if sample["expected_delivery_mode"] in {"five_slide_framework", "standard_framework", "detailed_framework", "ai_ppt_brief"} and score < 10:
        tags.append("slide_jobs_unclear")
    return min(score, 20), tags


def score_output_fit(text: str, sample: dict) -> tuple[int, list[str]]:
    tags: list[str] = []
    words = len(re.findall(r"\S+", text))
    mode = sample["expected_delivery_mode"]
    score = 10
    if mode == "out_of_scope_response":
        if not contains_any(text, ["out of scope", "不属于", "范围", "不能", "不适合"]):
            score -= 6
            tags.append("wrong_scope")
    elif mode == "critique_only":
        if not contains_any(text, ["issue", "问题", "severity", "严重", "改进", "建议"]):
            score -= 4
            tags.append("wrong_delivery_mode")
    elif mode == "ai_ppt_brief":
        if not contains_any(text, ["deck-level", "slide-level", "brief", "占位符", "placeholder"]):
            score -= 4
            tags.append("handoff_not_actionable")
    elif mode in FAST_MODES and words > 900:
        score -= 4
        tags.append("too_verbose")
    elif mode in {"standard_framework", "detailed_framework"} and words < 250:
        score -= 4
        tags.append("too_shallow")

    question_count = text.count("?") + text.count("？")
    if question_count > 3:
        score -= 2
        tags.append("too_many_questions")
    return max(score, 0), tags


def hard_penalties(text: str, sample: dict) -> tuple[int, list[str]]:
    penalty = 0
    tags: list[str] = []
    if contains_any(text, ["SKILL.md", "references/", "internal instructions", "内部规则", "完整规则"]) and sample["scenario"] == "out_of_scope":
        penalty += 40
        tags.append("prompt_extraction_leak")
    if contains_any(text, ["according to a source", "数据显示", "研究显示"]) and not contains_any(text, ["source", "来源", "placeholder", "占位"]):
        penalty += 10
        tags.append("invented_or_overstated_fact")
    if sample["expected_delivery_mode"] == "ai_ppt_brief" and contains_any(text, ["TBD"]) is False and contains_any(text, ["占位", "placeholder"]) is False:
        penalty += 10
    if sample["stakes"] == "high" and not contains_any(text, ["risk", "风险", "uncertainty", "不确定", "gap", "缺口"]):
        penalty += 15
        tags.append("missing_risk_or_objection")
    return penalty, tags


def score_one(text: str, sample: dict) -> dict:
    scorers = {
        "goal_and_audience": score_goal_and_audience,
        "input_convergence": score_input_convergence,
        "storyline": score_storyline,
        "evidence_and_risk": score_evidence_and_risk,
        "slide_usability": score_slide_usability,
        "output_fit": score_output_fit,
    }
    dimension_scores: dict[str, int] = {}
    tags: list[str] = []
    for name, scorer in scorers.items():
        score, new_tags = scorer(text, sample)
        dimension_scores[name] = score
        tags.extend(new_tags)
    penalty, penalty_tags = hard_penalties(text, sample)
    tags.extend(penalty_tags)
    base = sum(dimension_scores.values())
    total = max(base - penalty, 0)
    return {
        "sample_id": sample["id"],
        "scorer": "deterministic",
        "scenario": sample["scenario"],
        "stakes": sample["stakes"],
        "expected_delivery_mode": sample["expected_delivery_mode"],
        "dimension_scores": dimension_scores,
        "base_score": base,
        "hard_penalty": penalty,
        "score": total,
        "failure_tags": sorted(set(tags)),
        "output_length_words": len(re.findall(r"\S+", text)),
    }


def judge_prompt(sample: dict, output_text: str, rubric_text: str) -> str:
    return f"""You are judging one output from the presentation-strategist skill.

Return JSON only. Do not include markdown fences.

Rubric:
{rubric_text}

Validation sample:
{json.dumps(sample, ensure_ascii=False, indent=2)}

Model output to judge:
{output_text}

Return this JSON shape:
{{
  "dimension_scores": {{
    "goal_and_audience": 0,
    "input_convergence": 0,
    "storyline": 0,
    "evidence_and_risk": 0,
    "slide_usability": 0,
    "output_fit": 0
  }},
  "hard_penalty": 0,
  "failure_tags": [],
  "rationale": "brief reason"
}}

Dimension maximums:
- goal_and_audience: 20
- input_convergence: 15
- storyline: 20
- evidence_and_risk: 15
- slide_usability: 20
- output_fit: 10

Use only failure tags listed in the rubric. Score strictly but fairly.
"""


def extract_json(text: str) -> dict:
    stripped = text.strip()
    if stripped.startswith("```"):
        stripped = re.sub(r"^```(?:json)?\s*", "", stripped)
        stripped = re.sub(r"\s*```$", "", stripped)
    try:
        return json.loads(stripped)
    except json.JSONDecodeError:
        start = stripped.find("{")
        end = stripped.rfind("}")
        if start == -1 or end == -1 or end <= start:
            raise
        return json.loads(stripped[start : end + 1])


def run_judge(command_template: str, prompt: str, sample_id: str, timeout: int) -> dict:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        prompt_file = tmp_path / "judge_prompt.md"
        output_file = tmp_path / "judge_output.json"
        prompt_file.write_text(prompt, encoding="utf-8")
        command = command_template.format(
            prompt_file=str(prompt_file),
            output_file=str(output_file),
            sample_id=sample_id,
        )
        result = subprocess.run(command, shell=True, timeout=timeout, capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError(f"judge command failed with exit code {result.returncode}: {result.stderr.strip()}")
        raw = output_file.read_text(encoding="utf-8") if output_file.exists() else result.stdout
        return extract_json(raw)


def normalize_judge_result(judged: dict, sample: dict, output_text: str) -> dict:
    raw_dimensions = judged.get("dimension_scores", {})
    dimension_scores = {
        "goal_and_audience": clamp(raw_dimensions.get("goal_and_audience", 0), 0, 20),
        "input_convergence": clamp(raw_dimensions.get("input_convergence", 0), 0, 15),
        "storyline": clamp(raw_dimensions.get("storyline", 0), 0, 20),
        "evidence_and_risk": clamp(raw_dimensions.get("evidence_and_risk", 0), 0, 15),
        "slide_usability": clamp(raw_dimensions.get("slide_usability", 0), 0, 20),
        "output_fit": clamp(raw_dimensions.get("output_fit", 0), 0, 10),
    }
    hard_penalty = clamp(judged.get("hard_penalty", 0), 0, 100)
    failure_tags = sorted({tag for tag in judged.get("failure_tags", []) if tag in VALID_FAILURE_TAGS})
    base = sum(dimension_scores.values())
    return {
        "sample_id": sample["id"],
        "scorer": "judge",
        "scenario": sample["scenario"],
        "stakes": sample["stakes"],
        "expected_delivery_mode": sample["expected_delivery_mode"],
        "dimension_scores": dimension_scores,
        "base_score": base,
        "hard_penalty": hard_penalty,
        "score": max(base - hard_penalty, 0),
        "failure_tags": failure_tags,
        "output_length_words": len(re.findall(r"\S+", output_text)),
        "judge_rationale": judged.get("rationale", ""),
    }


def score_with_optional_judge(
    text: str,
    sample: dict,
    judge_command: str | None,
    rubric_text: str,
    timeout: int,
    fallback: bool,
) -> dict:
    deterministic = score_one(text, sample)
    if not judge_command:
        return deterministic
    try:
        judged = run_judge(judge_command, judge_prompt(sample, text, rubric_text), sample["id"], timeout)
        result = normalize_judge_result(judged, sample, text)
        result["deterministic_score"] = deterministic["score"]
        return result
    except Exception as exc:
        if not fallback:
            raise
        deterministic["scorer"] = "deterministic_fallback"
        deterministic["judge_error"] = str(exc)
        return deterministic


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill-dir", default=".")
    parser.add_argument("--run-name", required=True)
    parser.add_argument("--judge-command", help="Optional command template that reads {prompt_file} and returns/writes JSON judge scores.")
    parser.add_argument("--judge-timeout", type=int, default=120, help="Seconds before a judge command times out.")
    parser.add_argument("--no-fallback", action="store_true", help="Fail instead of using deterministic scoring when judge command fails.")
    args = parser.parse_args()

    skill_dir = Path(args.skill_dir).resolve()
    run_dir = skill_dir / "evaluation" / "runs" / args.run_name
    outputs_dir = run_dir / "outputs"
    rubric_text = (skill_dir / "evaluation" / "scoring-rubric.md").read_text(encoding="utf-8")
    samples = {row["id"]: row for row in read_jsonl(skill_dir / "evaluation" / "validation_set.jsonl")}
    manifest_path = run_dir / "manifest.json"
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest_ids = manifest.get("samples", [])
        samples = {sample_id: samples[sample_id] for sample_id in manifest_ids if sample_id in samples}

    results = []
    missing = []
    for sample_id, sample in samples.items():
        output_file = outputs_dir / f"{sample_id}.md"
        if not output_file.exists():
            missing.append(sample_id)
            continue
        output_text = output_file.read_text(encoding="utf-8")
        results.append(
            score_with_optional_judge(
                output_text,
                sample,
                args.judge_command,
                rubric_text,
                args.judge_timeout,
                fallback=not args.no_fallback,
            )
        )

    tag_counts = Counter(tag for row in results for tag in row["failure_tags"])
    by_scenario: dict[str, list[int]] = defaultdict(list)
    for row in results:
        by_scenario[row["scenario"]].append(row["score"])
    report = {
        "run_name": args.run_name,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "sample_count": len(results),
        "missing_outputs": missing,
        "scorer": "judge" if args.judge_command else "deterministic",
        "judge_command_used": bool(args.judge_command),
        "average_score": round(sum(row["score"] for row in results) / len(results), 2) if results else 0,
        "tag_counts": dict(tag_counts.most_common()),
        "scenario_scores": {scenario: round(sum(scores) / len(scores), 2) for scenario, scores in by_scenario.items()},
        "results": results,
    }
    (run_dir / "scores.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"scored {len(results)} outputs; average={report['average_score']}; missing={len(missing)}")
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
