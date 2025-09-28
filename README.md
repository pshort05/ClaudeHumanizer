# ClaudeHumanizer

A professional AI text humanization system using a specialized 9-phase assembly line to transform AI-generated content into natural, human-like writing while preserving meaning and voice.

## Overview

ClaudeHumanizer employs a **domain-specialized assembly line** where each phase targets one specific aspect of text improvement. This systematic approach eliminates AI detection markers while maintaining quality through:

- **Sequential processing** - Each phase builds on previous improvements
- **Domain isolation** - No phase interferes with others' specialized work
- **Master prohibited list** - Prevents reintroduction of AI-associated terms
- **Silent operation** - Returns improved text without commentary

## Quick Start

### Basic Workflow

1. **Download required files**: 9 phase prompts + `master_prohibited_words.json`
2. **Process sequentially**: Phase 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9
3. **Include master list**: Required for phases 2, 5, 6, 7, 8, 9
4. **Use previous output**: Each phase processes the result from the previous phase

### Execution Methods

#### Manual Processing
Copy each phase prompt into Claude with appropriate dependencies:

```
For phases 2, 5, 6, 7, 8, 9:
[master_prohibited_words.json content]
[phase prompt]
[input text]

For phases 1, 3, 4:
[phase prompt]
[input text]
```

#### Claude Project Setup
Configure custom instructions for automated sequential processing (see [Usage Guide](docs/USAGE_GUIDE.md))

#### Automation Integration
Set up n8n, Make.com, or API workflows (see [Technical Reference](docs/TECHNICAL_REFERENCE.md))

## Assembly Line Phases

### Core Processing Phases

| Phase | File | Domain | Dependencies |
|-------|------|--------|--------------|
| 1 | `1_grammar_foundation.json` | Grammar errors only | None |
| 2 | `2_ai_word_cleaning.json` | AI vocabulary removal | Master list |
| 3 | `3_overwritten_language_reduction.json` | Purple prose elimination | None |
| 4 | `4_sensory_enhancement.json` | Flat passage improvement | None |
| 5 | `5_subtlety_creation.json` | Obvious statement conversion | Master list |
| 6 | `6_dialogue_enhancement.json` | Character voice refinement | Master list |
| 7 | `7_weak_language_cleanup.json` | Weak language patterns | Master list |
| 8 | `8_strategic_imperfections.json` | Natural rhythm variation | Master list |
| 9 | `9_final_verification.json` | AI pattern detection | Master list |

### Optional Enhancement

**Phase 6.1**: `6.1_character_dialogue_pass.json` - Character-specific dialogue customization for targeted voice refinement (see [Customization Guide](docs/CUSTOMIZATION.md))

## Key Features

### ✅ Domain Specialization
- Each phase handles exactly one improvement type
- Clear boundaries prevent interference between phases
- Specialized expertise for consistent results

### ✅ Quality Assurance
- Master prohibited words list prevents AI term reintroduction
- Sequential dependencies ensure cumulative improvements
- Only Phase 6 modifies dialogue - all others preserve it

### ✅ Flexibility
- Optional character-specific dialogue enhancement
- Configurable for different content types and genres
- Compatible with automation workflows

## File Structure

```
ClaudeHumanizer/
├── README.md                           # This overview
├── master_prohibited_words.json        # AI terms to avoid
├── 1_grammar_foundation.json          # Phase 1 prompt
├── 2_ai_word_cleaning.json            # Phase 2 prompt
├── 3_overwritten_language_reduction.json
├── 4_sensory_enhancement.json
├── 5_subtlety_creation.json
├── 6_dialogue_enhancement.json
├── 6.1_character_dialogue_pass.json   # Optional
├── 7_weak_language_cleanup.json
├── 8_strategic_imperfections.json
├── 9_final_verification.json
└── docs/
    ├── USAGE_GUIDE.md                 # Step-by-step instructions
    ├── TECHNICAL_REFERENCE.md         # LLM optimization & automation
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
🧹 Phase 2: AI Word Cleaning → Natural vocabulary
    ↓
✂️ Phase 3: Purple Prose Reduction → Cleaner descriptions
    ↓
🎨 Phase 4: Sensory Enhancement → Engaging passages
    ↓
🎭 Phase 5: Subtlety Creation → Sophisticated implications
    ↓
💬 Phase 6: Dialogue Enhancement → Authentic voices
    ↓
🎭 Phase 6.1: Character-Specific (Optional) → Targeted refinement
    ↓
🔍 Phase 7: Weak Language Cleanup → Stronger expressions
    ↓
🎯 Phase 8: Strategic Imperfections → Natural rhythm
    ↓
✨ Phase 9: Final Verification → Human-like result
```

## Benefits

- **Eliminates circular processing** - No phase undoes another's work
- **Prevents term reintroduction** - Master list ensures consistency
- **Specialized expertise** - Each phase excels at one improvement type
- **Predictable results** - Systematic approach ensures quality
- **Scalable workflow** - Compatible with manual and automated processing

## Requirements

- Access to Claude AI (recommended) or compatible LLM
- All 9 phase prompt files + master prohibited words list
- Sequential processing capability (manual or automated)

## Getting Started

1. **Read the [Usage Guide](docs/USAGE_GUIDE.md)** for detailed instructions
2. **Download all required files** from the repository
3. **Start with a small text sample** to understand the process
4. **Process through all 9 phases sequentially**
5. **Review results** and adjust workflow as needed

For advanced users, see the [Technical Reference](docs/TECHNICAL_REFERENCE.md) for automation options and the [Customization Guide](docs/CUSTOMIZATION.md) for project-specific configurations.

---

**Version**: 2.0 Assembly Line Architecture
**Last Updated**: 2025-09-25