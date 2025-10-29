# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

ClaudeHumanizer is a production-ready AI text humanization system featuring a 10-phase assembly line that transforms AI-generated content into natural, human-like writing. The system uses JSON-formatted prompts designed specifically for Claude (Anthropic) that work sequentially to eliminate AI detection markers while preserving meaning and voice.

**Key characteristics:**
- Prompt-based system (no executable code)
- JSON files contain LLM system prompts
- Designed for Claude Sonnet 4.5 (optimal results)
- Sequential processing through 10 specialized phases
- Phase 9.5 is optional statistical analysis

## File Structure

**Phase Prompt Files** (numbered 1-10, with 6.1 and 9.5 optional):
- `1_grammar_foundation.json` through `10_final_ai_word_sweep.json`
- `6.1_character_dialogue_pass.json` (optional character-specific dialogue)
- `9.5_statistical_analysis_hub.json` (optional statistical analysis)

**Master Vocabulary List:**
- `master_prohibited_words.json` - Required dependency for phases 2 and 10
- Contains AI-associated terms, phrases, and pattern rules
- Also available in Markdown: `master_prohibited_words.md`

**Documentation** (`docs/` directory):
- `USAGE_GUIDE.md` - Step-by-step processing instructions
- `TECHNICAL_REFERENCE.md` - LLM optimization & automation guides
- `CUSTOMIZATION.md` - Advanced configuration
- `CHANGELOG.md` - Version history
- `How AI Detectors Work.md` - Research basis for design decisions

**Examples** (`examples/` directory):
- `n8n_workflow_sample.json` - Ready-to-import automation workflow
- Various YAML pipeline configurations for different LLM providers

**Other Files:**
- `Forbidden Words List.md` - Human-readable prohibited terms reference
- `GEMINI.md` - Gemini-specific guidance (similar to this file)

## Core Architecture Principles

1. **Assembly Line Processing**: Exactly 10 sequential phases (1→2→3→4→5→6→7→8→9→10)
2. **Domain Specialization**: Each phase targets ONE specific text improvement domain
3. **Domain Isolation**: Phases never modify content owned by other phases
4. **Master List Integration**: Only phases 2 and 10 require `master_prohibited_words.json`

5. **Dialogue Protection**: Only Phase 6 modifies dialogue - all other phases preserve quoted speech
6. **Sequential Dependencies**: Each phase processes output from the previous phase
7. **Optional Phases**: 6.1 (character dialogue) and 9.5 (statistics) can be inserted or skipped

## Phase Domains (What Each Phase Does)

Understanding phase domains is critical when modifying prompts:

| Phase | Domain | Master List? | Special Notes |
|-------|--------|--------------|---------------|
| 1 | Grammar errors only | No | Never touches style/voice |
| 2 | AI vocabulary removal | **Yes** | Applies pattern rules (dialogue pauses, light descriptions, finger actions) |
| 3 | Purple prose + nominalization | No | De-nominalization added in v2.4.0 |
| 4 | Flat passage improvement | No | Sensory detail enhancement |
| 5 | Obvious statement conversion | No | Adds subtlety and implication |
| 6 | Dialogue content ONLY | No | Temperature 1.0 recommended |
| 6.1 | Character-specific dialogue (optional) | No | Project-specific customization |
| 7 | Weak language patterns | No | 12 categories including transitions |
| 8 | Rhythm + punctuation variation | No | Strategic imperfections (v4.0) |
| 9 | AI pattern detection (qualitative) | No | N-grams, perplexity phrases |
| 9.5 | Statistical analysis (optional) | No | Burstiness, POS, TTR metrics |
| 10 | Word filtering ONLY | **Yes** | Catches reintroduced prohibited words |

## JSON Prompt Structure

All phase files follow this structure:

```json
{
  "title": "Phase Name",
  "version": "X.X.X",
  "date": "YYYY-MM-DD",
  "description": "What this phase does",
  "persona": "LLM role description",
  "agent_directives": { ... },
  "assembly_line_position": "Phase X: ...",
  "domain_restrictions": {
    "only_fix": [...],
    "never_touch": [...],
    "respect_later_stages": "..."
  },
  "instructions": [...],
  "output_format": { ... }
}
```

**Key fields:**
- `version`: Semantic versioning (update when modifying)
- `domain_restrictions.never_touch`: Critical for domain isolation
- `assembly_line_position`: Reinforces sequential processing
- `output_format`: Always specifies Markdown output, no JSON/commentary

## Prompt Standardization

All phase prompts follow a standardized structure for consistency and maintainability:

- **`PROMPT_TEMPLATE.json`** - Master template with all sections tagged as [REQUIRED], [OPTIONAL], or [PHASE-SPECIFIC]
- **`PROMPT_STANDARDS.md`** - Human-readable documentation of standardization rules
- **`validate_prompt.py`** - Automated validation script to check conformance
- **`STANDARDIZATION_SUMMARY.md`** - Overview of the standardization system

**Quick validation:**
```bash
python validate_prompt.py <phase_file.json>  # Check single file
python validate_prompt.py --all              # Check all phases
```

## Common Development Tasks

### Modifying Phase Prompts

When editing a phase JSON file:

1. **Read the entire prompt first** to understand domain boundaries
2. **Check `never_touch` rules** - do not violate domain isolation
3. **Update version number** using semantic versioning (MAJOR.MINOR.PATCH)
4. **Update date field** to current date (YYYY-MM-DD)
5. **Maintain standard structure** - sections should follow template order
6. **Validate changes** - run `python validate_prompt.py <file>.json`
7. **Test domain isolation** - ensure phase only affects its designated domain
8. **Test sequential integration** - run through full pipeline to verify no breaking changes

### Creating New Phase Prompts

1. **Copy `PROMPT_TEMPLATE.json`** as starting point
2. **Replace all [bracketed placeholders]** with phase-specific content
3. **Remove template guidance fields** (COMMENT_, _TEMPLATE_INSTRUCTIONS, etc.)
4. **Add phase-specific sections** using standardized naming conventions
5. **Validate** - run `python validate_prompt.py new_phase.json`
6. **Test** - verify phase works correctly in isolation and in pipeline

### Adding Terms to Master Prohibited Words

The `master_prohibited_words.json` file has this structure:

```json
{
  "title": "Master Prohibited Words List",
  "version": "X.X.X",
  "prohibited_single_words": [...],
  "prohibited_multi_word_phrases": [...],
  "pattern_based_rules": {
    "dialogue_pauses": [...],
    "light_descriptions": [...],
    "finger_actions": [...]
  }
}
```

**When adding new terms:**
1. Add to appropriate category (single words vs phrases vs patterns)
2. Update version number in changelog
3. Test with phases 2 and 10 to ensure proper integration
4. Update `master_prohibited_words.md` if maintaining both formats

### Testing Changes

**No automated tests exist.** Manual testing workflow:

1. **Create sample text** with content relevant to your changes
2. **Process through affected phase(s)** using Claude Sonnet 4.5
3. **Process through full pipeline** (phases 1-10) to check integration
4. **Verify domain boundaries** - confirm phase only changed its domain
5. **Check for regressions** - ensure quality hasn't degraded

### Documentation Updates

When modifying system behavior, update these files:

- **README.md**: If user-facing workflow changes
- **docs/USAGE_GUIDE.md**: If processing steps change
- **docs/TECHNICAL_REFERENCE.md**: If LLM recommendations change
- **docs/CHANGELOG.md**: Always document version changes
- **Phase JSON files**: Update version numbers and dates

## Important Domain Isolation Rules

**Critical principle:** Each phase ONLY modifies content in its domain.

**Dialogue handling:**
- Only Phase 6 (and optional 6.1) modify dialogue
- All other phases MUST preserve quoted speech exactly
- This is the most commonly violated rule - prompts extensively warn against it

**Master list dependencies:**
- Only phases 2 and 10 load `master_prohibited_words.json`
- Other phases should not implement separate word filtering
- Phase 10 exists specifically to catch reintroduced prohibited words

**Never modify:**
- Grammar in phases other than Phase 1
- Dialogue in phases other than 6/6.1
- Statistical metrics outside Phase 9.5
- Prohibited words outside phases 2/10

## Architecture Evolution Notes

**Phase 9 refactor (v17.0.0):**
- Separated qualitative (pattern) and quantitative (statistical) analysis
- Statistical metrics moved to Phase 9.5 for consolidated single-pass analysis
- Phase 9 now focuses on N-grams and perplexity patterns only

**Phase 10 addition (v3.0.0):**
- Created to catch prohibited words reintroduced by phases 3-9
- Pure word filtering - no statistical analysis
- Final quality control checkpoint

**Optional phases:**
- 6.1: Added for project-specific character dialogue customization
- 9.5: Added to consolidate all statistical analysis in one pass