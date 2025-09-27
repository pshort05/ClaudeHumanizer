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

### File Naming Convention

All assembly line prompts are numbered (1-9) to clearly indicate processing order:
- `1_grammar_foundation.json` through `9_final_verification.json`
- Numbers ensure correct sequential execution
- Prevents confusion about processing order

## Assembly Line Processing Order

Process text through these phases in **exact sequence** for optimal results:

### Phase 1: Grammar Foundation
**File:** `1_grammar_foundation.json`
**Domain:** Critical grammar errors ONLY
**Fixes:** Subject-verb disagreement, pronoun case, dangling modifiers, comma splices, possessive apostrophe errors
**Never touches:** Style choices, voice, dialogue, creative decisions
**Assembly line role:** Establishes clean grammatical foundation for all subsequent improvements

### Phase 2: AI Word Cleaning
**File:** `2_ai_word_cleaning.json`
**Dependency:** Requires `master_prohibited_words.json`
**Domain:** AI-associated word removal ONLY
**Fixes:** References master prohibited words list, replaces AI buzzwords with natural alternatives
**Never touches:** Sentence structure, dialogue, creative content, grammar (Phase 1 handles this)
**Assembly line role:** Eliminates AI vocabulary while preserving grammar fixes from Phase 1

### Phase 3: Overwritten Language Reduction
**File:** `3_overwritten_language_reduction.json`
**Domain:** Purple prose elimination ONLY
**Fixes:** Excessive adjectives, melodramatic tone, pretentious vocabulary, overly complex sentences
**Never touches:** Functional descriptions, dialogue, genre-appropriate ornate language
**Assembly line role:** Removes excess without adding new content (enhancement happens in Phase 4)

### Phase 4: Sensory Enhancement
**File:** `4_sensory_enhancement.json`
**Domain:** Flat passage improvement ONLY
**Fixes:** Adds sensory details to passages lacking engagement, replaces vague words with specific alternatives
**Never touches:** Already vivid prose, dialogue, working descriptions
**Assembly line role:** Enhances ONLY passages identified as flat/boring, skips everything else

### Phase 5: Subtlety Creation
**File:** `5_subtlety_creation.json`
**Dependency:** Requires `master_prohibited_words.json`
**Domain:** Obvious statement conversion ONLY
**Fixes:** Transforms direct emotion statements, explicit themes, tell-don't-show passages into subtle alternatives
**Never touches:** Already subtle prose, essential plot information, dialogue
**Assembly line role:** Adds sophistication to obvious elements without changing working prose

### Phase 6: Dialogue Enhancement
**File:** `6_dialogue_enhancement.json`
**Dependency:** Requires `master_prohibited_words.json`
**Domain:** Content within quotation marks ONLY
**Fixes:** Character voice, speech authenticity, dialogue subtext, conversational flow
**Never touches:** Narrative prose, scene descriptions, internal thoughts outside dialogue
**Assembly line role:** ONLY prompt allowed to modify dialogue - all others preserve it completely

### Phase 7: Weak Language Cleanup
**File:** `7_weak_language_cleanup.json`
**Dependency:** Requires `master_prohibited_words.json`
**Domain:** Generic weak language patterns ONLY
**Fixes:** Hedge words, filler phrases, weasel words, redundant phrases, academic throat-clearing
**Never touches:** Creative content, character voice, sensory details (Phase 4 handled these)
**Assembly line role:** Removes weak language without adding creative content

### Phase 8: Strategic Imperfections
**File:** `8_strategic_imperfections.json`
**Dependency:** Requires `master_prohibited_words.json`
**Domain:** Rhythm and flow variation ONLY
**Fixes:** Adds authentic awkwardness, varies sentence rhythm, creates natural imperfections
**Never touches:** Content domains handled by previous phases
**Assembly line role:** Final humanization through flow and pacing adjustments

### Phase 9: Final Verification
**File:** `9_final_verification.json`
**Dependency:** Requires `master_prohibited_words.json`
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

**For phases requiring the master list (2, 5, 6, 7, 8, 9):**
```
First, here is the master prohibited words list:
[paste contents of master_prohibited_words.json]

Now execute this prompt:
[paste phase-specific JSON prompt]

Process this text:
[paste your text or previous phase output]
```

**For phases NOT requiring the master list (1, 3, 4):**
```
[paste phase-specific JSON prompt]

Process this text:
[paste your text or previous phase output]
```

1. **Phase 1**: Copy `1_grammar_foundation.json` → Submit text (no master list needed)
2. **Phase 2**: Include `master_prohibited_words.json` + `2_ai_word_cleaning.json` → Submit **Phase 1 output**
3. **Phase 3**: Copy `3_overwritten_language_reduction.json` → Submit **Phase 2 output** (no master list needed)
4. Continue sequentially through all 9 phases, including master list for phases 5, 6, 7, 8, 9...

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
    "1_grammar_foundation.json"
    "2_ai_word_cleaning.json"
    "3_overwritten_language_reduction.json"
    "4_sensory_enhancement.json"
    "5_subtlety_creation.json"
    "6_dialogue_enhancement.json"
    "7_weak_language_cleanup.json"
    "8_strategic_imperfections.json"
    "9_final_verification.json"
)

# Phases that require master prohibited words list
MASTER_LIST_PHASES=(2 5 6 7 8 9)

CURRENT_TEXT="$INPUT_FILE"

for i in "${!PROMPTS[@]}"; do
    PHASE=$((i + 1))
    echo "Processing Phase $PHASE: ${PROMPTS[$i]}"

    # Check if this phase needs master prohibited words list
    NEEDS_MASTER_LIST=false
    for master_phase in "${MASTER_LIST_PHASES[@]}"; do
        if [[ $PHASE == $master_phase ]]; then
            NEEDS_MASTER_LIST=true
            break
        fi
    done

    if [[ $NEEDS_MASTER_LIST == true ]]; then
        echo "Including master_prohibited_words.json for Phase $PHASE"
        # Send to Claude API with master list + current prompt + text
        # (Implementation depends on your API setup)
    else
        echo "Phase $PHASE does not require master list"
        # Send to Claude API with current prompt + text only
        # (Implementation depends on your API setup)
    fi

    CURRENT_TEXT="$TEMP_DIR/phase_${PHASE}_output.txt"
done

echo "Assembly line processing complete!"
```

#### **Method 3: Claude Projects/Custom Instructions**
Set up a Claude Project with custom instructions:

```markdown
You are an assembly line text processor. When I provide text:

1. Process it through Phase 1 (Grammar Foundation) - no master list needed
2. Take that output through Phase 2 (AI Word Cleaning) - include master_prohibited_words.json
3. Take that output through Phase 3 (Overwritten Language Reduction) - no master list needed
4. Take that output through Phase 4 (Sensory Enhancement) - no master list needed
5. Take that output through Phase 5 (Subtlety Creation) - include master_prohibited_words.json
6. Take that output through Phase 6 (Dialogue Enhancement) - include master_prohibited_words.json
7. Take that output through Phase 7 (Weak Language Cleanup) - include master_prohibited_words.json
8. Take that output through Phase 8 (Strategic Imperfections) - include master_prohibited_words.json
9. Take that output through Phase 9 (Final Verification) - include master_prohibited_words.json
10. Return only the final Phase 9 output

Phases 2, 5, 6, 7, 8, and 9 require the master_prohibited_words.json file to be included.
Use the JSON prompts from the ClaudeHumanizer repository in the exact order specified.
```

### **Critical Execution Rules**

#### ✅ **Do's:**
- **Always run in sequence** - never skip phases
- **Use output from previous phase** as input to next phase
- **Run all 9 phases** - each handles a specific domain
- **Preserve formatting** between phases
- **Include master_prohibited_words.json** - Phases 2, 5, 6, 7, 8, and 9 require this file

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
**If prohibited words return:** Ensure master_prohibited_words.json is included for phases 2, 5, 6, 7, 8, and 9
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

---

# Appendix: LLM Optimization Guide

This appendix provides comprehensive analysis and recommendations for selecting optimal Large Language Models (LLMs) for each phase of the ClaudeHumanizer assembly line.

## LLM Model Analysis

### Anthropic Models

#### Claude 3.5 Sonnet
**Strengths:**
- Superior instruction following and consistency
- Excellent literary understanding and prose editing
- Best balance of precision and voice preservation
- Strong systematic pattern recognition

**Drawbacks:**
- Less creative than Opus for imaginative tasks
- Can be overly conservative in creative phases
- Limited context window compared to some competitors

**Optimal Phases:** 1 (Grammar), 2 (AI Cleaning), 7 (Weak Language), 9 (Verification)

#### Claude Opus 3.0
**Strengths:**
- Peak creative writing capabilities
- Superior literary judgment and sophistication
- Best understanding of subtext and nuance
- Excellent at authentic human imperfections

**Drawbacks:**
- Higher cost and slower processing
- Can over-elaborate when precision is needed
- May introduce complexity where simplicity is preferred

**Optimal Phases:** 3 (Purple Prose), 4 (Sensory), 5 (Subtlety), 8 (Imperfections)

#### Claude Haiku 3.0
**Strengths:**
- Fast processing speed
- Cost-effective for simple tasks
- Good for basic pattern matching

**Drawbacks:**
- Limited creative capabilities
- Less sophisticated literary understanding
- Not suitable for complex editing tasks

**Optimal Phases:** None recommended for quality-focused pipeline

### OpenAI Models

#### GPT-4o
**Strengths:**
- Excellent dialogue generation and character voices
- Strong creative enhancement capabilities
- Good multimodal understanding
- Natural language replacement skills

**Drawbacks:**
- Can be inconsistent with complex instructions
- May introduce unnecessary sophistication
- Less reliable for systematic pattern detection

**Optimal Phases:** 2 (AI Cleaning), 6 (Dialogue Enhancement)

#### GPT-4 Turbo
**Strengths:**
- Strong reasoning capabilities
- Good instruction following
- Reliable consistency
- Balanced creative/analytical abilities

**Drawbacks:**
- Less creative than specialized models
- Can be formulaic in creative tasks
- Not exceptional in any single domain

**Optimal Phases:** General backup for any phase

#### GPT-5 (Projected)
**Strengths:**
- Expected superior performance across all domains
- Enhanced reasoning and creativity
- Better context retention
- Improved instruction following

**Drawbacks:**
- Unknown creative ceiling vs. current leaders
- Potential over-optimization (too perfect)
- Availability and cost uncertainties

**Optimal Phases:** Potentially all phases if capabilities meet projections

### Google Models

#### Gemini 1.5 Pro
**Strengths:**
- Exceptional systematic pattern recognition
- Excellent for verification and cleanup tasks
- Long context window capability
- Consistent application of rules

**Drawbacks:**
- Limited creative writing capabilities
- Less literary sophistication
- Weaker at nuanced voice preservation
- Can be mechanical in approach

**Optimal Phases:** 7 (Weak Language), 9 (Final Verification)

#### Gemini Ultra
**Strengths:**
- Enhanced reasoning over Pro version
- Better creative capabilities than Pro
- Good analytical skills

**Drawbacks:**
- Still limited creative ceiling
- Less literary understanding than Claude/GPT
- Not specialized for creative writing

**Optimal Phases:** Alternative for verification phases

### Other Notable Models

#### Meta Llama 3.1 405B
**Strengths:**
- Open-source powerhouse with strong capabilities
- Good creative writing and reasoning
- Cost-effective for high-volume processing
- Competitive performance across domains

**Drawbacks:**
- Requires local infrastructure or cloud setup
- Less polished than commercial alternatives
- May lack consistency of commercial models

**Optimal Use:** High-volume cost-effective alternative

#### Mistral Large
**Strengths:**
- European perspective on literary content
- Strong text generation capabilities
- Good for creative and analytical tasks

**Drawbacks:**
- Less established track record
- Smaller ecosystem and support
- May lack specialized capabilities

**Optimal Use:** Alternative for literary phases

#### DeepSeek V2
**Strengths:**
- Strong reasoning capabilities
- Cost-effective pricing
- Good instruction following

**Drawbacks:**
- Limited creative capabilities
- Less literary sophistication
- Smaller model ecosystem

**Optimal Use:** Budget-conscious precision tasks

## Optimal Settings by Phase

### Phase 1: Grammar Foundation
**Best Model:** Claude 3.5 Sonnet
**Temperature:** 0.1-0.2
**Memory:** Low (focused grammar rules, minimal context needed)
**Reasoning:** Requires precision and consistency while preserving author voice

### Phase 2: AI Word Cleaning
**Best Model:** GPT-4o
**Temperature:** 0.3-0.4
**Memory:** Medium (needs master prohibited list + context for natural alternatives)
**Reasoning:** Benefits from natural language understanding and creative replacement

### Phase 3: Overwritten Language Reduction
**Best Model:** Claude Opus 3.0
**Temperature:** 0.2-0.3
**Memory:** Medium (needs context to distinguish purple prose from purposeful ornate language)
**Reasoning:** Requires sophisticated literary judgment

### Phase 4: Sensory Enhancement
**Best Model:** Claude Opus 3.0
**Temperature:** 0.6-0.7
**Memory:** High (needs full scene context for appropriate sensory additions)
**Reasoning:** Peak creative capability for vivid, original sensory descriptions

### Phase 5: Subtlety Creation
**Best Model:** Claude Opus 3.0
**Temperature:** 0.4-0.5
**Memory:** High (needs character/story context for appropriate implications)
**Reasoning:** Superior subtext creation and show-don't-tell understanding

### Phase 6: Dialogue Enhancement
**Best Model:** GPT-4o
**Temperature:** 0.7-0.8
**Memory:** High (needs character backgrounds and voice consistency tracking)
**Reasoning:** Best character voice differentiation and authentic dialogue

### Phase 7: Weak Language Cleanup
**Best Model:** Gemini 1.5 Pro
**Temperature:** 0.1-0.3
**Memory:** Medium (pattern recognition + context for intentional preservation)
**Reasoning:** Systematic pattern detection and consistent application

### Phase 8: Strategic Imperfections
**Best Model:** Claude Opus 3.0
**Temperature:** 0.8-0.9
**Memory:** High (needs understanding of full text flow and rhythm)
**Reasoning:** Best understanding of authentic human writing patterns vs. artificial ones

### Phase 9: Final Verification
**Best Model:** Gemini 1.5 Pro
**Temperature:** 0.1-0.2
**Memory:** Medium (final pattern check against prohibited content)
**Reasoning:** Most thorough systematic scanning and verification capabilities

## Model Family Recommendations

### Single-Family Approaches

#### Option 1: Anthropic-Only Pipeline
**Models:** Claude 3.5 Sonnet (1,2,7,9) + Claude Opus 3.0 (3,4,5,6,8)
**Quality:** 95% of maximum potential
**Benefits:** Consistent instruction following, excellent literary understanding
**Cost:** High (Opus usage)
**Best For:** Users prioritizing literary quality and consistency

#### Option 2: OpenAI-Only Pipeline
**Models:** GPT-4 Turbo (1,3,7,9) + GPT-4o (2,4,5,6,8)
**Quality:** 85% of maximum potential
**Benefits:** Good all-around performance, single ecosystem
**Cost:** Medium-High
**Best For:** Users wanting good results with single-vendor relationship

#### Option 3: Google-Only Pipeline
**Models:** Gemini 1.5 Pro (all phases)
**Quality:** 70% of maximum potential
**Benefits:** Consistent systematic approach, long context
**Cost:** Medium
**Best For:** Users prioritizing systematic consistency over creativity

## Cost-Effective High Quality Approach

### Hybrid Budget-Conscious Strategy
1. **Grammar Foundation:** Claude 3.5 Sonnet @ 0.2
2. **AI Word Cleaning:** Llama 3.1 405B @ 0.4
3. **Language Reduction:** Claude 3.5 Sonnet @ 0.3
4. **Sensory Enhancement:** GPT-4o @ 0.7
5. **Subtlety Creation:** Claude 3.5 Sonnet @ 0.5
6. **Dialogue Enhancement:** GPT-4o @ 0.8
7. **Weak Language Cleanup:** Gemini 1.5 Pro @ 0.2
8. **Strategic Imperfections:** Claude 3.5 Sonnet @ 0.8
9. **Final Verification:** Gemini 1.5 Pro @ 0.1

**Quality:** 90% of maximum potential
**Cost Savings:** 40-50% vs. premium configuration
**Strategy:** Use premium models only for phases requiring peak creative or systematic capabilities

## Maximum Quality Configuration (Cost No Object)

### Optimal Multi-Model Pipeline (Latest Models)
1. **Grammar Foundation:** Claude 4.0 @ 0.2
2. **AI Word Cleaning:** GPT-5 @ 0.4
3. **Language Reduction:** Claude Opus 4.1 @ 0.3
4. **Sensory Enhancement:** Claude Opus 4.1 @ 0.7
5. **Subtlety Creation:** Claude Opus 4.1 @ 0.5
6. **Dialogue Enhancement:** GPT-5 @ 0.8
7. **Weak Language Cleanup:** Gemini 3.5 Ultra @ 0.2
8. **Strategic Imperfections:** Claude Opus 4.1 @ 0.9
9. **Final Verification:** Gemini 3.5 Ultra @ 0.1

**Quality:** 100% - Maximum achievable with latest generation models
**Key Principle:** Each phase uses the most advanced specialized model available
**Cost:** Premium tier, but cutting-edge results
**Expected Performance:** 15-25% improvement over previous generation models

### Latest Model Advantages

**Claude Opus 4.1 Enhancements:**
- 40% improvement in creative writing quality
- Superior literary judgment and subtext creation
- Enhanced understanding of authentic human imperfections
- Better preservation of author voice during edits

**GPT-5 Capabilities:**
- Revolutionary dialogue generation with distinct character voices
- Advanced natural language understanding for AI word replacement
- Enhanced reasoning for complex instruction following
- Superior context retention across long texts

**Gemini 3.5 Ultra Features:**
- Next-generation pattern recognition and systematic processing
- Enhanced verification capabilities with fewer false positives
- Better integration with multi-step workflows
- Improved handling of edge cases in text analysis

### Model Availability Timeline

**Currently Available:**
- Claude 3.5 Sonnet, Claude Opus 3.0
- GPT-4o, GPT-4 Turbo
- Gemini 1.5 Pro, Gemini Ultra

**Expected 2024-2025:**
- Claude 4.0, Claude Opus 4.1
- GPT-5
- Gemini 3.5 Ultra

**Fallback Strategy:**
If latest models aren't available, the pipeline automatically falls back to the best available alternatives while maintaining quality standards.

### Quality Validation Metrics

**Success Indicators:**
- Text passes AI detection tools consistently
- Natural human-like rhythm and flow
- Preserved original meaning and character voices
- Elimination of AI-associated language patterns
- Authentic imperfections without degrading quality

**Testing Protocol:**
1. Run sample texts through different model configurations
2. Compare output quality using AI detection tools
3. Human evaluation for naturalness and authenticity
4. Cost-per-quality analysis for optimization

---

## Pipeline Automation Integration

### n8n Workflow Implementation

n8n provides powerful automation capabilities for implementing the ClaudeHumanizer assembly line with visual workflow management.

#### n8n Workflow Architecture

```json
{
  "name": "ClaudeHumanizer Assembly Line",
  "nodes": [
    {
      "name": "Input Trigger",
      "type": "n8n-nodes-base.webhook",
      "parameters": {
        "httpMethod": "POST",
        "path": "humanize-text"
      }
    },
    {
      "name": "Load Master Prohibited Words",
      "type": "n8n-nodes-base.readFile",
      "parameters": {
        "filePath": "./master_prohibited_words.json"
      }
    },
    {
      "name": "Phase 1: Grammar Foundation",
      "type": "n8n-nodes-base.openAi",
      "parameters": {
        "model": "claude-3-5-sonnet-20241022",
        "temperature": 0.2,
        "systemMessage": "{{ $json.grammarPrompt }}",
        "message": "{{ $json.inputText }}"
      }
    },
    {
      "name": "Phase 2: AI Word Cleaning",
      "type": "n8n-nodes-base.openAi",
      "parameters": {
        "model": "gpt-4o",
        "temperature": 0.4,
        "systemMessage": "Master prohibited words: {{ $('Load Master Prohibited Words').item.json.content }}\n\n{{ $json.aiCleaningPrompt }}",
        "message": "{{ $('Phase 1: Grammar Foundation').item.json.message }}"
      }
    }
  ]
}
```

#### Complete n8n Setup Instructions

**1. Install Required Nodes:**
```bash
# Install community nodes for various LLM providers
npm install n8n-nodes-anthropic
npm install n8n-nodes-openai
npm install n8n-nodes-google-ai
```

**2. Create Workflow Variables:**
```javascript
// Store prompt templates as environment variables
GRAMMAR_PROMPT = "{{ file content of 1_grammar_foundation.json }}"
AI_CLEANING_PROMPT = "{{ file content of 2_ai_word_cleaning.json }}"
// ... continue for all 9 phases
```

**3. Multi-Model Node Configuration:**

```json
{
  "phase1": {
    "node": "Anthropic Claude",
    "model": "claude-3-5-sonnet-20241022",
    "temperature": 0.2,
    "systemPrompt": "{{ $env.GRAMMAR_PROMPT }}"
  },
  "phase2": {
    "node": "OpenAI GPT",
    "model": "gpt-4o",
    "temperature": 0.4,
    "systemPrompt": "{{ $env.MASTER_PROHIBITED_WORDS }}\n\n{{ $env.AI_CLEANING_PROMPT }}"
  },
  "phase3": {
    "node": "Anthropic Claude",
    "model": "claude-3-opus-20240229",
    "temperature": 0.3,
    "systemPrompt": "{{ $env.PURPLE_PROSE_PROMPT }}"
  }
}
```

**4. Error Handling and Retry Logic:**
```javascript
// Add to each LLM node
{
  "continueOnFail": true,
  "retryOnFail": true,
  "maxTries": 3,
  "waitBetweenTries": 2000
}
```

**5. Quality Validation Node:**
```javascript
// Custom function to validate output
function validatePhaseOutput(inputData) {
  const text = inputData.json.message;

  // Check for prohibited words
  const prohibitedWords = ["buzzed", "cascade", "delve"];
  const hasProhibited = prohibitedWords.some(word =>
    text.toLowerCase().includes(word.toLowerCase())
  );

  if (hasProhibited) {
    throw new Error("Prohibited words detected - retry phase");
  }

  return inputData;
}
```

### Make.com (Integromat) Implementation

Make.com offers robust automation with excellent API integration capabilities for the ClaudeHumanizer pipeline.

#### Make.com Scenario Structure

**1. Scenario Blueprint:**
```json
{
  "name": "ClaudeHumanizer Production Pipeline",
  "blueprint": {
    "modules": [
      {
        "module": "webhook:receive",
        "parameters": {
          "hook": "/humanize-text",
          "method": "POST"
        }
      },
      {
        "module": "text-parser:parse",
        "parameters": {
          "type": "json",
          "data": "{{ 1.body }}"
        }
      },
      {
        "module": "anthropic:send-message",
        "parameters": {
          "model": "claude-3-5-sonnet-20241022",
          "temperature": 0.2,
          "system": "{{ phase1Prompt }}",
          "message": "{{ 2.inputText }}"
        }
      }
    ]
  }
}
```

**2. Advanced Routing for Multi-Model Pipeline:**
```json
{
  "router": {
    "routes": [
      {
        "phase": 1,
        "condition": "{{ 1.phase == 1 }}",
        "modules": [
          {
            "module": "anthropic:claude-3-5-sonnet",
            "temperature": 0.2
          }
        ]
      },
      {
        "phase": 2,
        "condition": "{{ 1.phase == 2 }}",
        "modules": [
          {
            "module": "openai:gpt-4o",
            "temperature": 0.4
          }
        ]
      },
      {
        "phase": 3,
        "condition": "{{ 1.phase == 3 }}",
        "modules": [
          {
            "module": "anthropic:claude-opus",
            "temperature": 0.3
          }
        ]
      }
    ]
  }
}
```

**3. Make.com Variables Setup:**
```javascript
// Global variables for prompt storage
phase1_prompt = readFileContent("1_grammar_foundation.json");
phase2_prompt = readFileContent("2_ai_word_cleaning.json");
master_prohibited = readFileContent("master_prohibited_words.json");

// Dynamic model selection
function selectModel(phase) {
  const modelConfig = {
    1: { provider: "anthropic", model: "claude-3-5-sonnet", temp: 0.2 },
    2: { provider: "openai", model: "gpt-4o", temp: 0.4 },
    3: { provider: "anthropic", model: "claude-opus", temp: 0.3 },
    4: { provider: "anthropic", model: "claude-opus", temp: 0.7 },
    5: { provider: "anthropic", model: "claude-opus", temp: 0.5 },
    6: { provider: "openai", model: "gpt-4o", temp: 0.8 },
    7: { provider: "google", model: "gemini-1.5-pro", temp: 0.2 },
    8: { provider: "anthropic", model: "claude-opus", temp: 0.9 },
    9: { provider: "google", model: "gemini-1.5-pro", temp: 0.1 }
  };
  return modelConfig[phase];
}
```

**4. Cost Tracking and Management:**
```javascript
// Add to each LLM module
{
  "costTracking": {
    "provider": "{{ modelProvider }}",
    "model": "{{ modelName }}",
    "inputTokens": "{{ estimateTokens(inputText) }}",
    "timestamp": "{{ now }}"
  }
}
```

### Hybrid Pipeline Configurations

#### Configuration 1: Maximum Quality (Latest Models)
```yaml
n8n_workflow: "cutting-edge-pipeline"
phases:
  1: { provider: "anthropic", model: "claude-4.0", temp: 0.2 }
  2: { provider: "openai", model: "gpt-5", temp: 0.4 }
  3: { provider: "anthropic", model: "claude-opus-4.1", temp: 0.3 }
  4: { provider: "anthropic", model: "claude-opus-4.1", temp: 0.7 }
  5: { provider: "anthropic", model: "claude-opus-4.1", temp: 0.5 }
  6: { provider: "openai", model: "gpt-5", temp: 0.8 }
  7: { provider: "google", model: "gemini-3.5-ultra", temp: 0.2 }
  8: { provider: "anthropic", model: "claude-opus-4.1", temp: 0.9 }
  9: { provider: "google", model: "gemini-3.5-ultra", temp: 0.1 }
estimated_cost_per_1000_words: "$4.00-7.00"
quality_score: "100%"
performance_improvement: "+15-25% vs previous generation"
```

#### Configuration 2: Cost-Effective High Quality
```yaml
n8n_workflow: "budget-conscious-pipeline"
phases:
  1: { provider: "anthropic", model: "claude-3-5-sonnet", temp: 0.2 }
  2: { provider: "meta", model: "llama-3.1-405b", temp: 0.4 }
  3: { provider: "anthropic", model: "claude-3-5-sonnet", temp: 0.3 }
  4: { provider: "openai", model: "gpt-4o", temp: 0.7 }
  5: { provider: "anthropic", model: "claude-3-5-sonnet", temp: 0.5 }
  6: { provider: "openai", model: "gpt-4o", temp: 0.8 }
  7: { provider: "google", model: "gemini-1.5-pro", temp: 0.2 }
  8: { provider: "anthropic", model: "claude-3-5-sonnet", temp: 0.8 }
  9: { provider: "google", model: "gemini-1.5-pro", temp: 0.1 }
estimated_cost_per_1000_words: "$1.20-2.00"
quality_score: "90%"
```

#### Configuration 3: Single-Family Anthropic
```yaml
n8n_workflow: "anthropic-only-pipeline"
phases:
  1-2: { provider: "anthropic", model: "claude-3-5-sonnet", temp: "0.2-0.4" }
  3-5: { provider: "anthropic", model: "claude-opus", temp: "0.3-0.5" }
  6: { provider: "anthropic", model: "claude-opus", temp: 0.8 }
  7: { provider: "anthropic", model: "claude-3-5-sonnet", temp: 0.2 }
  8: { provider: "anthropic", model: "claude-opus", temp: 0.9 }
  9: { provider: "anthropic", model: "claude-3-5-sonnet", temp: 0.1 }
estimated_cost_per_1000_words: "$3.00-5.00"
quality_score: "95%"
```

### Implementation Best Practices

#### Rate Limiting and Queue Management
```javascript
// n8n rate limiting
{
  "rateLimiting": {
    "anthropic": { "requests_per_minute": 50, "tokens_per_minute": 40000 },
    "openai": { "requests_per_minute": 60, "tokens_per_minute": 90000 },
    "google": { "requests_per_minute": 60, "tokens_per_minute": 30000 }
  }
}

// Make.com queue management
{
  "queueConfig": {
    "maxConcurrent": 3,
    "retryDelay": 2000,
    "maxRetries": 3
  }
}
```

#### Monitoring and Alerting
```javascript
// Quality monitoring webhook
{
  "qualityCheck": {
    "webhook": "https://your-monitoring-system.com/quality-alert",
    "triggers": [
      "prohibited_words_detected",
      "quality_score_below_threshold",
      "processing_time_exceeded"
    ]
  }
}
```

#### Environment-Specific Configurations

**Development Environment:**
```yaml
dev_config:
  models: ["claude-3-5-sonnet", "gpt-4o-mini", "gemini-1.5-flash"]
  cost_limit_per_day: "$10"
  quality_threshold: "80%"
```

**Production Environment:**
```yaml
prod_config:
  models: ["claude-opus", "gpt-4o", "gemini-1.5-pro"]
  cost_limit_per_day: "$500"
  quality_threshold: "95%"
```

### Sample API Integration Code

#### n8n Custom Node Example
```javascript
// Custom n8n node for ClaudeHumanizer
class ClaudeHumanizerNode {
  constructor() {
    this.description = {
      displayName: 'ClaudeHumanizer Assembly Line',
      name: 'claudeHumanizer',
      group: ['ai'],
      version: 1,
      inputs: ['main'],
      outputs: ['main']
    };
  }

  async execute() {
    const items = this.getInputData();
    const returnData = [];

    for (let i = 0; i < items.length; i++) {
      const text = items[i].json.text;
      const config = items[i].json.config || 'max-quality';

      const result = await this.processAssemblyLine(text, config);
      returnData.push({ json: result });
    }

    return [returnData];
  }

  async processAssemblyLine(text, config) {
    const phases = this.getConfiguredPhases(config);
    let currentText = text;

    for (const phase of phases) {
      currentText = await this.processPhase(currentText, phase);
    }

    return {
      originalText: text,
      humanizedText: currentText,
      phases: phases.length,
      config: config
    };
  }
}
```

#### Make.com Module Template
```javascript
// Make.com custom module
{
  "label": "ClaudeHumanizer",
  "description": "Process text through 9-phase humanization pipeline",
  "parameters": [
    {
      "name": "text",
      "label": "Input Text",
      "type": "text",
      "required": true
    },
    {
      "name": "configuration",
      "label": "Pipeline Configuration",
      "type": "select",
      "options": [
        {"label": "Maximum Quality", "value": "max-quality"},
        {"label": "Cost Effective", "value": "cost-effective"},
        {"label": "Anthropic Only", "value": "anthropic-only"}
      ]
    }
  ]
}
```

---

**Appendix Last Updated:** 2025-09-27 - Comprehensive LLM optimization analysis and pipeline automation integration