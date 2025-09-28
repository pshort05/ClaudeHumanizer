# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with this repository.

## Project Overview

ClaudeHumanizer is a mature, production-ready AI text humanization system featuring a specialized 9-phase assembly line that transforms AI-generated content into natural, human-like writing. The system uses domain-specialized prompts that work sequentially to eliminate AI detection markers while preserving meaning and voice.

## Repository Structure

```
ClaudeHumanizer/
├── README.md                           # Professional overview and quick start
├── master_prohibited_words.json        # AI-associated terms to avoid
├── 1_grammar_foundation.json          # Phase 1: Grammar correction
├── 2_ai_word_cleaning.json            # Phase 2: AI vocabulary removal
├── 3_overwritten_language_reduction.json # Phase 3: Purple prose elimination
├── 4_sensory_enhancement.json         # Phase 4: Flat passage improvement
├── 5_subtlety_creation.json          # Phase 5: Obvious statement conversion
├── 6_dialogue_enhancement.json       # Phase 6: Character voice refinement
├── 6.1_character_dialogue_pass.json  # Optional: Character-specific targeting
├── 7_weak_language_cleanup.json      # Phase 7: Weak language patterns
├── 8_strategic_imperfections.json    # Phase 8: Natural rhythm variation
├── 9_final_verification.json         # Phase 9: AI pattern detection
└── docs/
    ├── USAGE_GUIDE.md                # Complete user instructions
    ├── TECHNICAL_REFERENCE.md        # LLM optimization & automation
    └── CUSTOMIZATION.md              # Advanced configuration options
```

## Development Workflow

### Core Principles

1. **Assembly Line Architecture**: Each phase specializes in exactly one domain
2. **Sequential Processing**: Phases must run in order (1→2→3→4→5→6→7→8→9)
3. **Domain Isolation**: No phase interferes with others' specialized work
4. **Master List Integration**: Phases 2,5,6,7,8,9 require `master_prohibited_words.json`

### Prompt Development Standards

When creating or modifying prompts:

**File Naming Convention:**
- Use numbered prefixes: `1_phase_name.json` through `9_phase_name.json`
- Optional phases use decimal notation: `6.1_character_dialogue_pass.json`

**JSON Structure Requirements:**
```json
{
  "phase_name": "Descriptive Phase Name",
  "version": "X.X",
  "dependencies": ["master_prohibited_words.json"],
  "domain": "Specific processing domain only",
  "assembly_line_role": "How this fits in the sequential process",
  "never_touch": ["Domains handled by other phases"],
  "prompt": "The actual system prompt content..."
}
```

**Quality Standards:**
- Each prompt must be domain-specific and never overlap with other phases
- Include clear "never touch" rules to prevent interference
- Test with sample content to verify domain boundaries
- Ensure compatibility with master prohibited words list

### Testing and Validation

**Before committing prompt changes:**

1. **Domain Isolation Test**: Verify the prompt only affects its designated domain
2. **Sequential Integration Test**: Run through full 9-phase pipeline
3. **Master List Compatibility**: Ensure prohibited words integration works
4. **Quality Regression Test**: Compare before/after results for quality

**Sample Test Workflow:**
```bash
# Test individual phase
echo "Test content" | process_phase 3

# Test full pipeline integration
echo "Test content" | process_phases 1-9

# Test with master prohibited words
echo "Test content" | process_phase 2 --with-master-list
```

### Documentation Maintenance

**When modifying the system:**

1. **Update version numbers** in affected JSON files
2. **Update documentation** in relevant docs/ files
3. **Maintain backwards compatibility** or document breaking changes
4. **Update examples** in Usage Guide if workflow changes

### Advanced Development

**Character Dialogue Customization:**
- Modify `6.1_character_dialogue_pass.json` for project-specific characters
- Follow template structure in `docs/CUSTOMIZATION.md`
- Test character voice consistency after changes

**Master Prohibited Words Management:**
- Add new categories to `master_prohibited_words.json`
- Update version number and changelog
- Test across all dependent phases (2,5,6,7,8,9)

**Automation Integration:**
- Reference `docs/TECHNICAL_REFERENCE.md` for API configurations
- Test rate limiting and error handling
- Validate quality metrics and cost tracking

## Repository Maintenance

### Regular Tasks

**Monthly:**
- Review and update master prohibited words list
- Check for new AI-associated terms in the wild
- Validate prompt effectiveness with current AI models

**Quarterly:**
- Review LLM model recommendations in Technical Reference
- Update cost estimates and performance benchmarks
- Assess new automation platform compatibility

**As Needed:**
- Add new character types to customization examples
- Create genre-specific configuration templates
- Update API integration guides for new LLM providers

### Quality Assurance

**All changes must:**
- Preserve the assembly line architecture
- Maintain domain specialization boundaries
- Pass integration tests with existing phases
- Include appropriate documentation updates

**Never:**
- Modify multiple phase domains simultaneously
- Break sequential processing dependencies
- Remove master prohibited words list integration
- Change core assembly line principles without extensive testing

## Current State

ClaudeHumanizer is a mature, production-ready system with:
- ✅ Complete 9-phase assembly line implementation
- ✅ Comprehensive documentation suite
- ✅ Automation integration guides
- ✅ Character customization framework
- ✅ Quality assurance protocols
- ✅ Professional repository structure

The system is actively maintained and ready for production use across various text humanization workflows.