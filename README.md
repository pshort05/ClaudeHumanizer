# Claude Humanizer

A comprehensive collection of Claude prompts designed to transform AI-generated text into natural, human-like writing. These specialized editors work together as an **assembly line system** to eliminate AI detection markers while preserving meaning, voice, and quality.

## Overview

These prompts operate in **silent mode** by default - they process text and return only the improved version without commentary or analysis, unless explicitly asked for feedback. The system has been redesigned as a **true assembly line** where each prompt specializes in ONE specific domain and never interferes with others' work.

## ✨ New Assembly Line Architecture

The system now prevents conflicts through **domain specialization**:
- Each prompt handles ONE specific aspect of prose improvement
- Clear boundaries prevent prompts from undoing each other's work
- **Master prohibited words list** prevents reintroduction of AI-associated terms
- Sequential processing builds improvements without interference

## Master Prohibited Words List

**File:** `master_prohibited_words.json`
**Purpose:** Consolidated list of all AI-associated terms and phrases that should be avoided across all prompts. This single source of truth prevents the reintroduction problem where later prompts would add back terms that earlier prompts removed.

## Assembly Line Processing Order

Process text through these phases in **exact sequence** for optimal results:

### Phase 1: Grammar Foundation
**File:** `strunk_white_editor.json`
**Domain:** Critical grammar errors ONLY
**Fixes:** Subject-verb disagreement, pronoun case, dangling modifiers, comma splices, possessive apostrophe errors
**Never touches:** Style choices, voice, dialogue, creative decisions
**Assembly line role:** Establishes clean grammatical foundation for all subsequent improvements

### Phase 2: AI Word Cleaning
**File:** `ai_text_cleaner.json`
**Domain:** AI-associated word removal ONLY
**Fixes:** References master prohibited words list, replaces AI buzzwords with natural alternatives
**Never touches:** Sentence structure, dialogue, creative content, grammar (Phase 1 handles this)
**Assembly line role:** Eliminates AI vocabulary while preserving grammar fixes from Phase 1

### Phase 3: Overwritten Language Reduction
**File:** `purple_prose_removal.json`
**Domain:** Purple prose elimination ONLY
**Fixes:** Excessive adjectives, melodramatic tone, pretentious vocabulary, overly complex sentences
**Never touches:** Functional descriptions, dialogue, genre-appropriate ornate language
**Assembly line role:** Removes excess without adding new content (enhancement happens in Phase 4)

### Phase 4: Sensory Enhancement
**File:** `fix_boring_prose.json`
**Domain:** Flat passage improvement ONLY
**Fixes:** Adds sensory details to passages lacking engagement, replaces vague words with specific alternatives
**Never touches:** Already vivid prose, dialogue, working descriptions
**Assembly line role:** Enhances ONLY passages identified as flat/boring, skips everything else

### Phase 5: Subtlety Creation
**File:** `on_the_nose_editor.json`
**Domain:** Obvious statement conversion ONLY
**Fixes:** Transforms direct emotion statements, explicit themes, tell-don't-show passages into subtle alternatives
**Never touches:** Already subtle prose, essential plot information, dialogue
**Assembly line role:** Adds sophistication to obvious elements without changing working prose

### Phase 6: Dialogue Enhancement
**File:** `dialogue_enhancer.json`
**Domain:** Content within quotation marks ONLY
**Fixes:** Character voice, speech authenticity, dialogue subtext, conversational flow
**Never touches:** Narrative prose, scene descriptions, internal thoughts outside dialogue
**Assembly line role:** ONLY prompt allowed to modify dialogue - all others preserve it completely

### Phase 7: Weak Language Cleanup
**File:** `text_quality_prompt.json`
**Domain:** Generic weak language patterns ONLY
**Fixes:** Hedge words, filler phrases, weasel words, redundant phrases, academic throat-clearing
**Never touches:** Creative content, character voice, sensory details (Phase 4 handled these)
**Assembly line role:** Removes weak language without adding creative content

### Phase 8: Strategic Imperfections
**File:** `human_writing_editor.json`
**Domain:** Rhythm and flow variation ONLY
**Fixes:** Adds authentic awkwardness, varies sentence rhythm, creates natural imperfections
**Never touches:** Content domains handled by previous phases
**Assembly line role:** Final humanization through flow and pacing adjustments

### Phase 9: Final Verification
**File:** `claude_humanizer.json`
**Domain:** AI pattern detection and minor adjustments ONLY
**Fixes:** Catches any remaining AI patterns missed by previous 8 phases, final consistency check
**Never touches:** Major content changes (all handled by specialized phases)
**Assembly line role:** Quality control and final polish without redoing previous work

## Key Assembly Line Features

### ✅ **Domain Separation**
Each prompt only works within its assigned domain - no overlap or interference

### ✅ **Conflict Prevention**
Clear "never touch" rules prevent prompts from undoing each other's work

### ✅ **Master Prohibited List**
Single source of truth prevents reintroduction of AI-associated terms across all phases

### ✅ **Sequential Dependencies**
Later phases build upon and respect the work of earlier phases

### ✅ **Dialogue Handling Resolution**
Only Phase 6 (Dialogue Enhancer) modifies quoted speech - all others preserve it completely

## How to Execute the Assembly Line System

### **Sequential Execution Required**

The prompts **must** be run in exact order - each phase builds on the previous work:

```
Phase 1 → Phase 2 → Phase 3 → Phase 4 → Phase 5 → Phase 6 → Phase 7 → Phase 8 → Phase 9
```

### **Execution Methods**

#### **Method 1: Individual Prompt Execution**
Copy the JSON prompt content and paste it into Claude, then submit your text:

1. **Phase 1**: Copy `strunk_white_editor.json` → Paste into Claude → Submit text
2. **Phase 2**: Copy `ai_text_cleaner.json` → Paste into Claude → Submit **Phase 1 output**
3. **Phase 3**: Copy `purple_prose_removal.json` → Paste into Claude → Submit **Phase 2 output**
4. Continue sequentially through all 9 phases...

#### **Method 2: Batch Processing Script** (Recommended)
Create a script that processes text through all phases automatically:

```bash
#!/bin/bash
# Process text through ClaudeHumanizer assembly line

INPUT_FILE="$1"
TEMP_DIR="/tmp/claude_processing"
mkdir -p "$TEMP_DIR"

# Array of prompts in correct order
PROMPTS=(
    "strunk_white_editor.json"
    "ai_text_cleaner.json"
    "purple_prose_removal.json"
    "fix_boring_prose.json"
    "on_the_nose_editor.json"
    "dialogue_enhancer.json"
    "text_quality_prompt.json"
    "human_writing_editor.json"
    "claude_humanizer.json"
)

CURRENT_TEXT="$INPUT_FILE"

for i in "${!PROMPTS[@]}"; do
    PHASE=$((i + 1))
    echo "Processing Phase $PHASE: ${PROMPTS[$i]}"

    # Send to Claude API with current prompt and text
    # (Implementation depends on your API setup)

    CURRENT_TEXT="$TEMP_DIR/phase_${PHASE}_output.txt"
done

echo "Assembly line processing complete!"
```

#### **Method 3: Claude Projects/Custom Instructions**
Set up a Claude Project with custom instructions:

```markdown
You are an assembly line text processor. When I provide text:

1. Process it through Phase 1 (Strunk & White Editor)
2. Take that output through Phase 2 (AI Text Cleaner)
3. Continue through all 9 phases in sequence
4. Return only the final Phase 9 output

Use the JSON prompts from the ClaudeHumanizer repository in the exact order specified.
```

### **Critical Execution Rules**

#### ✅ **Do's:**
- **Always run in sequence** - never skip phases
- **Use output from previous phase** as input to next phase
- **Run all 9 phases** - each handles a specific domain
- **Preserve formatting** between phases
- **Reference master_prohibited_words.json** - all prompts use this

#### ❌ **Don'ts:**
- **Don't run phases in parallel** - they have dependencies
- **Don't skip phases** - you'll miss critical improvements
- **Don't run phases out of order** - later phases assume earlier work is done
- **Don't modify the text between phases** - let each prompt do its specialized work

### **Phase-by-Phase Execution Flow**

```
📝 Original Text
    ↓
🔧 Phase 1: Grammar fixes → Clean grammatical foundation
    ↓
🧹 Phase 2: AI word removal → Natural vocabulary
    ↓
✂️ Phase 3: Purple prose reduction → Cleaner descriptions
    ↓
🎨 Phase 4: Sensory enhancement → Vivid flat passages
    ↓
🎭 Phase 5: Subtlety creation → Sophisticated implications
    ↓
💬 Phase 6: Dialogue enhancement → Authentic character voices
    ↓
🔍 Phase 7: Weak language cleanup → Stronger expressions
    ↓
🎯 Phase 8: Strategic imperfections → Natural rhythm
    ↓
✨ Phase 9: Final verification → Polished human-like text
```

### **Quality Control**

After each phase, the text should be:
- ✅ **Improved** in that phase's domain
- ✅ **Unchanged** in all other domains
- ✅ **Compatible** with the next phase's expectations

### **Troubleshooting**

**If text becomes worse:** You likely skipped a phase or ran them out of order
**If prohibited words return:** Ensure master_prohibited_words.json is being referenced
**If dialogue changes unexpectedly:** Only Phase 6 should modify dialogue
**If grammar gets broken:** Phase 1 should run first and be preserved by later phases

## Usage Guidelines

### **Character-Specific Dialogue**
As noted, dialogue enhancement can be customized at runtime for character-specific voice requirements

### **Silent Operation**
All prompts return only the improved text unless explicitly asked for analysis or commentary

### **Structure Preservation**
All phases preserve titles, headers, markdown formatting, and document structure

## Assembly Line Benefits

- **Eliminates circular processing** - No prompt undoes another's work
- **Prevents reintroduction** - Master list ensures removed terms stay removed
- **Specialized expertise** - Each prompt excels at ONE specific improvement type
- **Predictable results** - Consistent output through systematic processing
- **Efficient workflow** - No redundant processing or conflicting changes

## File Versions

All prompts reference the latest assembly line architecture with updated version information and dates. The master prohibited words list is referenced by all prompts to ensure consistency.

**Last Updated:** 2025-09-25 - Assembly line architecture implementation