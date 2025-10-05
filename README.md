# ClaudeHumanizer

**⚠️ Optimized for Claude (Anthropic) - Best results with Claude Sonnet 4.5**

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

### Basic Workflow

1. **Download required files**: 10 phase prompts + `master_prohibited_words.json`
2. **Process sequentially**: Phase 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10
3. **Include master list**: Required for phases 2 and 10 (contains pattern rules)
4. **Use previous output**: Each phase processes the result from the previous phase
5. **Use Claude Sonnet 4.5**: Recommended for all phases with temperature 1.0 for Phase 6 (dialogue)

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

#### Claude Project Setup (RECOMMENDED)
Configure custom instructions for automated sequential processing using Claude Sonnet 4.5 (see [Usage Guide](docs/USAGE_GUIDE.md))

#### Automation Integration
Set up n8n, Make.com, or API workflows (see [Technical Reference](docs/TECHNICAL_REFERENCE.md))

## Assembly Line Phases

### Core Processing Phases

| Phase | File | Domain | Dependencies | Pattern Rules |
|-------|------|--------|--------------|---------------|
| 1 | `1_grammar_foundation.json` | Grammar errors only | None | - |
| 2 | `2_ai_word_cleaning.json` | AI vocabulary removal | Master list | Dialogue pauses, Light descriptions, Finger actions |
| 3 | `3_overwritten_language_reduction.json` | Purple prose elimination | None | - |
| 4 | `4_sensory_enhancement.json` | Flat passage improvement | None | - |
| 5 | `5_subtlety_creation.json` | Obvious statement conversion | None | - |
| 6 | `6_dialogue_enhancement.json` | Character voice refinement (temp 1.0) | None | - |
| 7 | `7_weak_language_cleanup.json` | Weak language patterns (12 categories) | None | - |
| 8 | `8_strategic_imperfections.json` | Natural rhythm variation | None | - |
| 9 | `9_final_verification.json` | AI pattern detection (no word filtering) | None | - |
| 10 | `10_final_ai_word_sweep.json` | **NEW** Final prohibited word sweep | Master list | All pattern rules |

### Optional Enhancement

**Phase 6.1**: `6.1_character_dialogue_pass.json` - Character-specific dialogue customization for targeted voice refinement (see [Customization Guide](docs/CUSTOMIZATION.md))

## Key Features

### ✅ Domain Specialization
- Each phase handles exactly one improvement type
- Clear boundaries prevent interference between phases
- Specialized expertise for consistent results

### ✅ Pattern-Based Intelligence (NEW)
- **Dialogue Pause Rules** - Eliminates "weight of words", "silence stretched", etc.
- **Light Description Rules** - Replaces "filtering through", "casting shadows" with simple alternatives
- **Finger Action Rules** - Converts "fingers dancing" to direct action verbs like "typing"
- Pattern matching catches creative variations automatically

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
├── master_prohibited_words.json        # Pattern rules & prohibited terms
├── 1_grammar_foundation.json          # Phase 1 prompt
├── 2_ai_word_cleaning.json            # Phase 2 prompt (with pattern rules)
├── 3_overwritten_language_reduction.json
├── 4_sensory_enhancement.json
├── 5_subtlety_creation.json
├── 6_dialogue_enhancement.json
├── 6.1_character_dialogue_pass.json   # Optional
├── 7_weak_language_cleanup.json
├── 8_strategic_imperfections.json
├── 9_final_verification.json
├── 10_final_ai_word_sweep.json        # NEW: Phase 10 final sweep
└── docs/
    ├── USAGE_GUIDE.md                 # Step-by-step instructions
    ├── TECHNICAL_REFERENCE.md         # Claude optimization & automation
    └── CUSTOMIZATION.md               # Advanced configuration
```

## Documentation

### 📖 [Usage Guide](docs/USAGE_GUIDE.md)
Complete step-by-step instructions for processing text through the assembly line system, including troubleshooting and quality control.

### ⚙️ [Technical Reference](docs/TECHNICAL_REFERENCE.md)
Advanced technical information including LLM optimization recommendations, automation integration guides, and API configurations.

### 🎛️ [Customization Guide](docs/CUSTOMIZATION.md)
Advanced customization options including character-specific dialogue enhancement and project-specific configurations.

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

- **Claude Sonnet 4.5** (strongly recommended) or compatible LLM
- All 10 phase prompt files + master prohibited words list
- Sequential processing capability (manual or automated)
- Temperature 1.0 for Phase 6 (dialogue enhancement)

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
**Last Updated**: 2025-10-05
**Optimized For**: Claude Sonnet 4.5