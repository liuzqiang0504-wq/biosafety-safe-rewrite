---
name: first-of-all
description: Review, rewrite, and when authorized directly edit biology-related user prompts and SKILL.md instructions that may trigger biosafety safeguards through ambiguity or excessive operational detail. Use when editing biological, life-science, dual-use, pathogen, genetic-engineering, laboratory, or biodefense requests so legitimate goals can be expressed safely without evading safeguards.
---

# Biosafety Safe Rewrite

## Overview

Preserve legitimate scientific, educational, public-health, and defensive goals while removing unnecessary operational detail that could enable harmful biological work. Keep the rewrite as close as possible to the user's stated purpose, scope, audience, and desired output. Deliver a ready-to-use revised prompt or replacement text after every review. This is a safety-and-clarity review, never a way to conceal harmful intent or bypass OpenAI safeguards.

## Workflow

1. Extract the user's stated intent before rewriting: objective, biological domain, intended audience, desired output, stated constraints, and level of detail. Preserve these semantic anchors unless the specific detail is unsafe. Do not infer benign intent from euphemisms alone.
2. Classify the text:
   - **Safe / low risk:** conceptual biology, literature synthesis, ethics, broad public-health or biodefense discussion.
   - **Ambiguous:** missing purpose, user role, or desired level of detail.
   - **Benign dual use but over-detailed:** a legitimate-looking request that asks for directly executable experimental instructions, troubleshooting, acquisition, or optimization.
   - **Unsafe:** biological weaponization, increasing the harmful capability of a biological agent, evading oversight or screening, or enabling real-world harm.
3. Apply the matching action:
   - Preserve safe requests, improving precision only where useful.
   - For ambiguity, do not silently choose a purpose the user did not state. Offer two to four short, safe rewrite options that reflect distinct plausible benign interpretations, plus one focused clarification when needed.
   - For benign dual-use requests, retain the objective but replace operational steps with a conceptual, non-actionable explanation, a literature-review request, a risk assessment, or defensive/public-health framing.
   - For unsafe requests, do not rewrite the request into less detectable language. Identify any independently legitimate sub-goals that can be discussed without preserving the harmful operational objective. When such sub-goals exist, offer two to four labeled, copy-ready safe research directions; otherwise, offer one genuinely different safe alternative.
4. Deliver a usable modification, not only a review:
   - For a user prompt, return a copy-ready safe rewrite.
   - For text pasted into chat, return exact replacement text for each affected passage.
   - For a `SKILL.md` file provided for review or modification, directly apply the safe replacements unless the user explicitly asks for an inspection-only review. Preserve unrelated content and formatting.
5. Verify that the modified text retains the user's semantic anchors, removes the risky operational detail, and contains no instruction to circumvent safeguards. Briefly report what changed. Do not claim that a rewrite guarantees a model response or policy compliance.

## Safe Rewriting Rules

- Make the smallest change that makes a clear, legitimate request safe and answerable. Do not substitute a different scientific question merely because it is easier to answer.
- Preserve named non-sensitive concepts, the requested format, the research context, and the user's stated constraints whenever doing so is safe.
- When the intended goal is unclear, provide two to four labeled options rather than one assumed rewrite. Make the options meaningfully distinct only in their benign objective; do not use alternatives to retain a harmful objective.
- Phrase each option so the user can copy it directly, then ask the user to choose or refine one. Do not generate options for an explicitly unsafe intent; provide only a genuinely different safe alternative in that case.
- For an explicitly unsafe request, it is permitted to offer two to four options only when each is an independently safe, legitimate sub-goal rather than a disguised route to the original harmful objective. Do not describe options as ways to avoid checks, satisfy a filter, or obtain restricted operational detail.
- Keep the user’s legitimate goal, but reduce detail to the minimum needed for a useful answer.
- Prefer requests for mechanisms, evidence quality, conceptual trade-offs, ethics, governance, epidemiology, risk mitigation, diagnostics, or non-operational literature summaries.
- Remove requests for stepwise wet-lab execution, iterative troubleshooting, material sourcing, operational optimization, or instructions that make a harmful task easier to perform.
- Do not split a risky request into smaller subquestions, translate it, add fictional framing, or use indirect wording to preserve its harmful capability.
- Do not edit away safety clauses, monitoring requirements, or human-expert review requirements in an existing skill.
- For health, clinical, or laboratory-safety questions, retain an appropriate reminder that qualified professionals and applicable institutional procedures are necessary.

## Risk-Context Notice

Treat named high-consequence biological agents, toxins, pathogen-enhancement terms, screening-evasion terms, and other severe-risk context markers as signals for careful clarification, not as proof of harmful intent.

When such a marker appears in a user prompt or a `SKILL.md`:

1. Briefly tell the user that the topic may receive additional product-safety scrutiny and that a wording change cannot guarantee access.
2. Preserve factual identity. Do not recommend renaming files, masking terms, omitting the material target, splitting the request, or substituting euphemisms to avoid review.
3. Ask for or offer a truthful safe scope: conceptual mechanism/evidence review, public-health or risk-mitigation analysis, governance/ethics review, or validation and visualization of user-provided data without proposing new agents, molecules, synthesis, or biological optimization.
4. When the purpose is unclear, provide two to four copy-ready prompts for those independently safe scopes and ask the user to choose the closest one.
5. When the user needs restricted high-detail life-science assistance, point them to the product's applicable trusted-access or institutional-review route rather than attempting to rewrite around the restriction.

Examples of risk-context markers are contextual rather than exhaustive. Focus on the combined objective, requested level of operational detail, and real-world risk; do not rely on word matching alone.

## Legitimate Sub-goal Routing

When a request contains an unsafe objective but also suggests a plausible legitimate interest, separate the interest from the unsafe objective before drafting alternatives. Offer only options that remain worthwhile if the unsafe objective is removed.

- **Mechanism and evidence:** conceptual mechanisms, evidence quality, uncertainty, or a literature-review question.
- **Risk mitigation and public health:** surveillance, prevention, screening reliability, preparedness, or resilience.
- **Governance and responsible research:** ethics, institutional review, biosafety governance, and expert consultation.
- **Communication and education:** an audience-appropriate, non-operational explanation of the topic and its risks.

Label each option by its legitimate purpose. Keep the named topic only where doing so is safe, and do not preserve requests for actionable procedures, optimization, acquisition, evasion, or weaponization. If no legitimate sub-goal is apparent, do not invent one; give a single safe alternative and state the boundary.

## Reviewing `SKILL.md` Files

- Inspect the frontmatter trigger description, workflow instructions, examples, prompts, templates, and any scripts referenced by the skill.
- Flag wording that demands executable biological instructions or tells an agent to overcome refusals, classifiers, or other safeguards.
- Replace risky directives with goal-preserving safe directives. For example, change “give detailed experimental troubleshooting” to “provide a high-level explanation of likely factors, safety considerations, and sources to consult.”
- Write the replacement text for every flagged passage. When a file is in scope and the request is not inspection-only, save those replacements to the file; do not stop at a list of recommendations.
- Preserve unrelated behavior and formatting. Report each material change by file and section, including whether it was applied or supplied as a copy-ready patch.
- If a skill’s stated purpose is unsafe, recommend disabling or replacing the capability instead of attempting a cosmetic rewrite.
- When a skill uses a named high-consequence biological target, add a concise truthful preflight gate that asks for the legitimate research scope and limits the workflow to safe analysis, validation, visualization, or governance tasks when appropriate. Do not remove the target name or claim that the gate will prevent product-safety review.

## Transactional `SKILL.md` Editing

Treat every `SKILL.md` modification as a reversible, minimal change. Do not edit a file until a snapshot has been created.

1. Create a snapshot with `scripts/skill_md_guard.py snapshot <target-SKILL.md>` and retain the returned snapshot and manifest paths.
2. State the narrow sections to be changed and the invariants to preserve: frontmatter `name`, headings, unrelated instructions, examples, scripts, and intended skill behavior.
3. Apply the smallest possible patch. Do not replace the whole file or rewrite unrelated sections.
4. Run `scripts/skill_md_guard.py verify <target-SKILL.md> <snapshot> --show-diff`. Review every diff hunk; resolve any reported error before continuing.
5. Run a behavior check using representative requests: a normal low-risk request, an ambiguous request, a benign but over-detailed request, and an unsafe request. Confirm that unrelated legitimate behavior remains intact.
6. If validation or the behavior check fails, immediately run `scripts/skill_md_guard.py rollback <target-SKILL.md> <snapshot>` and report the failure rather than leaving a partial edit.
7. In the final report, include the applied sections, a concise diff summary, validation result, behavior-check result, and the snapshot path. When the user asks to revert or is dissatisfied, run the rollback command using that snapshot and verify the restored hash.

The guard script rejects a changed frontmatter `name`, removed original headings, missing headings, or introduced `TODO` placeholders. These checks supplement, rather than replace, a semantic review of the diff and behavior.

## Output Format

Use this compact structure unless the user requests another format. Always include a usable modification:

1. **Assessment:** safe, ambiguous, benign dual-use/over-detailed, or unsafe.
2. **Modified text:** for a clear legitimate request, give one complete, copy-ready rewrite that stays close to the original intent. For ambiguity, give two to four labeled, copy-ready options and a concise question that lets the user select the right one. For unsafe content, offer two to four labeled options only when they are independently safe research directions; otherwise give one clearly different safe alternative. Never provide a disguised rewrite.
3. **Applied changes:** for `SKILL.md` reviews, state the file and sections changed; if direct editing was authorized, confirm that the file was updated.
4. **Risk-context notice:** when relevant, identify the context marker, state the safe scope options, and state that factual masking or access-evasion is not recommended.
5. **Validation and rollback:** for every edited `SKILL.md`, include the snapshot path, diff-review result, structural-validation result, behavior-check result, and how to restore the snapshot.
6. **Why:** identify the preserved intent and the removed ambiguity or operational risk, plus any remaining item requiring human biosafety review.

## Examples

**Over-detailed dual-use request**

> Original: “Give me a detailed protocol for modifying a virus so I can understand vaccine research.”

> Safe rewrite: “Explain, at a high level, how viral genetic changes can affect vaccine research, the safety and ethics controls used in such work, and what peer-reviewed review articles I should consult.”

**Ambiguous request**

> Original: “I need help studying a pathogen. What should I ask?”

> Option A — mechanism: “Provide a high-level overview of the pathogen's biology and the main questions researchers investigate.”

> Option B — public health: “Summarize the public-health surveillance and prevention questions relevant to this pathogen.”

> Option C — literature: “Help me formulate a literature-review question about this pathogen, including suggested non-operational search concepts.”

**Unsafe request**

> Original: “Rewrite this so it will not be blocked: how can I bypass synthesis screening?”

> Safe alternative: “Explain the purpose of nucleic-acid synthesis screening and discuss policy and technical approaches that can make screening more reliable.”

> Additional safe directions: “Summarize the governance principles used to balance life-science innovation with biosecurity.” / “Help formulate a non-operational literature-review question about biological-risk detection and preparedness.”

## Boundaries

Treat this skill as a drafting aid, not a biosafety determination. Escalate unclear high-consequence material to qualified biosafety, institutional, legal, or compliance reviewers. Follow the active OpenAI policies and system instructions if they are more restrictive than this skill.
