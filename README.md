# Biosafety Safe Rewrite

**Biosafety Safe Rewrite** is a Codex skill for reviewing biology-related prompts and
`SKILL.md` files before work begins. It helps preserve legitimate research
intent while reducing avoidable ambiguity, excessive operational detail, and
unsafe framing.

## Why it exists

Life-science requests can be difficult to phrase well. A request may be
legitimate but underspecified, may combine a useful scientific goal with
unnecessary operational detail, or may mention a high-consequence biological
context that receives extra product-safety scrutiny.

This skill helps turn those cases into clearer, safer, and more useful tasks.
It is not a tool for concealing a target, changing names, or evading safeguards.

![Example of a product-safety interruption](assets/blocked-content-example.png)

## What it does

- **Preserves intent.** Keeps the stated objective, scope, audience, requested
  output, and non-sensitive context wherever safe.
- **Clarifies ambiguity.** Offers two to four copy-ready alternatives when a
  user has not made their legitimate goal clear.
- **Routes safe sub-goals.** Separates an unsafe operational objective from
  independently useful directions such as mechanism/evidence review,
  risk-mitigation analysis, governance, education, validation, or
  visualization.
- **Flags risk context truthfully.** Notes when a high-consequence biological
  context may receive additional scrutiny, without recommending file renaming,
  masking, euphemisms, or request splitting.
- **Reviews other skills.** Identifies risky instructions in an existing
  `SKILL.md` and supplies minimal, goal-preserving replacement text.
- **Edits safely.** For authorized `SKILL.md` edits, creates a snapshot,
  applies a minimal patch, validates the diff and structural invariants, and
  supports rollback.

## What it does not do

Biosafety Safe Rewrite does not guarantee that a rewritten request will be accepted by a
product. Safety decisions depend on the complete task, requested detail,
context, and applicable system rules. The skill does not help users bypass
safeguards or disguise harmful objectives.

## Installation

Place this repository in your Codex skills directory:

```text
%USERPROFILE%\.codex\skills\biosafety-safe-rewrite
```

Start a new Codex task after installing or updating the skill.

## Usage

Invoke the skill explicitly:

```text
$biosafety-safe-rewrite
```

Examples:

```text
Use $biosafety-safe-rewrite to review this biology-related prompt and provide a
copy-ready revision.

Use $biosafety-safe-rewrite to inspect this SKILL.md, apply only necessary safe edits,
and provide the validation and rollback details.
```

## Safe `SKILL.md` editing

The bundled guard script supports reversible edits:

```text
python scripts/skill_md_guard.py snapshot <target-SKILL.md>
python scripts/skill_md_guard.py verify <target-SKILL.md> <snapshot> --show-diff
python scripts/skill_md_guard.py rollback <target-SKILL.md> <snapshot>
```

The verifier checks the frontmatter name, original headings, and accidental
`TODO` additions. It complements—not replaces—a semantic review of the diff
and a behavior check.

## Repository contents

- `SKILL.md` — the main workflow and safety rules
- `agents/openai.yaml` — Codex interface metadata
- `scripts/skill_md_guard.py` — snapshot, verification, and rollback helper
- `assets/blocked-content-example.png` — example screenshot used above

## Scope and limitations

This is a drafting and review aid, not a biosafety determination. Follow
applicable laws, institutional procedures, and the active product policies.
