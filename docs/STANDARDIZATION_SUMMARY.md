# Prompt Standardization - Implementation Summary

## What Was Created

Three new files to establish and enforce prompt consistency:

### 1. **PROMPT_TEMPLATE.json** - Master Template
- Complete standardized structure for all phase prompts
- Every section tagged as `[REQUIRED]`, `[OPTIONAL]`, or `[PHASE-SPECIFIC]`
- Includes inline guidance and placeholders
- Comments explain when to include optional sections
- Serves as copy-paste starting point for new phases

### 2. **PROMPT_STANDARDS.md** - Standards Guide
- Human-readable documentation of standardization rules
- Explains section order and required fields
- Lists standardized wording that must be identical across phases
- Provides naming conventions for consistency
- Includes common mistakes to avoid
- Step-by-step guide for using the template

### 3. **validate_prompt.py** - Validation Script
- Python script that checks prompt conformance
- Validates structure, required sections, and standardized wording
- Can check single file or all phases at once
- Color-coded output: errors (red), warnings (yellow), info (blue)
- Exit codes for CI/CD integration

## Standard Structure Overview

Every phase prompt must follow this exact order:

```
1. HEADER BLOCK (lines 1-10)
   - title, version, date
   - assembly_line_position (MUST be line 4)
   - description

2. DOMAIN DEFINITION (lines 11-30)
   - domain_restrictions
     - only_handle
     - never_touch (must include 4 standard items)
     - respect_assembly_line

3. PERSONA & FRAMEWORK (lines 31-75)
   - persona (4 fields)
   - agent_directives (3 fields)
   - anti_hallucination_framework (3 fields)

4. SPECIAL NOTES (lines 76-90) [OPTIONAL]
   - master_prohibited_list_reference (Phases 2, 6.1, 7, 10)
   - note_on_word_filtering (Phases 5, 6, 8, 9)
   - note_on_statistical_metrics (Phases 9, 10)

5. PHASE-SPECIFIC CONTENT (lines 91+)
   - Use standardized subsection names
   - processing_instructions (not "core_instructions")
   - detection_criteria/framework
   - enhancement_techniques/strategies
   - etc.

6. OUTPUT FORMAT (final ~50 lines)
   - Standardized block (identical across all phases)
   - Only change [bracketed] placeholders

7. CRITICAL_FINAL_INSTRUCTION (last line)
   - Standardized wording
```

## Key Standardization Rules

### Must Be Identical Across All Phases

1. **never_touch list** - Must include these 4 items:
   - "Dialogue content (text in quotation marks)"
   - "Markdown formatting (headers, links, code blocks, etc.)"
   - "Character speech patterns"
   - "Work completed by previous phases"

2. **agent_directives** - Exactly 3 fields:
   - persistence
   - tool_usage
   - deliberate_planning

3. **anti_hallucination_framework** - Exactly 3 fields:
   - real_world_facts
   - fictional_world_building
   - fallback_strategy

4. **output_format** - Entire block identical except [bracketed] placeholders

5. **CRITICAL_FINAL_INSTRUCTION** - Exact wording with phase-specific [placeholder]

### Naming Conventions

**Preferred subsection names:**
- `processing_instructions` (not "core_instructions" or "processing_steps")
- `detection_criteria` or `detection_framework`
- `enhancement_techniques` or `optimization_strategies`
- `replacement_guidelines` or `conversion_strategies`
- `quality_standards` or `quality_assurance`

## How to Use

### Creating a New Phase Prompt

1. Copy `PROMPT_TEMPLATE.json`
2. Replace all `[bracketed placeholders]` with phase-specific content
3. Remove all `COMMENT_` fields
4. Remove template instruction fields
5. Remove `OPTIONAL_` fields that don't apply
6. Add phase-specific sections using naming conventions
7. Validate: `python validate_prompt.py your_new_phase.json`

### Updating an Existing Phase

1. Read current phase file
2. Compare structure against `PROMPT_TEMPLATE.json`
3. Add any missing [REQUIRED] sections
4. Fix section order if needed
5. Standardize field names
6. Update version number and date
7. Validate: `python validate_prompt.py phase_file.json`

### Validating Prompts

**Check single file:**
```bash
python validate_prompt.py 3_overwritten_language_reduction.json
```

**Check all phase files:**
```bash
python validate_prompt.py --all
```

**Output legend:**
- ✗ ERROR (red) - Critical issue, must fix
- ⚠ WARNING (yellow) - Should fix for consistency
- ℹ INFO (blue) - Suggestion or minor issue

## Current State

Running `python validate_prompt.py --all` on existing prompts shows:

**Common Issues Found:**
- Missing `date` field in some headers
- `assembly_line_position` not always at line 4
- Inconsistent `never_touch` lists (missing standard items)
- Incomplete `anti_hallucination_framework` in some phases
- Mixed use of "core_instructions" vs "processing_instructions"
- Extra non-standard fields in `agent_directives`

**These are all warnings/info** - the prompts still function, but standardizing them will improve:
- Maintainability
- Consistency
- LLM comprehension
- Version control diffs

## Benefits of Standardization

### For Development
- **Easier to create new phases** - Copy template, fill in placeholders
- **Faster updates** - Know exactly where to find each type of instruction
- **Better diffs** - Changes are easier to spot in version control
- **Reduced errors** - Less chance of omitting critical instructions

### For Maintenance
- **Quick audits** - Run validator to check all prompts at once
- **Consistent updates** - When updating output_format, change once and apply everywhere
- **Clear structure** - Anyone can understand prompt organization

### For LLMs
- **Predictable context** - Same structure helps with prompt comprehension
- **Consistent priming** - Standard order ensures critical context comes early
- **Better parsing** - Well-structured prompts are easier to process

## Next Steps

### Recommended Actions

1. **Review the template** - Familiarize yourself with `PROMPT_TEMPLATE.json`
2. **Read the standards** - Understand rules in `PROMPT_STANDARDS.md`
3. **Run validation** - Check current state: `python validate_prompt.py --all`
4. **Fix critical errors first** - Address any ERROR-level issues
5. **Standardize incrementally** - Update prompts as you modify them
6. **Use template for new phases** - Don't create from scratch

### Optional: Full Standardization Pass

If you want to bring all existing prompts into full conformance:

1. Start with phases that have fewest warnings
2. Update one phase at a time
3. Test the phase after updating
4. Validate: `python validate_prompt.py <phase>.json`
5. Commit changes per phase

**Estimated effort:** ~10-15 minutes per phase × 12 phases = 2-3 hours total

### Maintaining Standards Going Forward

1. **Use the template** for all new phases
2. **Run validator** before committing changes
3. **Update version/date** with every change
4. **Keep standards docs updated** if you evolve the structure

## Files Reference

| File | Purpose | When to Use |
|------|---------|-------------|
| `PROMPT_TEMPLATE.json` | Master template with all sections tagged | Creating new phases, updating existing ones |
| `PROMPT_STANDARDS.md` | Human-readable documentation | Understanding rules, quick reference |
| `validate_prompt.py` | Automated validation script | Before committing, periodic audits |
| This file | Implementation summary | Understanding what was created and why |

## Questions?

- **What's required vs optional?** Check tags in `PROMPT_TEMPLATE.json`
- **How should I name a section?** See "Naming Conventions" in `PROMPT_STANDARDS.md`
- **Is my prompt conformant?** Run `python validate_prompt.py <file>.json`
- **What's the exact wording for X?** Copy from `PROMPT_TEMPLATE.json`

---

**Bottom line:** These three files provide everything needed to create consistent, maintainable phase prompts. The template shows what to include, the standards document explains why, and the validator ensures compliance.
