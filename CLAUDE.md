# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

ClaudeHumanizer is a production-ready AI text humanization system featuring an 11-phase assembly line that transforms AI-generated content into natural, human-like writing. The system uses JSON-formatted prompts designed specifically for Claude (Anthropic) that work sequentially to eliminate AI detection markers while preserving meaning and voice.

**Key characteristics:**
- Prompt-based system (no executable code)
- JSON files contain LLM system prompts
- Designed for Claude Sonnet 4.5 (optimal results)
- Sequential processing through 11 core phases (with 6.1 and 9.5 optional)
- Phase 8.5 is new structural pattern elimination (v3.2.0+)
- Phase 9.5 is optional statistical analysis
- v3.3.0: All JSON files optimized for performance (37.8 KB reduction / 23.5%)
- v3.3.0: Romance and erotica patterns moved to optional genre-specific lists

## File Structure

**Phase Prompt Files** (numbered 1-10, with 6.1 and 8.5 and 9.5 optional):
- `1_grammar_foundation.json` through `10_final_ai_word_sweep.json`
- `6.1_character_dialogue_pass.json` (optional character-specific dialogue)
- `8.5_structural_construction_elimination.json` (new in v3.2.0 - syntactic pattern removal)
- `9_final_verification.json` - AI pattern detection (qualitative analysis)
- `9.5_statistical_analysis_hub.json` (optional statistical analysis)

**Master Vocabulary List:**
- `master_prohibited_words.json` - Required dependency for phases 2 and 10
- Contains AI-associated terms, phrases, and pattern rules
- Also available in Markdown: `master_prohibited_words.md`

**Prompt Standardization Tools** (for development):
- `PROMPT_TEMPLATE.json` - Master template with all standardized sections tagged [REQUIRED], [OPTIONAL], [PHASE-SPECIFIC]
- `PROMPT_STANDARDS.md` - Human-readable standardization rules and naming conventions
- `validate_prompt.py` - Python script for automated prompt conformance validation
- `STANDARDIZATION_SUMMARY.md` - Implementation guide and current standardization status

**Documentation** (`docs/` directory):
- `USAGE_GUIDE.md` - Step-by-step processing instructions
- `TECHNICAL_REFERENCE.md` - LLM optimization & automation guides
- `CUSTOMIZATION.md` - Advanced configuration
- `CHANGELOG.md` - Version history (v3.1.0+)
- `DEVELOPMENTAL_EDITOR_GUIDE.md` - Advanced editing techniques and phase-by-phase improvement strategies
- `HUMANIZATION_GAP_ANALYSIS.md` - Research on humanization effectiveness
- `How AI Detectors Work.md` - Research basis for design decisions
- `STYLE_GUIDE.md` - One-page writing style reference for text generation (NEW v3.3.0)
- `JSON_OPTIMIZATION_ANALYSIS.md` - Comprehensive analysis of optimization opportunities (NEW v3.3.0)
- `OPTIMIZATION_COMPLETION_REPORT.md` - Detailed results of JSON optimization implementation (NEW v3.3.0)
- `GENRE_SPECIFIC_SEPARATION_SUMMARY.md` - Guide to optional romance/erotica word lists (NEW v3.3.0)

**Examples** (`examples/` directory):
- `n8n_workflow_sample.json` - Ready-to-import automation workflow
- `n8n_chapter_loop_workflow.json` - Chapter-based batch processing workflow
- `N8N_CHAPTER_LOOP_GUIDE.md` - Instructions for chapter loop automation
- Various YAML pipeline configurations for different LLM providers

**Other Files:**
- `README.md` - Project overview with model selection and quick start guides
- `GEMINI.md` - Gemini-specific guidance (similar to this file)
- `DOCUMENTATION_UPDATES.md` - Record of documentation changes in v3.1.0

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
| 3 | Purple prose + nominalization | No | De-nominalization, passive voice reduction |
| 4 | Flat passage improvement | No | Sensory detail enhancement |
| 5 | Obvious statement conversion | No | Adds subtlety and implication |
| 6 | Dialogue content ONLY | No | Temperature 1.0 recommended |
| 6.1 | Character-specific dialogue (optional) | No | Project-specific customization |
| 7 | Weak language patterns | No | 12 categories including transitions |
| 8 | Rhythm + punctuation variation | No | Strategic imperfections, sentence rhythm |
| 8.5 | Structural construction elimination (new v3.2.0) | No | 29 syntactic patterns, mechanical construction removal |
| 9 | AI pattern detection (qualitative) | No | N-grams, perplexity phrases, pattern families |
| 9.5 | Statistical analysis (optional) | No | Burstiness, POS diversity, TTR metrics |
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

## Prompt Standardization (v3.1.0+)

All phase prompts follow a standardized structure for consistency, maintainability, and optimal LLM comprehension:

### Standardization Resources

- **`PROMPT_TEMPLATE.json`** - Master template with all sections tagged as [REQUIRED], [OPTIONAL], or [PHASE-SPECIFIC]
  - Copy-paste starting point for new phases
  - Includes inline guidance and placeholders
  - Shows exact section ordering and naming conventions

- **`PROMPT_STANDARDS.md`** - Human-readable documentation of standardization rules
  - Complete section order requirements
  - Standardized wording that must be identical across all phases
  - Naming conventions for consistency
  - Common mistakes to avoid

- **`validate_prompt.py`** - Automated validation script for prompt conformance
  - Checks structure, required sections, and standardized wording
  - Color-coded output (errors, warnings, info)
  - Exit codes for CI/CD integration
  - Single file or batch validation

- **`STANDARDIZATION_SUMMARY.md`** - Implementation guide and current status
  - What was created and why
  - Current standardization status
  - Common issues and how to fix them
  - Benefits and next steps

### Standard Structure

All phase prompts follow this exact section order:
1. **Header Block** - title, version, date, assembly_line_position, description
2. **Domain Definition** - domain_restrictions with only_handle, never_touch, respect_assembly_line
3. **Persona & Framework** - persona, agent_directives, anti_hallucination_framework
4. **Special Notes** (optional) - master list references, word filtering notes, statistical notes
5. **Phase-Specific Content** - processing_instructions, detection_criteria, enhancement_techniques, etc.
6. **Output Format** - standardized across all phases with [bracketed] placeholders only
7. **Critical Final Instruction** - standardized wording with phase-specific [placeholder]

### Quick Validation

```bash
python validate_prompt.py <phase_file.json>  # Check single file
python validate_prompt.py --all              # Check all phases
```

**Output legend:**
- ✗ ERROR (red) - Critical issue, must fix
- ⚠ WARNING (yellow) - Should fix for consistency
- ℹ INFO (blue) - Suggestion or minor issue

## Common Development Tasks

### Modifying Phase Prompts

When editing a phase JSON file:

1. **Read the entire prompt first** to understand domain boundaries
2. **Review `PROMPT_TEMPLATE.json`** to understand standardized structure
3. **Check `never_touch` rules** - do not violate domain isolation
4. **Update version number** using semantic versioning (MAJOR.MINOR.PATCH)
5. **Update date field** to current date (YYYY-MM-DD)
6. **Maintain standard structure** - sections should follow template order from PROMPT_STANDARDS.md
7. **Use standardized field names** - processing_instructions, detection_criteria, not core_instructions or processing_steps
8. **Validate changes** - run `python validate_prompt.py <file>.json` before committing
9. **Test domain isolation** - ensure phase only affects its designated domain
10. **Test sequential integration** - run through full pipeline to verify no breaking changes

### Creating New Phase Prompts

1. **Copy `PROMPT_TEMPLATE.json`** as starting point
2. **Review section order** in PROMPT_STANDARDS.md
3. **Replace all [bracketed placeholders]** with phase-specific content
4. **Remove all COMMENT_ fields** and _TEMPLATE_INSTRUCTIONS sections
5. **Remove [OPTIONAL] sections** that don't apply to your phase
6. **Add phase-specific sections** using standardized naming conventions:
   - `processing_instructions` (not "core_instructions")
   - `detection_criteria` or `detection_framework`
   - `enhancement_techniques` or `optimization_strategies`
   - `replacement_guidelines` or `conversion_strategies`
7. **Validate** - run `python validate_prompt.py new_phase.json`
8. **Fix any errors** - address ERROR-level issues before committing
9. **Test** - verify phase works correctly in isolation and in full pipeline

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

**Phase 8.5 addition (v3.2.0):**
- Created to eliminate syntactic construction patterns that substitute form for content
- 29 pattern frameworks covering mechanical constructions, anthropomorphized concepts, echo-line poetics, narrative intrusion, false emotional shorthand
- Based on comprehensive analysis of "AI BANNED Construction.md" source document
- Inserted between Phase 8 (rhythm work) and Phase 9 (AI pattern detection)
- Eliminates 7 critical patterns not covered by any existing phase
- Can be used standalone, selectively, or integrated as standard pipeline phase

**Prompt Standardization (v3.1.0):**
- Created `PROMPT_TEMPLATE.json` as master template for all phases
- Established `PROMPT_STANDARDS.md` for consistent structure and naming
- Added `validate_prompt.py` for automated conformance checking
- Implemented hierarchical N-gram consolidation in Phase 9
- Optimized phase files by consolidating redundancy (~200 lines reduced across 6 phases)
- Introduced `STANDARDIZATION_SUMMARY.md` as implementation guide

**Phase 9 refactor (v17.0.0):**
- Separated qualitative (pattern) and quantitative (statistical) analysis
- Statistical metrics moved to Phase 9.5 for consolidated single-pass analysis
- Phase 9 now focuses on N-grams and perplexity patterns with hierarchical family organization
- Bracket notation for optional pattern extensions (e.g., "it is important [to/to note that]")

**Phase 10 addition (v3.0.0):**
- Created to catch prohibited words reintroduced by phases 3-9
- Pure word filtering - no statistical analysis
- Final quality control checkpoint

**Optional phases:**
- 6.1: Added for project-specific character dialogue customization
- 9.5: Added to consolidate all statistical analysis in one pass

**Documentation evolution:**
- `DEVELOPMENTAL_EDITOR_GUIDE.md` added for advanced editing techniques
- `HUMANIZATION_GAP_ANALYSIS.md` added for effectiveness research
- `N8N_CHAPTER_LOOP_GUIDE.md` and workflow added for batch processing
- `DOCUMENTATION_UPDATES.md` added to track v3.1.0 changes