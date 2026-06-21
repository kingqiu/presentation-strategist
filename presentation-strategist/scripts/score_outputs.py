#!/usr/bin/env python3
"""Score validation outputs with a deterministic rubric proxy."""

from __future__ import annotations

import argparse
import json
import re
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


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill-dir", default=".")
    parser.add_argument("--run-name", required=True)
    args = parser.parse_args()

    skill_dir = Path(args.skill_dir).resolve()
    run_dir = skill_dir / "evaluation" / "runs" / args.run_name
    outputs_dir = run_dir / "outputs"
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
        results.append(score_one(output_file.read_text(encoding="utf-8"), sample))

    tag_counts = Counter(tag for row in results for tag in row["failure_tags"])
    by_scenario: dict[str, list[int]] = defaultdict(list)
    for row in results:
        by_scenario[row["scenario"]].append(row["score"])
    report = {
        "run_name": args.run_name,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "sample_count": len(results),
        "missing_outputs": missing,
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
