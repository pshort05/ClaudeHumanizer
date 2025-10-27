# ClaudeHumanizer

**⚠️ Optimized for Claude Sonnet 4.5 (Recommended) | Also supports: Gemini 2.5 Pro, GPT-5**

A professional AI text humanization system using a specialized 10-phase assembly line to transform AI-generated content into natural, human-like writing while preserving meaning and voice.

## Overview

ClaudeHumanizer employs a **domain-specialized assembly line** where each phase targets one specific aspect of text improvement. This systematic approach eliminates AI detection markers while maintaining quality through:

- **Sequential processing** - Each phase builds on previous improvements
- **Domain isolation** - No phase interferes with others' specialized work
- **Pattern-based filtering** - Intelligent rules for dialogue pauses, light descriptions, finger movements
- **Master prohibited list** - Prevents reintroduction of AI-associated terms
- **Final quality control** - Phase 10 catches prohibited words reintroduced by phases 3-9
- **Silent operation** - Returns improved text without commentary

## Quick Start

### ⚠️ Important Usage Considerations

**Non-Native English Speaker (NNES) Bias Warning**
AI detectors exhibit documented bias against non-native English speakers. NNES writing often features simpler sentence structures, more limited vocabulary, and reliance on common phrasings—characteristics that detectors may misclassify as AI-generated.

**Important**: If you are processing text originally written by an NNES writer, be aware that:
- The humanization process may inadvertently simplify vocabulary and sentence structures further
- Some NNES writing patterns are naturally similar to AI patterns (limited lexical diversity, common phrases)
- Over-processing NNES text through all phases might make it appear MORE AI-like to certain detectors
- Consider selectively applying phases rather than the full pipeline for NNES-authored content

**Hybrid Text (Human + AI) Guidance**
AI detectors often fail catastrophically on hybrid texts containing both human and AI-generated content, frequently misclassifying them as either 100% human or 100% AI with no middle ground.

**Important**: This system assumes 100% AI-generated input. If you have hybrid text:
- Manually identify which sections are human-written vs AI-generated
- Only process the AI-generated sections through the pipeline
- Keep human-written sections completely untouched
- Do NOT run mixed human/AI paragraphs through the system—process them separately
- Consider whether detection is even a concern if substantial human contribution exists

### Model Selection (October 2025)

**Choose your LLM based on priorities:**

| Model | Best For | Cost | Key Advantage |
|-------|----------|------|---------------|
| **Claude Sonnet 4.5** ⭐ | Maximum quality | $3-15/1M tokens | "Surgical" edits, natural human tone, best instruction-following |
| **Gemini 2.5 Pro** 💰 | Budget/Long texts | $1.25-15/1M tokens | 40% cheaper, 1M context, fastest (372 tok/s) |
| **GPT-5** 🔄 | ChatGPT users | Subscription | Literary style, widely available (requires stricter prompting) |

**Quick Decision:**
- **Quality priority?** → Claude Sonnet 4.5 (recommended)
- **Budget priority or text >100K words?** → Gemini 2.5 Pro
- **Already have ChatGPT Plus?** → GPT-5 (with cautions)

### Basic Workflow

1. **Download required files**: 10 phase prompts + `master_prohibited_words.json`
2. **Select your model**: Claude Sonnet 4.5 (recommended), Gemini 2.5 Pro (budget), or GPT-5
3. **Process sequentially**: Phase 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → (9.5 optional) → 10
4. **Include master list**: Required for phases 2 and 10 (contains pattern rules)
5. **Use previous output**: Each phase processes the result from the previous phase
6. **Temperature settings**: Use temperature 1.0 for Phase 6 (dialogue), standard temps for others

### Execution Methods

#### Manual Processing
Copy each phase prompt into Claude Sonnet 4.5 with appropriate dependencies:

```
For phases 2 and 10:
[master_prohibited_words.json content]
[phase prompt]
[input text]

For phases 1, 3, 4, 5, 6, 7, 8, 9:
[phase prompt]
[input text]
```

#### Claude Project Setup (RECOMMENDED for Claude users)
Configure custom instructions for automated sequential processing using Claude Sonnet 4.5 (see [Usage Guide](docs/USAGE_GUIDE.md))

#### ChatGPT Project Setup (For GPT-5 users)
Configure custom GPT or use Projects feature with GPT-5 model selection (see [Usage Guide](docs/USAGE_GUIDE.md))

#### Google AI Studio (For Gemini 2.5 Pro users)
Use Google AI Studio with Gemini 2.5 Pro for automated processing (see [Technical Reference](docs/TECHNICAL_REFERENCE.md))

#### Automation Integration
Set up n8n, Make.com, or API workflows (see [Technical Reference](docs/TECHNICAL_REFERENCE.md))

## Assembly Line Phases

### Core Processing Phases

| Phase | File | Domain | Master List | NEW Features |
|-------|------|--------|-------------|---------------|
| 1 | `1_grammar_foundation.json` | Grammar errors only | ❌ No | - |
| 2 | `2_ai_word_cleaning.json` | AI vocabulary removal | ✅ **Required** | Pattern rules |
| 3 | `3_overwritten_language_reduction.json` | Purple prose + **nominalization** | ❌ No | ✨ **De-nominalization** |
| 4 | `4_sensory_enhancement.json` | Flat passage improvement | ❌ No | - |
| 5 | `5_subtlety_creation.json` | Obvious statement conversion | ❌ No | - |
| 6 | `6_dialogue_enhancement.json` | Character voice (temp 1.0) | ❌ No | - |
| 7 | `7_weak_language_cleanup.json` | Weak language + **voice distribution** | ❌ No | ✨ **Active/passive monitoring** |
| 8 | `8_strategic_imperfections.json` | Rhythm + **punctuation inconsistency** | ❌ No | ✨ **Enhanced imperfections** |
| 9 | `9_final_verification.json` | **AI patterns** (N-grams + perplexity) | ❌ No | ✨ **Pattern replacement** |
| 10 | `10_final_ai_word_sweep.json` | **Word filtering only** | ✅ **Required** | Pure prohibited word removal |

### Optional Enhancements

**Phase 6.1**: `6.1_character_dialogue_pass.json` - Character-specific dialogue customization for targeted voice refinement (see [Customization Guide](docs/CUSTOMIZATION.md))

**Phase 9.5**: `9.5_statistical_analysis_hub.json` - **COMPREHENSIVE STATISTICAL HUB** consolidating all quantitative metrics (burstiness, POS distribution, lexical diversity/TTR) into single-pass analysis. Use when AI detection is a concern or text needs statistical optimization. Provides optional detailed metrics report.

## Key Features

### ✅ Architectural Clarity (NEW)
**Clear Separation of Concerns:**
- **Phase 9**: QUALITATIVE pattern replacement (N-grams, formulaic phrases, AI patterns)
- **Phase 9.5**: QUANTITATIVE statistical optimization (burstiness, POS, TTR) - all metrics in one pass
- **Phase 10**: Pure WORD FILTERING (prohibited words only)

**Benefits:**
- Single-pass statistical analysis = more efficient
- Coordinated metric optimization = balanced results
- Clear conceptual boundaries = easier to understand and maintain
- Optional statistics phase = skip if text is already optimized

### ✅ Domain Specialization
- Each phase handles exactly one improvement type
- Clear boundaries prevent interference between phases
- Specialized expertise for consistent results

### ✅ Pattern-Based Intelligence
- **Dialogue Pause Rules** - Eliminates "weight of words", "silence stretched", etc.
- **Light Description Rules** - Replaces "filtering through", "casting shadows" with simple alternatives
- **Finger Action Rules** - Converts "fingers dancing" to direct action verbs like "typing"
- Pattern matching catches creative variations automatically

### ✨ NEW: Research-Based Detection Countermeasures
Based on academic AI detector research, ClaudeHumanizer now includes targeted countermeasures for the latest detection methods:

**Phase 3 - Nominalization Conversion** (v2.4.0)
- Converts AI's abstract nominalized constructions to direct verbal forms
- Example: "The implementation of the solution" → "They implemented the solution"
- Addresses HIGH-priority detection marker explicitly identified in research

**Phase 8 - Punctuation Inconsistency Injection** (v4.1.0)
- Breaks AI's "machine-like consistency" in punctuation patterns
- Strategic Oxford comma variation, spacing inconsistencies, hyphenation variation
- Addresses detector-specific marker: perfect punctuation consistency

**Phase 8 - Enhanced Strategic Imperfections** (v4.1.0)
- Logical leap injection (removes over-explanation)
- Tangential thought insertion (breaks perfect linearity)
- Awkward phrasing retention (preserves authentic human voice)
- Minor typo injection (user-configurable for casual content)
- Addresses "counterintuitive perfection" detection signal

**Phase 9 - Cross-Document N-gram Filter** (v15.0.0)
- Eliminates 150+ common AI n-gram patterns (2-5+ word sequences)
- Examples: "it is important to note that", "plays a crucial role in", "in order to"
- Addresses N-gram frequency analysis used by advanced detectors

**Phase 9 - AI Pattern Detection** (v17.0.0) - REFACTORED
- Focuses on QUALITATIVE pattern replacement (N-grams, perplexity phrases)
- Removes formulaic expressions and predictable AI language patterns
- Statistical metrics moved to Phase 9.5 for consolidated analysis

**Phase 9.5 - Statistical Analysis Hub** (v2.0.0) - **NEW ARCHITECTURE**
- **Consolidates ALL quantitative metrics** into single comprehensive pass
- **Burstiness**: Sentence variation (CV, range, variance, complexity)
- **POS Distribution**: Noun/verb/adjective ratios normalized to human baselines (18-23% nouns, 16-20% verbs, 6-9% adjectives)
- **Lexical Diversity**: TTR calculation and vocabulary optimization (target 0.40-0.60)
- **Single-pass efficiency**: Reads text once, calculates all metrics, makes coordinated optimizations
- **Optional metrics report**: Detailed statistical analysis with before/after scores
- Addresses multiple detection vectors simultaneously with balanced optimization

**Phase 10 - Word Filtering Only** (v3.0.0) - SIMPLIFIED
- Pure prohibited word removal using master_prohibited_words.json
- No statistical analysis - focuses exclusively on word-level filtering
- Clean separation from statistical optimization (Phase 9.5)

### ✨ MEDIUM PRIORITY: Additional Detection Countermeasures

**Phase 7 - Active/Passive Voice Distribution Monitor** (v2.4.0)
- Analyzes active/passive voice ratios and normalizes to human baselines
- Targets: 85-90% active, 10-15% passive for narrative prose
- Prevents both excessive passive (early AI) and zero passive (over-correction)
- Addresses syntactic feature analysis used by detectors

**Phase 9 - Perplexity Optimizer** (v17.0.0)
- Systematically identifies and replaces low-perplexity (predictable) constructions
- Disrupts predictable collocations: "crystal clear" → "obvious", "highly effective" → "powerful"
- Replaces 30+ common business cliches and formulaic expressions
- Increases text unpredictability to reduce detection probability
- Now part of qualitative pattern detection (statistical metrics moved to 9.5)

**Master Prohibited Words** (updated)
- Added "underscoring its importance/significance" variants from research
- Expanded phrase coverage based on academic detector documentation

### ✅ Quality Assurance
- Master prohibited words list with intelligent pattern rules
- Phase 10 final sweep catches words reintroduced by phases 3-9
- Sequential dependencies ensure cumulative improvements
- Only Phase 6 modifies dialogue - all others preserve it

### ✅ Claude Optimization
- Prompts specifically designed for Claude's strengths
- Superior literary judgment and pattern recognition
- Best results with Claude Sonnet 4.5
- Temperature 1.0 for Phase 6 produces natural dialogue

### ✅ Flexibility
- Optional character-specific dialogue enhancement
- Configurable for different content types and genres
- Compatible with automation workflows

## File Structure

```
ClaudeHumanizer/
├── README.md                           # This overview
├── How AI Detectors Work.md            # Research basis for enhancements
├── master_prohibited_words.json        # Pattern rules & prohibited terms
├── 1_grammar_foundation.json          # Phase 1 prompt
├── 2_ai_word_cleaning.json            # Phase 2 prompt (with pattern rules)
├── 3_overwritten_language_reduction.json  # v2.4.0 + nominalization
├── 4_sensory_enhancement.json
├── 5_subtlety_creation.json
├── 6_dialogue_enhancement.json
├── 6.1_character_dialogue_pass.json   # Optional
├── 7_weak_language_cleanup.json       # v2.4.0 + voice distribution
├── 8_strategic_imperfections.json     # v4.1.0 + punctuation + imperfections
├── 9_final_verification.json          # v17.0.0 PATTERN DETECTION (qualitative)
├── 9.5_statistical_analysis_hub.json  # v2.0.0 OPTIONAL - ALL statistics consolidated
├── 10_final_ai_word_sweep.json        # v3.0.0 WORD FILTERING (pure)
└── docs/
    ├── USAGE_GUIDE.md                 # Step-by-step instructions
    ├── TECHNICAL_REFERENCE.md         # Claude optimization & automation
    ├── CUSTOMIZATION.md               # Advanced configuration
    ├── CHANGELOG.md                   # Version history & updates
    └── n8n_workflow_sample.json       # Ready-to-import n8n workflow
```

## Documentation

### 📖 [Usage Guide](docs/USAGE_GUIDE.md)
Complete step-by-step instructions for processing text through the assembly line system, including troubleshooting and quality control.

### ⚙️ [Technical Reference](docs/TECHNICAL_REFERENCE.md)
Advanced technical information including LLM optimization recommendations, automation integration guides (n8n, Make.com), and API configurations.

### 🎛️ [Customization Guide](docs/CUSTOMIZATION.md)
Advanced customization options including character-specific dialogue enhancement and project-specific configurations.

### 📋 [Changelog](docs/CHANGELOG.md)
Version history, recent updates, and migration guides. See latest changes including master list consolidation and Phase 8/9 clarifications.

### 🤖 [n8n Workflow](docs/n8n_workflow_sample.json)
Ready-to-import n8n workflow for complete 10-phase automation with Claude Sonnet 4.5. Import into n8n, configure file paths and API credentials, then activate.

## Processing Flow

```
📝 Original Text
    ↓
🔧 Phase 1: Grammar Foundation → Clean grammatical base
    ↓
🧹 Phase 2: AI Word Cleaning + Pattern Rules → Natural vocabulary
    ↓
✂️ Phase 3: Purple Prose Reduction → Cleaner descriptions
    ↓
🎨 Phase 4: Sensory Enhancement → Engaging passages
    ↓
🎭 Phase 5: Subtlety Creation → Sophisticated implications
    ↓
💬 Phase 6: Dialogue Enhancement (temp 1.0) → Authentic voices
    ↓
🎭 Phase 6.1: Character-Specific (Optional) → Targeted refinement
    ↓
🔍 Phase 7: Weak Language Cleanup (12 categories) → Stronger expressions
    ↓
🎯 Phase 8: Strategic Imperfections → Natural rhythm
    ↓
✨ Phase 9: Final Verification → AI pattern detection
    ↓
🎯 Phase 10: Final AI Word Sweep → Quality control checkpoint
```

## Benefits

- **Eliminates circular processing** - No phase undoes another's work
- **Intelligent pattern matching** - Catches AI writing patterns automatically
- **Prevents term reintroduction** - Phase 10 final sweep ensures consistency
- **Claude-optimized** - Designed for Claude's superior literary judgment
- **Specialized expertise** - Each phase excels at one improvement type
- **Predictable results** - Systematic approach ensures quality
- **Scalable workflow** - Compatible with manual and automated processing

## Requirements

- **LLM Access**: One of the following (see Model Selection above)
  - **Claude Sonnet 4.5** (recommended) - Best quality, most reliable
  - **Gemini 2.5 Pro** - Budget-friendly, excellent for long texts (1M context)
  - **GPT-5** - Good alternative for ChatGPT Plus/Pro users
- All 10 phase prompt files + master prohibited words list
- Sequential processing capability (manual or automated)
- Temperature 1.0 for Phase 6 (dialogue enhancement) across all models

## Getting Started

1. **Read the [Usage Guide](docs/USAGE_GUIDE.md)** for detailed instructions
2. **Download all required files** from the repository
3. **Set up Claude Sonnet 4.5** access (recommended)
4. **Start with a small text sample** to understand the process
5. **Process through all 10 phases sequentially**
6. **Review results** and adjust workflow as needed

For advanced users, see the [Technical Reference](docs/TECHNICAL_REFERENCE.md) for Claude optimization and automation options, and the [Customization Guide](docs/CUSTOMIZATION.md) for project-specific configurations.

---

**Version**: 3.0 Pattern-Based Architecture with Phase 10
**Last Updated**: 2025-10-26
**Optimized For**: Claude Sonnet 4.5