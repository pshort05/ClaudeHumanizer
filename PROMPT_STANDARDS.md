# ClaudeHumanizer Prompt Standardization Guide

## Overview

All phase prompts follow a standardized structure to ensure consistency, maintainability, and optimal LLM comprehension. This document explains the standards and how to apply them.

## Standard Section Order

Every phase prompt MUST follow this exact order:

```
1. HEADER BLOCK (lines 1-10)
   ├─ title
   ├─ version
   ├─ date
   ├─ assembly_line_position ← MUST be line 4
   └─ description

2. DOMAIN DEFINITION (lines 11-30)
   └─ domain_restrictions
      ├─ only_handle
      ├─ never_touch
      └─ respect_assembly_line

3. PERSONA & FRAMEWORK (lines 31-75)
   ├─ persona (4 fields: name, background, expertise, philosophy)
   ├─ agent_directives (3 fields: persistence, tool_usage, deliberate_planning)
   └─ anti_hallucination_framework (3 fields: real_world_facts, fictional_world_building, fallback_strategy)

4. SPECIAL NOTES (lines 76-90) [OPTIONAL - as applicable]
   ├─ master_prohibited_list_reference (Phases 2, 6.1, 7, 10 only)
   ├─ note_on_word_filtering (Phases 5, 6, 8, 9 only)
   ├─ note_on_statistical_metrics (Phases 9, 10 only)
   └─ why_phase_exists (Use when phase might seem redundant)

5. PHASE-SPECIFIC CONTENT (lines 91+) [VARIABLE]
   ├─ processing_instructions (preferred name)
   ├─ detection_criteria OR detection_framework
   ├─ enhancement_techniques OR optimization_strategies
   ├─ replacement_guidelines OR conversion_strategies
   ├─ quality_standards OR quality_assurance
   ├─ examples (when needed)
   └─ preservation_guidelines (when special rules needed)

6. OUTPUT FORMAT (final ~50 lines) [REQUIRED - STANDARDIZED]
   └─ output_format
      ├─ artifact_only_system
      ├─ artifact_specifications
      ├─ no_changes_handling
      ├─ protection_requirements
      └─ output_restrictions

7. FINAL INSTRUCTION (absolute last line) [REQUIRED - STANDARDIZED]
   └─ CRITICAL_FINAL_INSTRUCTION
```

## Section Tags

| Tag | Meaning | Action |
|-----|---------|--------|
| **[REQUIRED]** | Must be present in every phase | Always include, use standard wording |
| **[OPTIONAL]** | Include only when applicable | Add if phase needs it |
| **[PHASE-SPECIFIC]** | Content varies by phase | Customize for phase domain |

## Required Sections Checklist

Before finalizing any phase prompt, verify:

- ✓ **Header block** (lines 1-5): title, version, date, assembly_line_position, description
- ✓ **assembly_line_position** is on line 4 (right after date, before description)
- ✓ **domain_restrictions** includes: only_handle, never_touch, respect_assembly_line
- ✓ **persona** has 4 fields: name, background, expertise, philosophy
- ✓ **agent_directives** has 3 fields: persistence, tool_usage, deliberate_planning
- ✓ **anti_hallucination_framework** has 3 fields: real_world_facts, fictional_world_building, fallback_strategy
- ✓ **output_format** block uses standardized wording (only change [bracketed] placeholders)
- ✓ **CRITICAL_FINAL_INSTRUCTION** is absolute last line with standardized wording

## Standardized Wording

### Never Touch List (domain_restrictions.never_touch)

**Every phase MUST include these standard items:**
```json
"never_touch": [
  "Dialogue content (text in quotation marks)",
  "Markdown formatting (headers, links, code blocks, etc.)",
  "Character speech patterns",
  "Work completed by previous phases",
  "[Add phase-specific items here]"
]
```

### Agent Directives Structure

**Always use this exact 3-field structure:**
```json
"agent_directives": {
  "persistence": "Continue [action] until [completion criteria]. Only conclude when [final state].",
  "tool_usage": "If uncertain about [aspect], use your tools to [gather info]. DO NOT guess or make assumptions.",
  "deliberate_planning": "You MUST plan extensively before [action], identifying [what to look for]. DO NOT [anti-pattern]."
}
```

### Output Format Block

**This section must be IDENTICAL across all phases except for bracketed placeholders:**

- `artifact_creation`: "...with [grammar corrections/AI word replacements/rhythm variations/etc.] applied"
- `content`: "...with [prohibited words replaced/weak language improved/etc.] applied"
- `completeness_requirement`: "...with only [critical grammar errors corrected/sensory elements enhanced/etc.] made"
- `preserve_everything`: "If no [grammar errors/AI patterns/weak language/etc.] exist..."

**Do NOT change:** "no_commentary", "format", "structure", "when_no_changes_needed", "never_summarize", "dialogue_protection", "structural_protection", "output_restrictions"

### Critical Final Instruction

**Last line must follow this template exactly:**
```json
"CRITICAL_FINAL_INSTRUCTION": "Always output the complete text content in Markdown format. Never output JSON, analysis, or summaries. If no [phase-specific improvements] are needed, output the entire original text exactly as provided."
```

## Naming Conventions

### Preferred Subsection Names

Use these standardized names in phase-specific sections:

| Concept | Preferred Name | Avoid |
|---------|---------------|-------|
| Step-by-step instructions | `processing_instructions` | "core_instructions", "processing_steps" |
| How to identify issues | `detection_criteria` or `detection_framework` | "identification_rules" |
| How to improve | `enhancement_techniques` or `optimization_strategies` | "improvement_methods" |
| How to replace/convert | `replacement_guidelines` or `conversion_strategies` | "replacement_rules" |
| Quality metrics | `quality_standards` or `quality_assurance` | "quality_checks" |
| Example content | `examples` | "sample_cases" |
| Special preservation rules | `preservation_guidelines` | "protection_rules" |

## Special Notes - When to Include

### master_prohibited_list_reference
**Include in:** Phases 2, 6.1, 7, 10 (phases that use the master list)

**Standard wording:**
```json
"master_prohibited_list_reference": "Uses master_prohibited_words.json as single source of truth for all prohibited terms. Do not maintain separate word lists in this prompt."
```

### note_on_word_filtering
**Include in:** Phases 5, 6, 8, 9 (mid-pipeline phases that might be confused with filtering phases)

**Standard wording:**
```json
"note_on_word_filtering": "Phase X does NOT perform word filtering. Phases 2 and 10 handle all prohibited word removal. Phase X focuses exclusively on [this phase's domain]."
```

### note_on_statistical_metrics
**Include in:** Phases 9, 10 (phases that might be confused with Phase 9.5)

**Standard wording:**
```json
"note_on_statistical_metrics": "Phase X does NOT perform statistical analysis (burstiness, POS distribution, TTR). Phase 9.5 handles all quantitative metrics. Phase X focuses exclusively on [this phase's domain]."
```

## Common Mistakes to Avoid

| ❌ Wrong | ✓ Right | Why |
|---------|---------|-----|
| `assembly_line_position` on line 22 | Line 4 (before description) | LLM should understand role immediately |
| Different `never_touch` lists | Standard 4 items + phase-specific | Consistency across phases |
| Missing `anti_hallucination_framework` | Include in ALL phases | Critical for accuracy |
| `core_instructions` AND `processing_steps` | Pick ONE: `processing_instructions` | Avoid redundancy |
| Custom `output_format` wording | Use template exactly | Ensures consistency |
| Forgetting version/date update | Update with every change | Track revisions |

## How to Use the Template

1. **Copy** `PROMPT_TEMPLATE.json` as starting point
2. **Replace** all `[bracketed placeholders]` with phase-specific content
3. **Remove** all `COMMENT_` fields (they're guidance only)
4. **Remove** template instruction fields: `_TEMPLATE_INSTRUCTIONS`, `_SECTION_TAGS`, `_USAGE_INSTRUCTIONS`, `RECOMMENDED_SUBSECTION_NAMES`, `_STANDARDIZATION_CHECKLIST`, `_QUALITY_CHECKS`
5. **Remove** `OPTIONAL_` fields that don't apply to your phase
6. **Add** phase-specific sections following naming conventions
7. **Verify** all [REQUIRED] sections present
8. **Validate** JSON syntax

## Quality Audit Process

Run this checklist before committing any prompt changes:

**Structure Audit:**
- [ ] Header block is lines 1-5 with correct order
- [ ] `assembly_line_position` is line 4
- [ ] All [REQUIRED] sections present
- [ ] Sections in standardized order

**Content Audit:**
- [ ] `never_touch` includes 4 standard items
- [ ] `agent_directives` has exactly 3 fields
- [ ] `anti_hallucination_framework` has exactly 3 fields
- [ ] Special notes included if applicable

**Wording Audit:**
- [ ] `output_format` block matches template (except [bracketed] content)
- [ ] `CRITICAL_FINAL_INSTRUCTION` matches template exactly
- [ ] Subsection names follow conventions (no "core_instructions" or "processing_steps")

**Functionality Audit:**
- [ ] Phase-specific content is clear and actionable
- [ ] No duplicate instructions
- [ ] Examples provided for complex concepts
- [ ] Version number updated if content changed
- [ ] Date updated to today

## Version Control

When updating a phase:

1. **Increment version number:**
   - MAJOR: Breaking changes (complete restructure)
   - MINOR: New functionality added
   - PATCH: Bug fixes, clarifications, small improvements

2. **Update date** to current date

3. **Document changes** in `CHANGELOG.md` (if significant)

## File Naming

All phase files follow this pattern:
- Single-digit phases: `X_phase_name.json` (e.g., `1_grammar_foundation.json`)
- Optional phases: `X.X_phase_name.json` (e.g., `6.1_character_dialogue_pass.json`, `9.5_statistical_analysis_hub.json`)

## Questions?

If unsure about standardization:
1. Check `PROMPT_TEMPLATE.json` for guidance
2. Compare with recent well-structured phase (e.g., Phase 10)
3. When in doubt, follow the template exactly
