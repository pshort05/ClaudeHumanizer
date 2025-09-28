# ClaudeHumanizer Usage Guide

Complete step-by-step instructions for using the ClaudeHumanizer assembly line system to transform AI-generated text into natural, human-like writing.

## Table of Contents

- [Quick Start](#quick-start)
- [Assembly Line Overview](#assembly-line-overview)
- [Execution Methods](#execution-methods)
- [Phase-by-Phase Guide](#phase-by-phase-guide)
- [Dependencies](#dependencies)
- [Troubleshooting](#troubleshooting)
- [Quality Control](#quality-control)

## Quick Start

### Minimum Viable Process

1. **Download Required Files**:
   - All 9 phase prompts (`1_grammar_foundation.json` through `9_final_verification.json`)
   - `master_prohibited_words.json`

2. **Process Your Text**:
   ```
   Phase 1 → Phase 2 → Phase 3 → Phase 4 → Phase 5 → Phase 6 → Phase 7 → Phase 8 → Phase 9
   ```

3. **Include Master List**: Phases 2, 5, 6, 7, 8, and 9 require `master_prohibited_words.json`

4. **Use Previous Output**: Each phase processes the output from the previous phase

## Assembly Line Overview

The ClaudeHumanizer operates as a **true assembly line** where each phase specializes in ONE specific domain:

### Domain Specialization
- **Phase 1**: Grammar errors ONLY
- **Phase 2**: AI-associated words ONLY
- **Phase 3**: Purple prose elimination ONLY
- **Phase 4**: Flat passage enhancement ONLY
- **Phase 5**: Obvious statement conversion ONLY
- **Phase 6**: Dialogue content ONLY
- **Phase 7**: Weak language patterns ONLY
- **Phase 8**: Rhythm and flow variation ONLY
- **Phase 9**: Final AI pattern detection ONLY

### Key Features
- ✅ **No interference** - Each prompt only works in its domain
- ✅ **Master prohibited list** - Prevents reintroduction of AI terms
- ✅ **Sequential dependencies** - Later phases build on earlier work
- ✅ **Dialogue protection** - Only Phase 6 modifies quoted speech

## Execution Methods

### Method 1: Manual Individual Execution

Copy and paste each prompt with proper dependencies:

#### For Phases Requiring Master List (2, 5, 6, 7, 8, 9):
```
First, here is the master prohibited words list:
[paste contents of master_prohibited_words.json]

Now execute this prompt:
[paste phase-specific JSON prompt]

Process this text:
[paste your text or previous phase output]
```

#### For Phases NOT Requiring Master List (1, 3, 4):
```
[paste phase-specific JSON prompt]

Process this text:
[paste your text or previous phase output]
```

### Method 2: Claude Projects/Custom Instructions

Set up a Claude Project with these instructions:

```markdown
You are an assembly line text processor. When I provide text:

1. Process through Phase 1 (Grammar Foundation) - no master list needed
2. Take output through Phase 2 (AI Word Cleaning) - include master_prohibited_words.json
3. Take output through Phase 3 (Overwritten Language Reduction) - no master list needed
4. Take output through Phase 4 (Sensory Enhancement) - no master list needed
5. Take output through Phase 5 (Subtlety Creation) - include master_prohibited_words.json
6. Take output through Phase 6 (Dialogue Enhancement) - include master_prohibited_words.json
7. Take output through Phase 7 (Weak Language Cleanup) - include master_prohibited_words.json
8. Take output through Phase 8 (Strategic Imperfections) - include master_prohibited_words.json
9. Take output through Phase 9 (Final Verification) - include master_prohibited_words.json
10. Return only the final Phase 9 output

Phases 2, 5, 6, 7, 8, and 9 require the master_prohibited_words.json file.
Use the JSON prompts from the ClaudeHumanizer repository in exact order.
```

### Method 3: Automation Integration

See [Technical Reference](TECHNICAL_REFERENCE.md) for n8n, Make.com, and API integration guides.

## Phase-by-Phase Guide

### Phase 1: Grammar Foundation
**File**: `1_grammar_foundation.json`
**Dependencies**: None
**Purpose**: Fix critical grammar errors without changing style

**What it fixes**:
- Subject-verb disagreement
- Pronoun case errors
- Dangling modifiers
- Comma splices
- Possessive apostrophe errors

**What it preserves**:
- Author voice and style
- Creative word choices
- Dialogue authenticity
- Intentional stylistic decisions

### Phase 2: AI Word Cleaning
**File**: `2_ai_word_cleaning.json`
**Dependencies**: `master_prohibited_words.json`
**Purpose**: Remove AI-associated vocabulary

**What it fixes**:
- AI buzzwords and phrases
- Unnatural word choices
- Corporate-speak infiltration
- Robotic language patterns

**What it preserves**:
- Grammar fixes from Phase 1
- Natural sentence structure
- Character voice distinctions

### Phase 3: Overwritten Language Reduction
**File**: `3_overwritten_language_reduction.json`
**Dependencies**: None
**Purpose**: Eliminate purple prose and melodrama

**What it fixes**:
- Excessive adjectives
- Overly dramatic descriptions
- Pretentious vocabulary
- Unnecessarily complex sentences

**What it preserves**:
- Genre-appropriate ornate language
- Functional descriptions
- Working dialogue

### Phase 4: Sensory Enhancement
**File**: `4_sensory_enhancement.json`
**Dependencies**: None
**Purpose**: Add engagement to flat passages

**What it enhances**:
- Passages lacking sensory details
- Vague or generic descriptions
- Boring narrative sections

**What it avoids**:
- Already vivid prose
- Working dialogue
- Over-description

### Phase 5: Subtlety Creation
**File**: `5_subtlety_creation.json`
**Dependencies**: `master_prohibited_words.json`
**Purpose**: Convert obvious statements to subtle implications

**What it transforms**:
- Direct emotion statements
- Explicit theme declarations
- Tell-don't-show passages
- Heavy-handed messaging

**What it preserves**:
- Essential plot information
- Already subtle prose
- Character dialogue

### Phase 6: Dialogue Enhancement
**File**: `6_dialogue_enhancement.json`
**Dependencies**: `master_prohibited_words.json`
**Purpose**: Improve character voice and speech authenticity

**What it enhances**:
- Character voice distinction
- Conversational flow
- Speech authenticity
- Dialogue subtext

**Critical note**: ONLY phase allowed to modify quoted speech

### Phase 6.1: Character-Specific Dialogue (Optional)
**File**: `6.1_character_dialogue_pass.json`
**When to use**: When specific characters need targeted voice refinement
**Dependencies**: Character specifications, `master_prohibited_words.json`

See [Customization Guide](CUSTOMIZATION.md) for detailed setup instructions.

### Phase 7: Weak Language Cleanup
**File**: `7_weak_language_cleanup.json`
**Dependencies**: `master_prohibited_words.json`
**Purpose**: Remove generic weak language patterns

**What it removes**:
- Hedge words and filler phrases
- Weasel words
- Redundant expressions
- Academic throat-clearing

**What it preserves**:
- Creative content from previous phases
- Character-specific speech patterns
- Intentional hesitation in dialogue

### Phase 8: Strategic Imperfections
**File**: `8_strategic_imperfections.json`
**Dependencies**: `master_prohibited_words.json`
**Purpose**: Add authentic human flow variations

**What it adds**:
- Natural sentence rhythm variation
- Authentic awkwardness
- Human-like pacing
- Organic imperfections

**What it avoids**:
- Content changes handled by other phases
- Breaking established character voices
- Introducing errors

### Phase 9: Final Verification
**File**: `9_final_verification.json`
**Dependencies**: `master_prohibited_words.json`
**Purpose**: Quality control and final polish

**What it catches**:
- Remaining AI patterns missed by previous phases
- Consistency issues
- Final prohibited word check

**What it avoids**:
- Major content changes
- Redoing previous phases' work

## Dependencies

### Required Files by Phase

| Phase | Prompt File | Master List Required |
|-------|-------------|---------------------|
| 1 | `1_grammar_foundation.json` | ❌ No |
| 2 | `2_ai_word_cleaning.json` | ✅ Yes |
| 3 | `3_overwritten_language_reduction.json` | ❌ No |
| 4 | `4_sensory_enhancement.json` | ❌ No |
| 5 | `5_subtlety_creation.json` | ✅ Yes |
| 6 | `6_dialogue_enhancement.json` | ✅ Yes |
| 6.1 | `6.1_character_dialogue_pass.json` | ✅ Yes |
| 7 | `7_weak_language_cleanup.json` | ✅ Yes |
| 8 | `8_strategic_imperfections.json` | ✅ Yes |
| 9 | `9_final_verification.json` | ✅ Yes |

### Master Prohibited Words List
**File**: `master_prohibited_words.json`
**Purpose**: Single source of truth for AI-associated terms to avoid

Must be included with phases: 2, 5, 6, 7, 8, 9

## Troubleshooting

### Common Issues

**Text becomes worse after processing**:
- ✅ Check: Are you running phases in correct order?
- ✅ Check: Are you using output from previous phase as input?
- ✅ Check: Are you skipping any phases?

**Prohibited words keep returning**:
- ✅ Check: Is `master_prohibited_words.json` included for phases 2, 5, 6, 7, 8, 9?
- ✅ Check: Are you using the most recent version of the master list?

**Dialogue changes unexpectedly**:
- ✅ Check: Only Phase 6 should modify dialogue
- ✅ Check: Other phases should preserve quoted speech completely

**Grammar gets broken in later phases**:
- ✅ Check: Phase 1 ran successfully first
- ✅ Check: Later phases are preserving grammar fixes

**Character voices become inconsistent**:
- ✅ Consider using Phase 6.1 for character-specific refinement
- ✅ Check character specifications are properly defined

### Processing Flow Validation

After each phase, verify:
- ✅ Text is improved in that phase's domain
- ✅ Previous phases' work is preserved
- ✅ Text is ready for next phase

### Performance Issues

**Slow processing**:
- Consider automation tools (see [Technical Reference](TECHNICAL_REFERENCE.md))
- Use batch processing for multiple texts
- Optimize LLM selection per phase

**Inconsistent results**:
- Verify exact prompt versions
- Check temperature settings if using API
- Ensure consistent model selection

## Quality Control

### Success Indicators
- Text passes AI detection tools consistently
- Natural human-like rhythm and flow
- Preserved original meaning and character voices
- Elimination of AI-associated language patterns
- Authentic imperfections without quality degradation

### Quality Checkpoints

**After Phase 1**: Grammar should be clean without style changes
**After Phase 2**: AI vocabulary removed, natural alternatives present
**After Phase 3**: Purple prose reduced, clarity improved
**After Phase 4**: Flat passages more engaging
**After Phase 5**: Obvious statements converted to implications
**After Phase 6**: Character voices distinct and authentic
**After Phase 7**: Weak language eliminated
**After Phase 8**: Natural rhythm and imperfections present
**After Phase 9**: All AI patterns eliminated, ready for publication

### Final Validation
1. **AI Detection Test**: Run through multiple AI detection tools
2. **Human Reading Test**: Does it sound naturally written?
3. **Character Consistency**: Are voices distinct without tags?
4. **Meaning Preservation**: Is original intent intact?
5. **Quality Improvement**: Is it better than the original?

---

For advanced configuration and customization options, see the [Customization Guide](CUSTOMIZATION.md).
For technical implementation and automation, see the [Technical Reference](TECHNICAL_REFERENCE.md).