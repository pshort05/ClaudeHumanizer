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

**⚠️ IMPORTANT: These prompts are optimized for Claude (Anthropic). For best results, use Claude Sonnet 4.5.**

### Minimum Viable Process

1. **Download Required Files**:
   - All 10 phase prompts (`1_grammar_foundation.json` through `10_final_ai_word_sweep.json`)
   - `master_prohibited_words.json`

2. **Process Your Text**:
   ```
   Phase 1 → Phase 2 → Phase 3 → Phase 4 → Phase 5 → Phase 6 → Phase 7 → Phase 8 → Phase 9 → (Phase 9.5 optional) → Phase 10
   ```

3. **Include Master List**: Phases 2 and 10 require `master_prohibited_words.json`

4. **Optional Phase 9.5**: Include for comprehensive statistical optimization or skip for budget savings

5. **Use Previous Output**: Each phase processes the output from the previous phase

## Model Selection (October 2025)

### Choosing the Right LLM

ClaudeHumanizer supports multiple leading LLMs. Your choice depends on priorities:

| Priority | Recommended Model | Why |
|----------|------------------|-----|
| **Maximum Quality** | Claude Sonnet 4.5 ⭐ | "Surgical" edits, best instruction-following, natural human tone |
| **Budget Savings** | Gemini 2.5 Pro 💰 | 40% cheaper than Claude, excellent performance |
| **Long Texts (>100K words)** | Gemini 2.5 Pro | 1M token context vs Claude's 200K |
| **Speed Priority** | Gemini 2.5 Pro | Fastest (372 tokens/second) |
| **ChatGPT Subscriber** | GPT-5 🔄 | Already included in subscription (with caveats) |

### Model Comparison

**Claude Sonnet 4.5 (RECOMMENDED)**
- **Pricing**: $3/1M input, $15/1M output
- **Quality**: 95-98% of maximum potential
- **Strengths**:
  - Best instruction-following (respects domain boundaries)
  - "Surgical" approach (minimal changes, precise edits)
  - Natural human tone
  - Most reliable for 10-phase assembly line
- **Use when**: Quality and reliability are paramount

**Gemini 2.5 Pro (BUDGET TIER)**
- **Pricing**: $1.25-2.50/1M input, $10-15/1M output (context-dependent)
- **Quality**: 85-92% of maximum potential (estimated)
- **Strengths**:
  - 40% cost savings
  - 1M token context (5x larger than Claude)
  - Fastest processing (372 tok/s)
  - Top-ranked on LM Arena
- **Use when**: Budget matters, processing long texts, or high-volume workflows

**GPT-5 (ALTERNATIVE)**
- **Pricing**: Subscription-based (ChatGPT Plus/Pro)
- **Quality**: 80-90% of maximum potential
- **Strengths**:
  - Excellent literary style
  - Good at style mimicry
  - Widely available
- **Limitations**: ⚠️
  - Tends to "take over" and rewrite beyond instructions
  - Less "surgical" than Claude (may violate domain boundaries)
  - Requires stricter "never touch" constraints
- **Use when**: Already have ChatGPT subscription and willing to accept potential boundary issues

### Decision Tree

```
What's your primary concern?

QUALITY & RELIABILITY
  └─→ Claude Sonnet 4.5 ⭐ RECOMMENDED

BUDGET
  ├─→ Text >100K words? → Gemini 2.5 Pro (1M context advantage)
  └─→ Text <100K words? → Gemini 2.5 Pro (40% cheaper)

SPEED
  └─→ Gemini 2.5 Pro (372 tokens/second)

EXISTING SUBSCRIPTION
  └─→ Have ChatGPT Plus/Pro? → GPT-5 (included, but less reliable)

BOOK-LENGTH CONTENT
  └─→ Gemini 2.5 Pro (1M context handles 200K+ word documents)
```

**Important Notes:**
- All models use the same temperature settings
- Hybrid strategies available (see [Technical Reference](TECHNICAL_REFERENCE.md))
- For automation, n8n workflows support all three models

## Assembly Line Overview

The ClaudeHumanizer operates as a **true assembly line** where each phase specializes in ONE specific domain:

### Domain Specialization
- **Phase 1**: Grammar errors ONLY
- **Phase 2**: AI-associated words ONLY (applies pattern rules for dialogue pauses, light descriptions, finger actions)
- **Phase 3**: Purple prose elimination ONLY (includes de-nominalization)
- **Phase 4**: Flat passage enhancement ONLY
- **Phase 5**: Obvious statement conversion ONLY
- **Phase 6**: Dialogue content ONLY
- **Phase 7**: Weak language patterns ONLY (12 categories including overused transitions and robotic qualifiers)
- **Phase 8**: Rhythm and flow variation ONLY (strategic imperfections, punctuation inconsistency)
- **Phase 9**: AI pattern detection ONLY - QUALITATIVE (N-grams, formulaic phrases, perplexity)
- **Phase 9.5**: Statistical optimization ONLY - QUANTITATIVE (burstiness, POS, TTR) - **OPTIONAL**
- **Phase 10**: Word filtering ONLY (catches prohibited words reintroduced by phases 3-9)

### Key Features
- ✅ **No interference** - Each prompt only works in its domain
- ✅ **Master prohibited list** - Contains pattern-based rules (not just word lists)
- ✅ **Sequential dependencies** - Later phases build on earlier work
- ✅ **Dialogue protection** - Only Phase 6 modifies quoted speech
- ✅ **Pattern recognition** - New intelligent rules for common AI writing patterns
- ✅ **Final quality control** - Phase 10 ensures no prohibited words slip through

## Execution Methods

### Method 1: Manual Individual Execution

Copy and paste each prompt with proper dependencies:

#### For Phases Requiring Master List (2, 10):
```
First, here is the master prohibited words list:
[paste contents of master_prohibited_words.json]

Now execute this prompt:
[paste phase-specific JSON prompt]

Process this text:
[paste your text or previous phase output]
```

#### For Phases NOT Requiring Master List (1, 3, 4, 5, 6, 7, 8, 9):
```
[paste phase-specific JSON prompt]

Process this text:
[paste your text or previous phase output]
```

### Method 2: Claude Projects/Custom Instructions (RECOMMENDED)

**Use Claude Sonnet 4.5 for best results.**

Set up a Claude Project with these instructions:

```markdown
You are an assembly line text processor optimized for humanizing AI-generated text. When I provide text:

1. Process through Phase 1 (Grammar Foundation)
2. Take output through Phase 2 (AI Word Cleaning) - include master_prohibited_words.json
3. Take output through Phase 3 (Overwritten Language Reduction)
4. Take output through Phase 4 (Sensory Enhancement)
5. Take output through Phase 5 (Subtlety Creation)
6. Take output through Phase 6 (Dialogue Enhancement) - use temperature 1.0
7. Take output through Phase 7 (Weak Language Cleanup)
8. Take output through Phase 8 (Strategic Imperfections)
9. Take output through Phase 9 (Final Verification)
10. OPTIONAL: Take output through Phase 9.5 (Statistical Analysis Hub) - for comprehensive statistical optimization
11. Take output through Phase 10 (Final AI Word Sweep) - include master_prohibited_words.json
12. Return only the final Phase 10 output

IMPORTANT:
- Phases 2 and 10 require master_prohibited_words.json (contains pattern rules)
- Phase 6 should use higher creativity (temperature 1.0) for natural dialogue
- Phase 9.5 is OPTIONAL - include for maximum quality or skip for budget savings
- Use the JSON prompts from the ClaudeHumanizer repository in exact order
- Phase 10 is critical - it catches prohibited words reintroduced by phases 3-9
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
**Dependencies**: None
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
**Dependencies**: None
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
**Dependencies**: Character specifications

See [Customization Guide](CUSTOMIZATION.md) for detailed setup instructions.

### Phase 7: Weak Language Cleanup
**File**: `7_weak_language_cleanup.json`
**Dependencies**: None
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
**Dependencies**: None
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
**Dependencies**: None
**Purpose**: AI pattern detection and quality control (qualitative)

**What it catches**:
- Remaining AI patterns (perfection syndrome, predictable phrasing)
- N-gram patterns (150+ common AI sequences)
- Phrase repetition issues
- Rhythm and flow variations needed
- Perplexity enhancement opportunities (formulaic phrase replacement)

**What it avoids**:
- Word-level filtering (handled by Phase 10)
- Statistical analysis (handled by Phase 9.5)
- Major content changes
- Redoing previous phases' work

### Phase 9.5: Statistical Analysis Hub (OPTIONAL)
**File**: `9.5_statistical_analysis_hub.json`
**Dependencies**: None
**Purpose**: Comprehensive quantitative statistical optimization
**Status**: OPTIONAL - can be skipped for budget savings

**When to use**:
- AI detection is a high concern
- Text feels monotonous or statistically uniform
- Maximum quality optimization needed
- Budget allows for comprehensive processing

**When to skip**:
- Text already has good statistical properties
- Budget constraints (saves 10-15% of total cost)
- Fast turnaround is critical
- Processing large volumes

**What it optimizes**:
- **Burstiness**: Sentence length variation (CV, range, variance, complexity)
- **POS Distribution**: Noun/verb/adjective ratios normalized to human baselines
- **Lexical Diversity**: TTR (Type-Token Ratio) calculation and enhancement
- Single-pass efficiency: Reads text once, optimizes all metrics together

**What it avoids**:
- Word filtering (handled by Phase 10)
- Pattern replacement (handled by Phase 9)
- Dialogue content modification
- Meaning or factual changes

**Optional features**:
- Detailed metrics report (before/after statistics)

### Phase 10: Final AI Word Sweep
**File**: `10_final_ai_word_sweep.json`
**Dependencies**: `master_prohibited_words.json`
**Purpose**: Final quality control checkpoint

**What it catches**:
- Prohibited words reintroduced by phases 3-9
- AI vocabulary patterns missed earlier
- Pattern rule violations (dialogue pauses, light descriptions, finger actions)

**What it avoids**:
- Dialogue modification
- Sentence restructuring
- Content changes

## Dependencies

### Required Files by Phase

| Phase | Prompt File | Master List Required | Status |
|-------|-------------|---------------------|--------|
| 1 | `1_grammar_foundation.json` | ❌ No | Required |
| 2 | `2_ai_word_cleaning.json` | ✅ Yes | Required |
| 3 | `3_overwritten_language_reduction.json` | ❌ No | Required |
| 4 | `4_sensory_enhancement.json` | ❌ No | Required |
| 5 | `5_subtlety_creation.json` | ❌ No | Required |
| 6 | `6_dialogue_enhancement.json` | ❌ No | Required |
| 6.1 | `6.1_character_dialogue_pass.json` | ❌ No | Optional |
| 7 | `7_weak_language_cleanup.json` | ❌ No | Required |
| 8 | `8_strategic_imperfections.json` | ❌ No | Required |
| 9 | `9_final_verification.json` | ❌ No | Required |
| 9.5 | `9.5_statistical_analysis_hub.json` | ❌ No | **Optional** |
| 10 | `10_final_ai_word_sweep.json` | ✅ Yes | Required |

### Master Prohibited Words List
**File**: `master_prohibited_words.json`
**Purpose**: Single source of truth for AI-associated terms and pattern rules

**Must be included with phases: 2 and 10 ONLY**

- **Phase 2**: Uses pattern rules (dialogue pauses, light descriptions, finger actions) to remove AI vocabulary
- **Phase 10**: Final sweep to catch any prohibited words reintroduced by phases 3-9

## Troubleshooting

### Common Issues

**Text becomes worse after processing**:
- ✅ Check: Are you running phases in correct order?
- ✅ Check: Are you using output from previous phase as input?
- ✅ Check: Are you skipping any phases?

**Prohibited words keep returning**:
- ✅ Check: Is `master_prohibited_words.json` included for phases 2 and 10?
- ✅ Check: Are you running Phase 10 as the final step?
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
**After Phase 9**: AI patterns detected, rhythm variations applied
**After Phase 10**: All prohibited words eliminated, ready for publication

### Final Validation
1. **AI Detection Test**: Run through multiple AI detection tools
2. **Human Reading Test**: Does it sound naturally written?
3. **Character Consistency**: Are voices distinct without tags?
4. **Meaning Preservation**: Is original intent intact?
5. **Quality Improvement**: Is it better than the original?

---

For advanced configuration and customization options, see the [Customization Guide](CUSTOMIZATION.md).
For technical implementation and automation, see the [Technical Reference](TECHNICAL_REFERENCE.md).