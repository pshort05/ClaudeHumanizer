# ClaudeHumanizer Technical Reference

Advanced technical information for developers, integrators, and power users implementing the ClaudeHumanizer assembly line system.

## Table of Contents

- [Claude-Specific Instructions](#claude-specific-instructions)
- [LLM Optimization](#llm-optimization)
- [Automation Integration](#automation-integration)
- [API Configurations](#api-configurations)
- [Performance Optimization](#performance-optimization)
- [Model Selection Guide](#model-selection-guide)
- [Cost Management](#cost-management)
- [Quality Metrics](#quality-metrics)

## Claude-Specific Instructions

**IMPORTANT: These prompts are optimized for Claude models (Anthropic).**

ClaudeHumanizer has been designed and tested extensively with Claude models. While other LLMs can be used, Claude consistently delivers superior results across all phases due to:

- **Superior literary judgment** - Claude excels at distinguishing purposeful style from AI artifacts
- **Better instruction following** - Claude adheres to complex multi-constraint prompts more reliably
- **Nuanced understanding** - Claude better understands "show don't tell" and subtext creation
- **Pattern recognition** - Claude more accurately identifies and applies pattern rules (dialogue pauses, light descriptions, finger movements)

### Recommended Claude Configuration

**For Best Results (Claude-Only Pipeline):**
```yaml
models: Claude Sonnet 4.5 (all phases except creative phases) + Claude Sonnet 4.5 @ higher temperature (phases 4,5,6,8)
quality: 95-98% of maximum potential
cost: Medium-High
best_for: Consistent, high-quality humanization across all text types
```

**Why Claude Sonnet 4.5:**
- Latest model with best balance of quality, speed, and cost
- Superior to previous Opus models for most tasks
- Excellent at following complex assembly line constraints
- Best pattern matching for new dialogue pause, light, and finger action rules

## LLM Optimization

### Model Selection Guide (October 2025)

**Current LLM Landscape:**

The ClaudeHumanizer system supports multiple leading LLMs, each with distinct strengths:

| Model | Best For | Pricing (per 1M tokens) | Key Advantage |
|-------|----------|------------------------|---------------|
| **Claude Sonnet 4.5** ⭐ | Maximum quality, reliable boundaries | $3 in / $15 out | "Surgical" edits, natural human tone, best instruction-following |
| **Gemini 2.5 Pro** 💰 | Budget-conscious, long texts | $1.25-2.50 in / $10-15 out | 40% cheaper, 1M context, fastest (372 tok/s) |
| **GPT-5** 🔄 | ChatGPT Plus users | Subscription-based | Literary style, widely available |

**Decision Tree:**

```
Is budget the primary concern?
  ├─ Yes + Text >100K words? → Gemini 2.5 Pro (1M context advantage)
  ├─ Yes + Text <100K words? → Gemini 2.5 Pro or Hybrid Strategy
  └─ No (quality priority)? → Claude Sonnet 4.5 ⭐ RECOMMENDED

Already have ChatGPT Plus/Pro?
  ├─ Yes → Consider GPT-5 (with stricter prompting)
  └─ No → Claude Sonnet 4.5 or Gemini 2.5 Pro

Processing book-length content (>200K words)?
  └─ → Gemini 2.5 Pro (1M context window)
```

**Why Claude Sonnet 4.5 Remains Our Top Recommendation:**
- **"Surgical" approach**: Makes minimal, precise changes respecting domain boundaries
- **Most aligned frontier model**: Best at following complex multi-constraint prompts
- **Natural human tone**: Users report it "writes like a human" better than alternatives
- **Superior agent capabilities**: Ideal for sequential 10-phase processing
- **Proven pattern recognition**: Reliably applies dialogue pause, light, and finger action rules

### Optimal Model Selection by Phase

**Note:** The 10-phase system now includes a final AI word sweep (Phase 10) to catch any prohibited words reintroduced during phases 3-9.

#### Phase 1: Grammar Foundation
- **Best Model**: Claude Sonnet 4.5
- **Temperature**: 0.1-0.2
- **Memory**: Low (focused grammar rules)
- **Reasoning**: Requires precision and consistency while preserving voice

#### Phase 2: AI Word Cleaning
- **Best Model**: Claude Sonnet 4.5
- **Temperature**: 0.3-0.4
- **Memory**: Medium (master list + pattern rules for dialogue pauses, light descriptions, finger actions)
- **Reasoning**: Excellent pattern recognition for new pattern-based rules
- **Pattern Rules Applied**: dialogue_pause_pattern_rules, light_description_pattern_rules, finger_hand_action_pattern_rules

#### Phase 3: Overwritten Language Reduction
- **Best Model**: Claude Sonnet 4.5
- **Temperature**: 0.2-0.3
- **Memory**: Medium (context to distinguish purple prose from purposeful ornate language)
- **Reasoning**: Superior literary judgment and nuanced understanding

#### Phase 4: Sensory Enhancement
- **Best Model**: Claude Sonnet 4.5
- **Temperature**: 0.6-0.7
- **Memory**: High (full scene context for appropriate sensory additions)
- **Reasoning**: Creative capability for vivid, original descriptions while avoiding AI patterns

#### Phase 5: Subtlety Creation
- **Best Model**: Claude Sonnet 4.5
- **Temperature**: 0.4-0.5
- **Memory**: High (character/story context for appropriate implications)
- **Reasoning**: Superior subtext creation and show-don't-tell understanding

#### Phase 6: Dialogue Enhancement
- **Best Model**: Claude Sonnet 4.5
- **Temperature**: 1.0
- **Memory**: High (character backgrounds and voice consistency tracking)
- **Reasoning**: Higher temperature produces more natural, varied character voices
- **Note**: Increased temperature from 0.7-0.8 to 1.0 for maximum dialogue authenticity

#### Phase 7: Weak Language Cleanup
- **Best Model**: Claude Sonnet 4.5
- **Temperature**: 0.1-0.3
- **Memory**: Medium (12 weak language pattern categories embedded in prompt)
- **Reasoning**: Systematic pattern detection with literary awareness
- **Note**: Now includes overused_transitions and robotic_qualifiers

#### Phase 8: Strategic Imperfections & Error Injection
- **Best Model**: Claude Sonnet 4.5
- **Temperature**: 0.8-0.9
- **Memory**: High (understanding of full text flow and rhythm)
- **Reasoning**: Best understanding of authentic human writing patterns and imperfections
- **New Features**: Punctuation inconsistency injection, enhanced imperfections, optional homophone error injection (user-configurable)
- **Note**: Higher temperature supports natural variation in imperfection placement

#### Phase 9: AI Pattern Detection (REFACTORED)
- **Best Model**: Claude Sonnet 4.5
- **Temperature**: 0.2-0.3
- **Memory**: Medium (AI pattern detection, N-gram corpus, perplexity patterns)
- **Reasoning**: QUALITATIVE pattern replacement only - N-grams and formulaic phrases
- **Architecture Change**: Statistical metrics (POS, TTR, burstiness) moved to Phase 9.5
- **Focus**: Pattern-based detection and replacement, not quantitative analysis

#### Phase 9.5: Statistical Analysis Hub (NEW OPTIONAL)
- **Best Model**: Claude Sonnet 4.5
- **Temperature**: 0.3-0.4
- **Memory**: High (comprehensive statistical analysis requires full text context)
- **Reasoning**: QUANTITATIVE metrics require precision for accurate calculations
- **Consolidates**: Burstiness (CV, range, variance), POS distribution (noun/verb/adj ratios), Lexical diversity (TTR, word frequency)
- **Critical**: Slightly higher temp (0.3-0.4) allows natural optimization while maintaining analytical precision
- **Single-Pass Efficiency**: Reads text once, calculates all metrics, makes coordinated optimizations
- **Optional**: Skip if text already has good statistical properties or for budget processing
- **Metrics Report**: Can generate detailed before/after statistical analysis on request

#### Phase 10: Final Word Filtering (SIMPLIFIED)
- **Best Model**: Claude Sonnet 4.5
- **Temperature**: 0.2-0.3
- **Memory**: Low (surgical word replacement only)
- **Reasoning**: Pure word filtering - no statistical analysis
- **Pattern Rules Applied**: All pattern rules from master_prohibited_words.json
- **Architecture Change**: Lexical diversity analysis moved to Phase 9.5
- **Critical Role**: Final quality control for prohibited words only

### Pricing Comparison (October 2025)

| Model | Input Cost | Output Cost | Est. 10K Word Processing | Notes |
|-------|-----------|-------------|--------------------------|-------|
| Claude Sonnet 4.5 | $3/1M | $15/1M | $0.50-2.00 | Premium quality, best reliability |
| Gemini 2.5 Pro (≤200K) | $1.25/1M | $10/1M | $0.30-1.30 | Budget tier, excellent for most content |
| Gemini 2.5 Pro (>200K) | $2.50/1M | $15/1M | $0.50-1.80 | Book-length content with 1M context |
| GPT-5 | Subscription | Subscription | Included | ChatGPT Plus/Pro users |
| Claude Haiku 3.5 | $0.25/1M | $1.25/1M | $0.05-0.25 | Ultra-budget option |

**Cost Savings Analysis:**
- Gemini 2.5 Pro vs Claude Sonnet 4.5: ~40% savings (short contexts)
- Hybrid strategy (Gemini + Claude): ~25-40% savings
- Full Haiku pipeline: ~85% savings (significant quality reduction)

### Model Family Strategies

#### Single-Family Approaches

**Premium Tier - Anthropic-Only Pipeline (RECOMMENDED)**:
```yaml
models: Claude Sonnet 4.5 (all 10 phases + optional Phase 9.5)
temperatures: 0.1-0.2 (phases 1,7,9), 0.3-0.5 (phases 2,3,5,9.5,10), 0.6-0.9 (phases 4,8), 1.0 (phase 6)
quality: 95-98% of maximum potential (with Phase 9.5), 93-96% (without Phase 9.5)
cost: Medium-High (~10-15% higher with Phase 9.5 included)
best_for: Optimal humanization with consistent quality across all text types
consistency: Superior assembly line constraint adherence
pattern_recognition: Best for new pattern-based rules
flexibility: Phase 9.5 can be skipped for budget savings with minimal quality impact
```

**Budget Tier - Google-Only Pipeline (NEW for 2025)**:
```yaml
models: Gemini 2.5 Pro (all 10 phases + optional Phase 9.5)
temperatures: Same as Claude configuration (0.1-1.0 by phase)
quality: 85-92% of maximum potential (estimated)
cost: ~40% less than Claude Sonnet 4.5
best_for: Budget-conscious users, long texts (1M context), speed priority
advantages:
  - 1M token context window (vs Claude's 200K)
  - Fastest processing (372 tokens/second)
  - Significantly lower cost
  - Excellent for book-length content (>200K words)
limitations:
  - Less proven for literary judgment
  - May require more iteration for optimal results
  - Instruction-following may be less precise than Claude
```

**Alternative - OpenAI Pipeline (GPT-5)**:
```yaml
models: GPT-5 (all 10 phases + optional Phase 9.5)
temperatures: Same as Claude configuration
quality: 80-90% of maximum potential
cost: Subscription-based (ChatGPT Plus/Pro)
best_for: Users already on ChatGPT subscription
advantages:
  - Excellent literary style and creative flair
  - Good at style mimicry
  - 45% less hallucination than GPT-4o
  - Widely available
limitations:
  - "Takes over" narrative - tries to rewrite beyond instructions ⚠️
  - Aggressive refactoring - less "surgical" than Claude ⚠️
  - May violate domain boundaries without stricter prompting ⚠️
  - Requires enhanced "never touch" constraints in prompts
WARNING: GPT-5 tends to make larger, more aggressive changes. For ClaudeHumanizer's
domain-isolated architecture, this can cause phases to interfere with each other.
Use only if willing to accept potential boundary violations.
```

#### Hybrid Strategies (Cost Optimization)

**Cost-Optimized Hybrid:**
```yaml
phases_1-3: Gemini 2.5 Pro @ standard temps (systematic cleanup)
phases_4-6: Claude Sonnet 4.5 @ standard temps (creative/literary - where quality matters most)
phases_7-10: Gemini 2.5 Pro @ standard temps (systematic cleanup)
optional_9_5: Gemini 2.5 Pro @ 0.4 (statistical analysis)

quality: 90-94% of maximum potential
cost_savings: ~40% vs full Claude Sonnet 4.5 pipeline
best_for: Balance of quality and cost
rationale: Use premium Claude only where literary judgment is critical (Phases 4-6)
```

**Quality-Optimized Hybrid:**
```yaml
phases_1-2: Gemini 2.5 Pro @ standard temps (systematic phases)
phases_3-6: Claude Sonnet 4.5 @ standard temps (literary/creative phases)
phase_7: Gemini 2.5 Pro @ 0.2 (systematic patterns)
phase_8: Claude Sonnet 4.5 @ 0.9 (rhythm variation - critical)
phase_9: Gemini 2.5 Pro @ 0.2 (pattern detection)
optional_9_5: Gemini 2.5 Pro @ 0.4 (statistical analysis)
phase_10: Gemini 2.5 Pro @ 0.3 (final cleanup)

quality: 93-96% of maximum potential
cost_savings: ~25% vs full Claude Sonnet 4.5 pipeline
best_for: Near-premium quality with moderate cost savings
rationale: Use Claude for all creative/literary work, Gemini for systematic processing
```

**Ultra-Budget Hybrid:**
```yaml
phases_1-2: Claude Haiku 3.5 @ standard temps
phases_3-6: Gemini 2.5 Pro @ standard temps
phases_7-10: Claude Haiku 3.5 @ standard temps
optional_9_5: SKIP (cost savings)

quality: 80-85% of maximum potential
cost_savings: ~70% vs full Claude Sonnet 4.5 pipeline
best_for: Maximum cost reduction, high-volume processing
trade-offs: Lower quality, may need manual review
```

#### Configuration Details

**Premium Configuration - Claude Sonnet 4.5 (RECOMMENDED)**
```yaml
phase_1: Claude Sonnet 4.5 @ 0.2
phase_2: Claude Sonnet 4.5 @ 0.4
phase_3: Claude Sonnet 4.5 @ 0.3
phase_4: Claude Sonnet 4.5 @ 0.7
phase_5: Claude Sonnet 4.5 @ 0.5
phase_6: Claude Sonnet 4.5 @ 1.0  # Increased for dialogue naturalness
phase_7: Claude Sonnet 4.5 @ 0.2
phase_8: Claude Sonnet 4.5 @ 0.9
phase_9: Claude Sonnet 4.5 @ 0.2
phase_9_5: Claude Sonnet 4.5 @ 0.4  # OPTIONAL: Statistical analysis hub
phase_10: Claude Sonnet 4.5 @ 0.3  # Final word sweep

quality: 95-98% of maximum potential (with Phase 9.5), 93-96% (without Phase 9.5)
cost: Medium-High (~$0.50-2.00 per 10k words without Phase 9.5, ~$0.60-2.30 with Phase 9.5)
consistency: Excellent - single model understands full assembly line context
advantages:
  - Superior pattern recognition (dialogue pauses, light descriptions, finger actions)
  - Best literary judgment and nuance
  - Excellent instruction following across all phases
  - No model switching overhead
  - Phase 9.5 optional for budget flexibility
```

**Budget Configuration - Gemini 2.5 Pro (NEW for 2025)**
```yaml
phase_1: Gemini 2.5 Pro @ 0.2
phase_2: Gemini 2.5 Pro @ 0.4
phase_3: Gemini 2.5 Pro @ 0.3
phase_4: Gemini 2.5 Pro @ 0.7
phase_5: Gemini 2.5 Pro @ 0.5
phase_6: Gemini 2.5 Pro @ 1.0  # Dialogue naturalness
phase_7: Gemini 2.5 Pro @ 0.2
phase_8: Gemini 2.5 Pro @ 0.9
phase_9: Gemini 2.5 Pro @ 0.2
phase_9_5: Gemini 2.5 Pro @ 0.4  # OPTIONAL
phase_10: Gemini 2.5 Pro @ 0.3

quality: 85-92% of maximum potential (estimated)
cost: $0.30-1.50 per 10K words (≤200K context), $0.50-1.80 (>200K context)
savings: ~40% vs Claude Sonnet 4.5
special_advantages:
  - 1M token context window (perfect for books >200K words)
  - Fastest processing (372 tokens/second)
  - Excellent for batch processing large volumes
  - Top-ranked on LM Arena (general performance)
best_for: Budget-conscious users, long-form content, speed priority
```

**Budget Configuration - Claude Haiku/Sonnet Mix**
```yaml
phase_1: Claude Sonnet 4.5 @ 0.2
phase_2: Claude Sonnet 4.5 @ 0.4
phase_3: Claude Haiku 3.5 @ 0.3
phase_4: Claude Sonnet 4.5 @ 0.7
phase_5: Claude Haiku 3.5 @ 0.5
phase_6: Claude Sonnet 4.5 @ 1.0
phase_7: Claude Haiku 3.5 @ 0.2
phase_8: Claude Sonnet 4.5 @ 0.9
phase_9: Claude Haiku 3.5 @ 0.2
phase_9_5: SKIP  # Optional - skip for budget processing
phase_10: Claude Sonnet 4.5 @ 0.3

quality: 85-90% of maximum potential
cost_savings: 50-60% vs full Sonnet 4.5 pipeline
strategy: Use Sonnet 4.5 for critical creative/pattern phases (2,4,6,8,10), Haiku for systematic phases
note: Stays within Anthropic ecosystem for consistency
```

## Automation Integration

### n8n Workflow Implementation (RECOMMENDED)

**Two workflow options available:**

1. **Single Text Processing** (`examples/n8n_workflow_sample.json`)
   - Process one text through all 10 phases
   - Best for: Single documents, articles, short stories
   - Simple linear flow

2. **Chapter Loop Processing** (`examples/n8n_chapter_loop_workflow.json`) ⭐ **NEW**
   - Process entire books chapter-by-chapter
   - Automatic looping through chapter array
   - Best for: Novels, book-length manuscripts
   - Returns all chapters when complete
   - **See**: `examples/N8N_CHAPTER_LOOP_GUIDE.md` for complete documentation

### n8n Chapter Loop Workflow (Book Processing)

**Workflow file**: `examples/n8n_chapter_loop_workflow.json`
**Complete guide**: `examples/N8N_CHAPTER_LOOP_GUIDE.md`

This workflow processes entire books by looping through chapters sequentially, processing each through all 10 phases automatically.

#### Quick Start - Chapter Loop

**1. Input Format:**
```json
{
  "chapters": [
    {
      "number": 1,
      "title": "Chapter One: The Beginning",
      "text": "Your AI-generated chapter text..."
    },
    {
      "number": 2,
      "title": "Chapter Two: The Journey",
      "text": "Your AI-generated chapter text..."
    }
  ],
  "include_phase_9_5": false
}
```

**2. Send Request:**
```bash
curl -X POST https://your-n8n-instance.com/webhook/claudehumanizer-chapters \
  -H "Content-Type: application/json" \
  -d @chapters.json
```

**3. Receive Results:**
```json
{
  "status": "completed",
  "total_chapters": 2,
  "processed_chapters": [
    {
      "number": 1,
      "title": "Chapter One: The Beginning",
      "original_text": "Original AI text...",
      "humanized_text": "Humanized text after 10 phases...",
      "processed_at": "2025-10-26T14:30:00.000Z"
    },
    {
      "number": 2,
      "title": "Chapter Two: The Journey",
      "original_text": "Original AI text...",
      "humanized_text": "Humanized text after 10 phases...",
      "processed_at": "2025-10-26T14:35:00.000Z"
    }
  ],
  "completed_at": "2025-10-26T14:35:00.000Z"
}
```

**Key Features:**
- ✅ Automatic looping through all chapters
- ✅ Sequential processing (one chapter at a time)
- ✅ Progress tracking (current/total)
- ✅ Preserves original + humanized text
- ✅ Optional Phase 9.5 (statistical analysis)
- ✅ Claude Sonnet 4.5 for all phases
- ✅ Correct temperature settings per phase

**Performance:**
- ~3-4 minutes per chapter (without Phase 9.5)
- ~$1.00-1.20 per chapter (Claude Sonnet 4.5)
- Processes chapters sequentially (not parallel)
- Example: 20-chapter book = ~60-80 minutes, ~$20-25

**See full documentation**: `examples/N8N_CHAPTER_LOOP_GUIDE.md`

---

### n8n Single Text Workflow (Original)

**Complete workflow available:** See `examples/n8n_workflow_sample.json` for a ready-to-import workflow.

#### Quick Start Guide

1. **Import the Workflow**
   ```bash
   # In n8n, go to Workflows → Import from File
   # Select: docs/n8n_workflow_sample.json
   ```

2. **Configure File Paths**
   - Update all "Load Phase X Prompt" nodes with your ClaudeHumanizer directory path
   - Example: `/home/user/ClaudeHumanizer/1_grammar_foundation.json`

3. **Set Up Anthropic API Credentials**
   ```
   Settings → Credentials → New Credential → Anthropic API
   Add your API key from: https://console.anthropic.com/
   ```

4. **Activate and Test**
   ```bash
   # Activate the workflow
   # Send test request:
   curl -X POST https://your-n8n-instance.com/webhook/humanize-text \
     -H "Content-Type: application/json" \
     -d '{"text": "Your AI-generated text here..."}'
   ```

#### Architecture Overview

The workflow consists of:
- **1 Webhook Trigger** (POST endpoint)
- **11-12 File Loaders** (master list + 10 phase prompts + optional Phase 9.5)
- **10-11 Anthropic Claude Nodes** (one per phase, Phase 9.5 optional)
- **1 Webhook Response** (returns humanized text)

**Sequential Flow:**
```
Webhook Input
  ↓
Load Master Prohibited Words + Phase Prompts
  ↓
Phase 1 (temp 0.2) → Phase 2 (temp 0.4, + master list)
  ↓
Phase 3 (temp 0.3) → Phase 4 (temp 0.7)
  ↓
Phase 5 (temp 0.5) → Phase 6 (temp 1.0)
  ↓
Phase 7 (temp 0.2) → Phase 8 (temp 0.9)
  ↓
Phase 9 (temp 0.2) → Phase 9.5 (OPTIONAL, temp 0.4) → Phase 10 (temp 0.3, + master list)
  ↓
Webhook Response (JSON with humanized text)
```

**Note on Phase 9.5:**
Phase 9.5 is optional and can be skipped if:
- Text already has good statistical properties (varied sentence length, balanced POS distribution, adequate lexical diversity)
- Budget constraints require reducing processing costs
- Fast turnaround is more important than maximum optimization

If Phase 9.5 is skipped, Phase 9 output feeds directly to Phase 10.

#### Key Configuration Details

**Phase 2 & 10 (Master List Integration):**
```javascript
// System message for Phase 2 and Phase 10
systemMessage: `={{
  JSON.parse($node['Load Master Prohibited Words'].json.data).toString() +
  '\n\n' +
  JSON.parse($node['Load Phase 2 Prompt'].json.data).prompt
}}`
```

**All Other Phases (No Master List):**
```javascript
// System message for Phases 1, 3-9
systemMessage: `={{
  JSON.parse($node['Load Phase X Prompt'].json.data).prompt
}}`
```

**Text Chaining Between Phases:**
```javascript
// First phase uses webhook input
text: "={{ $json.body.text }}"

// All subsequent phases use previous phase output
text: "={{ $json.content[0].text }}"
```

#### Complete Node Configuration Example

```json
{
  "parameters": {
    "authentication": "predefinedCredentialType",
    "nodeCredentialType": "anthropicApi",
    "resource": "message",
    "model": "claude-sonnet-4-5-20250929",  // Current recommended Claude Sonnet 4.5 model
    "text": "={{ $json.content[0].text }}",
    "options": {
      "temperature": 0.4,
      "systemMessage": "={{ JSON.parse($node['Load Master Prohibited Words'].json.data).toString() + '\\n\\n' + JSON.parse($node['Load Phase 2 Prompt'].json.data).prompt }}",
      "maxTokens": 8192
    }
  },
  "name": "Phase 2 - AI Word Cleaning",
  "type": "n8n-nodes-base.anthropic",
  "typeVersion": 1,
  "position": [850, 400],
  "credentials": {
    "anthropicApi": {
      "id": "1",
      "name": "Anthropic API"
    }
  }
}
```

#### Response Format

```json
{
  "success": true,
  "original_text": "The system leverages cutting-edge...",
  "humanized_text": "The system uses modern...",
  "phases_completed": 10,
  "timestamp": "2025-10-07T10:30:00.000Z"
}
```

#### Multi-Model Node Configuration (For Reference - Claude Sonnet 4.5 Recommended for All Phases)
```json
{
  "phase1": {
    "node": "Anthropic Claude",
    "model": "claude-sonnet-4-5-20250929",
    "temperature": 0.2,
    "systemPrompt": "{{ $env.GRAMMAR_PROMPT }}"
  },
  "phase2": {
    "node": "Anthropic Claude",
    "model": "claude-sonnet-4-5-20250929",
    "temperature": 0.4,
    "systemPrompt": "{{ $env.MASTER_PROHIBITED_WORDS }}\\n\\n{{ $env.AI_CLEANING_PROMPT }}"
  },
  "phase3": {
    "node": "Anthropic Claude",
    "model": "claude-sonnet-4-5-20250929",
    "temperature": 0.3,
    "systemPrompt": "{{ $env.PURPLE_PROSE_PROMPT }}"
  }
}
```

**Note:** While the system can use different LLM providers, Claude Sonnet 4.5 is strongly recommended for all phases for optimal results.

#### Error Handling and Retry Logic
```javascript
{
  "continueOnFail": true,
  "retryOnFail": true,
  "maxTries": 3,
  "waitBetweenTries": 2000
}
```

#### Quality Validation Node
```javascript
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

### Make.com Implementation

#### Scenario Blueprint
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
          "model": "claude-sonnet-4-5-20250929",
          "temperature": 0.2,
          "system": "{{ phase1Prompt }}",
          "message": "{{ 2.inputText }}"
        }
      }
    ]
  }
}
```

#### Advanced Routing for Multi-Model Pipeline
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
      }
    ]
  }
}
```

#### Dynamic Model Selection Function (October 2025)
```javascript
function selectModel(phase, strategy = "premium") {
  // Strategy options: "premium", "budget", "hybrid_cost", "hybrid_quality"

  const strategies = {
    premium: {
      // Claude Sonnet 4.5 - Best quality, most reliable
      1: { provider: "anthropic", model: "claude-sonnet-4-5-20250929", temp: 0.2 },
      2: { provider: "anthropic", model: "claude-sonnet-4-5-20250929", temp: 0.4 },
      3: { provider: "anthropic", model: "claude-sonnet-4-5-20250929", temp: 0.3 },
      4: { provider: "anthropic", model: "claude-sonnet-4-5-20250929", temp: 0.7 },
      5: { provider: "anthropic", model: "claude-sonnet-4-5-20250929", temp: 0.5 },
      6: { provider: "anthropic", model: "claude-sonnet-4-5-20250929", temp: 1.0 },
      7: { provider: "anthropic", model: "claude-sonnet-4-5-20250929", temp: 0.2 },
      8: { provider: "anthropic", model: "claude-sonnet-4-5-20250929", temp: 0.9 },
      9: { provider: "anthropic", model: "claude-sonnet-4-5-20250929", temp: 0.2 },
      9.5: { provider: "anthropic", model: "claude-sonnet-4-5-20250929", temp: 0.4 },
      10: { provider: "anthropic", model: "claude-sonnet-4-5-20250929", temp: 0.3 }
    },

    budget: {
      // Gemini 2.5 Pro - 40% cheaper, 1M context, fastest
      1: { provider: "google", model: "gemini-2.5-pro", temp: 0.2 },
      2: { provider: "google", model: "gemini-2.5-pro", temp: 0.4 },
      3: { provider: "google", model: "gemini-2.5-pro", temp: 0.3 },
      4: { provider: "google", model: "gemini-2.5-pro", temp: 0.7 },
      5: { provider: "google", model: "gemini-2.5-pro", temp: 0.5 },
      6: { provider: "google", model: "gemini-2.5-pro", temp: 1.0 },
      7: { provider: "google", model: "gemini-2.5-pro", temp: 0.2 },
      8: { provider: "google", model: "gemini-2.5-pro", temp: 0.9 },
      9: { provider: "google", model: "gemini-2.5-pro", temp: 0.2 },
      9.5: { provider: "google", model: "gemini-2.5-pro", temp: 0.4 },
      10: { provider: "google", model: "gemini-2.5-pro", temp: 0.3 }
    },

    hybrid_cost: {
      // Cost-optimized hybrid: Gemini for systematic, Claude for creative
      1: { provider: "google", model: "gemini-2.5-pro", temp: 0.2 },
      2: { provider: "google", model: "gemini-2.5-pro", temp: 0.4 },
      3: { provider: "google", model: "gemini-2.5-pro", temp: 0.3 },
      4: { provider: "anthropic", model: "claude-sonnet-4-5-20250929", temp: 0.7 },  // Creative
      5: { provider: "anthropic", model: "claude-sonnet-4-5-20250929", temp: 0.5 },  // Creative
      6: { provider: "anthropic", model: "claude-sonnet-4-5-20250929", temp: 1.0 },  // Creative
      7: { provider: "google", model: "gemini-2.5-pro", temp: 0.2 },
      8: { provider: "google", model: "gemini-2.5-pro", temp: 0.9 },
      9: { provider: "google", model: "gemini-2.5-pro", temp: 0.2 },
      9.5: { provider: "google", model: "gemini-2.5-pro", temp: 0.4 },
      10: { provider: "google", model: "gemini-2.5-pro", temp: 0.3 }
    },

    hybrid_quality: {
      // Quality-optimized hybrid: Claude for literary, Gemini for systematic
      1: { provider: "google", model: "gemini-2.5-pro", temp: 0.2 },
      2: { provider: "google", model: "gemini-2.5-pro", temp: 0.4 },
      3: { provider: "anthropic", model: "claude-sonnet-4-5-20250929", temp: 0.3 },  // Literary
      4: { provider: "anthropic", model: "claude-sonnet-4-5-20250929", temp: 0.7 },  // Literary
      5: { provider: "anthropic", model: "claude-sonnet-4-5-20250929", temp: 0.5 },  // Literary
      6: { provider: "anthropic", model: "claude-sonnet-4-5-20250929", temp: 1.0 },  // Literary
      7: { provider: "google", model: "gemini-2.5-pro", temp: 0.2 },
      8: { provider: "anthropic", model: "claude-sonnet-4-5-20250929", temp: 0.9 },  // Rhythm critical
      9: { provider: "google", model: "gemini-2.5-pro", temp: 0.2 },
      9.5: { provider: "google", model: "gemini-2.5-pro", temp: 0.4 },
      10: { provider: "google", model: "gemini-2.5-pro", temp: 0.3 }
    }
  };

  return strategies[strategy][phase];
}

// Usage example:
// const config = selectModel(6, "premium");  // Returns Claude Sonnet 4.5 @ temp 1.0
// const config = selectModel(6, "budget");   // Returns Gemini 2.5 Pro @ temp 1.0
```

## API Configurations

### Anthropic Claude API
```python
import anthropic

client = anthropic.Anthropic(api_key="your-api-key")

def process_phase_anthropic(text, prompt, model="claude-sonnet-4-5-20250929", temperature=0.2):
    response = client.messages.create(
        model=model,
        max_tokens=4096,
        temperature=temperature,
        system=prompt,
        messages=[{"role": "user", "content": text}]
    )
    return response.content[0].text
```

### OpenAI GPT API (GPT-5 - August 2025)
```python
import openai

client = openai.OpenAI(api_key="your-api-key")

def process_phase_openai(text, prompt, model="gpt-5", temperature=0.4):
    """
    Process text through GPT-5.

    Args:
        text: Input text to process
        prompt: Phase-specific system prompt
        model: Model identifier (default: gpt-5)
        temperature: Sampling temperature

    Returns:
        Processed text from the model

    Note: GPT-5 released August 2025. Now default model in ChatGPT.
          Available variants: gpt-5, gpt-5-mini, gpt-5-nano
    """
    response = client.chat.completions.create(
        model=model,
        temperature=temperature,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": text}
        ],
        max_tokens=16384  # GPT-5 supports longer outputs
    )
    return response.choices[0].message.content

# WARNING for ClaudeHumanizer:
# GPT-5 tends to make aggressive changes and may violate domain boundaries.
# Consider adding stricter "never touch" constraints to prompts when using GPT-5.
# For best results with domain isolation, use Claude Sonnet 4.5 or Gemini 2.5 Pro.
```

### Google Gemini API (Gemini 2.5 Pro - October 2025)
```python
import google.generativeai as genai

genai.configure(api_key="your-api-key")

def process_phase_gemini(text, prompt, model="gemini-2.5-pro", temperature=0.2):
    """
    Process text through Gemini 2.5 Pro.

    Args:
        text: Input text to process
        prompt: Phase-specific system prompt
        model: Model identifier (default: gemini-2.5-pro)
        temperature: Sampling temperature

    Returns:
        Processed text from the model
    """
    model_instance = genai.GenerativeModel(
        model_name=model,
        system_instruction=prompt  # System instruction for better prompt adherence
    )

    response = model_instance.generate_content(
        text,
        generation_config=genai.types.GenerationConfig(
            temperature=temperature,
            max_output_tokens=8192,  # Increased for long outputs
            candidate_count=1
        )
    )
    return response.text

# Note: Gemini 2.5 Pro supports up to 1M token context window
# Pricing: $1.25/1M input (≤200K), $2.50/1M input (>200K), $10-15/1M output
```

### Complete Pipeline Implementation
```python
class ClaudeHumanizerPipeline:
    def __init__(self, config, include_phase_9_5=False):
        self.config = config
        self.include_phase_9_5 = include_phase_9_5
        self.load_prompts()
        self.load_master_prohibited_words()

    def load_prompts(self):
        self.prompts = {}
        # Load main phases 1-10
        for i in range(1, 11):
            with open(f"{i}_*.json", "r") as f:
                self.prompts[i] = json.load(f)

        # Load optional Phase 9.5 if requested
        if self.include_phase_9_5:
            with open("9.5_statistical_analysis_hub.json", "r") as f:
                self.prompts[9.5] = json.load(f)

    def load_master_prohibited_words(self):
        with open("master_prohibited_words.json", "r") as f:
            self.master_prohibited = json.load(f)

    def process_text(self, text, enable_9_5_metrics_report=False):
        current_text = text

        # Build phase sequence
        phases = list(range(1, 10))  # Phases 1-9
        if self.include_phase_9_5:
            phases.append(9.5)  # Optional Phase 9.5
        phases.append(10)  # Phase 10 always last

        for phase in phases:
            print(f"Processing Phase {phase}...")

            # Prepare prompt
            prompt = self.prompts[phase]["content"]
            # ONLY Phases 2 and 10 require master list with pattern rules
            if phase in [2, 10]:
                prompt = f"{self.master_prohibited}\\n\\n{prompt}"

            # Phase 9.5 can optionally include metrics report request
            if phase == 9.5 and enable_9_5_metrics_report:
                prompt += "\\n\\nPlease include detailed statistical metrics report."

            # Select model and settings
            model_config = self.config["phases"][phase]

            # Process with appropriate API
            if model_config["provider"] == "anthropic":
                current_text = process_phase_anthropic(
                    current_text, prompt,
                    model_config["model"],
                    model_config["temperature"]
                )
            elif model_config["provider"] == "openai":
                current_text = process_phase_openai(
                    current_text, prompt,
                    model_config["model"],
                    model_config["temperature"]
                )
            elif model_config["provider"] == "google":
                current_text = process_phase_gemini(
                    current_text, prompt,
                    model_config["model"],
                    model_config["temperature"]
                )

            # Quality validation
            if self.validate_phase_output(current_text, phase):
                print(f"Phase {phase} completed successfully")
            else:
                raise Exception(f"Phase {phase} failed validation")

        return current_text

    def validate_phase_output(self, text, phase):
        # Check for prohibited words in Phase 2 and Phase 10 (final sweep)
        if phase in [2, 10]:
            prohibited_found = any(
                word.lower() in text.lower()
                for word in self.master_prohibited.get("prohibited_single_words", [])
            )
            if prohibited_found:
                return False
        return True
```

**Usage Examples:**

```python
# Standard processing (without Phase 9.5)
pipeline = ClaudeHumanizerPipeline(config, include_phase_9_5=False)
result = pipeline.process_text(input_text)

# Full processing with statistical optimization
pipeline_with_stats = ClaudeHumanizerPipeline(config, include_phase_9_5=True)
result = pipeline_with_stats.process_text(input_text)

# Full processing with detailed metrics report
result_with_report = pipeline_with_stats.process_text(
    input_text,
    enable_9_5_metrics_report=True
)
```

## Performance Optimization

### Rate Limiting and Queue Management
```javascript
// Rate limiting configuration
{
  "rateLimiting": {
    "anthropic": {
      "requests_per_minute": 50,
      "tokens_per_minute": 40000
    },
    "openai": {
      "requests_per_minute": 60,
      "tokens_per_minute": 90000
    },
    "google": {
      "requests_per_minute": 60,
      "tokens_per_minute": 30000
    }
  }
}

// Queue management
{
  "queueConfig": {
    "maxConcurrent": 3,
    "retryDelay": 2000,
    "maxRetries": 3
  }
}
```

### Batch Processing
```python
class BatchProcessor:
    def __init__(self, pipeline, batch_size=5):
        self.pipeline = pipeline
        self.batch_size = batch_size

    def process_batch(self, texts):
        results = []
        for i in range(0, len(texts), self.batch_size):
            batch = texts[i:i + self.batch_size]
            batch_results = []

            for text in batch:
                try:
                    result = self.pipeline.process_text(text)
                    batch_results.append(result)
                except Exception as e:
                    print(f"Error processing text: {e}")
                    batch_results.append(None)

            results.extend(batch_results)
            time.sleep(1)  # Rate limiting

        return results
```

## Cost Management

### Cost Tracking
```python
class CostTracker:
    def __init__(self):
        self.costs = {
            "anthropic": {"input": 0.003, "output": 0.015},  # per 1K tokens
            "openai": {"input": 0.005, "output": 0.015},
            "google": {"input": 0.00125, "output": 0.005}
        }
        self.usage = []

    def estimate_cost(self, text, model_config):
        tokens = self.estimate_tokens(text)
        provider = model_config["provider"]

        input_cost = tokens * self.costs[provider]["input"] / 1000
        output_cost = tokens * self.costs[provider]["output"] / 1000

        return input_cost + output_cost

    def track_usage(self, phase, text, model_config, cost):
        self.usage.append({
            "phase": phase,
            "provider": model_config["provider"],
            "model": model_config["model"],
            "tokens": self.estimate_tokens(text),
            "cost": cost,
            "timestamp": datetime.now()
        })

    def get_daily_cost(self):
        today = datetime.now().date()
        daily_usage = [u for u in self.usage if u["timestamp"].date() == today]
        return sum(u["cost"] for u in daily_usage)
```

### Budget Management
```python
class BudgetManager:
    def __init__(self, daily_limit=50.0):
        self.daily_limit = daily_limit
        self.cost_tracker = CostTracker()

    def check_budget(self, estimated_cost):
        current_daily = self.cost_tracker.get_daily_cost()
        if current_daily + estimated_cost > self.daily_limit:
            raise Exception(f"Budget exceeded: ${current_daily + estimated_cost:.2f} > ${self.daily_limit}")
        return True

    def select_cost_effective_model(self, phase, budget_remaining):
        if budget_remaining > 5.0:
            return "premium"  # Use optimal models
        elif budget_remaining > 2.0:
            return "balanced"  # Use cost-effective models
        else:
            return "budget"  # Use cheapest models

    def should_include_phase_9_5(self, budget_remaining, text_length):
        """
        Determine if Phase 9.5 should be included based on budget constraints.

        Phase 9.5 is optional and can be skipped for budget savings with minimal
        quality impact if the text already has good statistical properties.

        Args:
            budget_remaining: Remaining daily budget in dollars
            text_length: Length of text in words

        Returns:
            bool: True if Phase 9.5 should be included, False to skip
        """
        # Estimate cost for Phase 9.5 (roughly 10-15% of total pipeline cost)
        estimated_9_5_cost = (text_length / 1000) * 0.15  # ~$0.15 per 1K words

        # Skip Phase 9.5 if budget is tight
        if budget_remaining < estimated_9_5_cost * 2:
            print("Skipping Phase 9.5 for budget conservation")
            return False

        return True
```

## Quality Metrics

### Automated Quality Assessment
```python
class QualityAssessor:
    def __init__(self):
        self.ai_detectors = [
            "gptzero", "originality_ai", "copyleaks", "writer_ai"
        ]

    def assess_quality(self, original_text, processed_text):
        metrics = {
            "ai_detection_scores": self.run_ai_detection(processed_text),
            "readability_improvement": self.measure_readability(original_text, processed_text),
            "character_voice_consistency": self.check_character_voices(processed_text),
            "prohibited_words_removed": self.check_prohibited_words(processed_text),
            "meaning_preservation": self.measure_semantic_similarity(original_text, processed_text)
        }
        return metrics

    def run_ai_detection(self, text):
        scores = {}
        for detector in self.ai_detectors:
            # Implementation depends on specific API
            scores[detector] = self.call_detector_api(detector, text)
        return scores

    def measure_readability(self, original, processed):
        # Use libraries like textstat
        original_score = textstat.flesch_reading_ease(original)
        processed_score = textstat.flesch_reading_ease(processed)
        return processed_score - original_score

    def quality_score(self, metrics):
        # Weighted scoring system
        weights = {
            "ai_detection": 0.4,
            "readability": 0.2,
            "character_consistency": 0.2,
            "prohibited_removal": 0.1,
            "meaning_preservation": 0.1
        }

        total_score = 0
        for metric, weight in weights.items():
            total_score += metrics.get(metric, 0) * weight

        return min(100, max(0, total_score))
```

### Performance Monitoring
```python
class PerformanceMonitor:
    def __init__(self):
        self.metrics = []

    def log_processing(self, text_length, processing_time, quality_score, cost):
        self.metrics.append({
            "text_length": text_length,
            "processing_time": processing_time,
            "quality_score": quality_score,
            "cost": cost,
            "cost_per_word": cost / text_length * 1000,  # per 1000 words
            "timestamp": datetime.now()
        })

    def get_performance_stats(self, days=7):
        cutoff = datetime.now() - timedelta(days=days)
        recent_metrics = [m for m in self.metrics if m["timestamp"] > cutoff]

        if not recent_metrics:
            return None

        return {
            "avg_quality": np.mean([m["quality_score"] for m in recent_metrics]),
            "avg_cost_per_1k_words": np.mean([m["cost_per_word"] for m in recent_metrics]),
            "avg_processing_time": np.mean([m["processing_time"] for m in recent_metrics]),
            "total_processed": len(recent_metrics),
            "total_cost": sum([m["cost"] for m in recent_metrics])
        }
```

### Environment-Specific Configurations

#### Development Environment
```yaml
dev_config:
  models: ["claude-sonnet-4-5-20250929"]  # Use same model as production for consistency
  cost_limit_per_day: "$10"
  quality_threshold: "80%"
  enable_detailed_logging: true
  mock_expensive_models: false  # Test with actual model for accurate results
```

#### Production Environment
```yaml
prod_config:
  models: ["claude-sonnet-4-5-20250929"]  # Recommended: Claude Sonnet 4.5 for all phases
  cost_limit_per_day: "$500"
  quality_threshold: "95%"
  enable_monitoring: true
  alert_on_quality_drop: true
  backup_models: ["claude-3-5-sonnet-20241022"]  # Fallback if Sonnet 4.5 unavailable
```

### Monitoring and Alerting
```python
class AlertManager:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def check_alerts(self, metrics):
        alerts = []

        if metrics.get("quality_score", 100) < 85:
            alerts.append("Quality score below threshold")

        if metrics.get("processing_time", 0) > 300:  # 5 minutes
            alerts.append("Processing time exceeded limit")

        if any("prohibited" in word for word in metrics.get("prohibited_words_found", [])):
            alerts.append("Prohibited words detected in output")

        for alert in alerts:
            self.send_alert(alert)

    def send_alert(self, message):
        payload = {
            "text": f"ClaudeHumanizer Alert: {message}",
            "timestamp": datetime.now().isoformat()
        }
        requests.post(self.webhook_url, json=payload)
```

## Architectural Summary: Phase 9/9.5/10 Separation

### Clear Separation of Concerns

The ClaudeHumanizer system now features a refined architecture with three distinct phases handling different aspects of AI detection countermeasures:

#### Phase 9: Qualitative Pattern Replacement
- **Focus**: QUALITATIVE pattern detection and replacement
- **Handles**: N-gram filtering, formulaic phrases, AI patterns, perplexity optimization
- **Temperature**: 0.2-0.3 (analytical)
- **Memory**: Medium (pattern corpus and AI detection patterns)
- **Purpose**: Identifies and replaces predictable AI language patterns

#### Phase 9.5: Quantitative Statistical Hub (OPTIONAL)
- **Focus**: QUANTITATIVE statistical analysis and optimization
- **Handles**: Burstiness (CV, range, variance), POS distribution (noun/verb/adj ratios), Lexical diversity (TTR)
- **Temperature**: 0.3-0.4 (analytical with natural optimization)
- **Memory**: High (comprehensive full-text statistical analysis)
- **Purpose**: Single-pass coordinated statistical optimization
- **Skip When**: Budget constraints, fast turnaround needed, text already has good statistical properties

#### Phase 10: Pure Word Filtering
- **Focus**: Word-level filtering ONLY
- **Handles**: Prohibited word removal using master_prohibited_words.json
- **Temperature**: 0.2-0.3 (analytical)
- **Memory**: Low (surgical word replacement)
- **Purpose**: Final quality control checkpoint for prohibited words

### Benefits of This Architecture

1. **Single-Pass Efficiency**: Phase 9.5 reads text once and calculates all metrics simultaneously
2. **Coordinated Optimization**: Statistical metrics are balanced together, not optimized independently
3. **Clear Conceptual Boundaries**: Qualitative (9) vs Quantitative (9.5) vs Filtering (10)
4. **Budget Flexibility**: Phase 9.5 can be skipped for 10-15% cost savings with minimal quality impact
5. **Better Maintenance**: Each phase has a single, well-defined responsibility

### Processing Flow

```
Phase 9 (Pattern Replacement)
  ↓
Phase 9.5 (Statistical Analysis) - OPTIONAL
  ↓
Phase 10 (Word Filtering)
```

### When to Include Phase 9.5

**Include Phase 9.5 if:**
- AI detection is a serious concern
- Text quality is paramount
- Budget allows for comprehensive optimization
- Text may have statistical anomalies (too uniform, unbalanced POS distribution)

**Skip Phase 9.5 if:**
- Budget is constrained (saves 10-15% of total cost)
- Fast turnaround is critical
- Text already has good statistical properties
- Processing large volumes where aggregate quality is acceptable

### Cost-Quality Tradeoffs

| Configuration | Quality | Cost per 10K words | Use Case |
|--------------|---------|-------------------|----------|
| Full Pipeline (with 9.5) | 95-98% | $0.60-2.30 | Maximum quality, AI detection critical |
| Standard (without 9.5) | 93-96% | $0.50-2.00 | Good quality, moderate AI detection concern |
| Budget (Haiku + skip 9.5) | 85-90% | $0.20-0.80 | Cost-sensitive, basic humanization |

---

## Prompt Development & Standardization

**NEW in v3.1.0**: ClaudeHumanizer now includes a comprehensive standardization system for maintaining consistent, high-quality phase prompts.

### Standardization Overview

All phase prompts follow a standardized structure to ensure:
- **Consistency** across all phases
- **Maintainability** for easier updates
- **Quality** through automated validation
- **Clarity** for developers and LLMs

### Key Files

| File | Purpose |
|------|---------|
| `PROMPT_TEMPLATE.json` | Master template with all sections tagged as [REQUIRED], [OPTIONAL], or [PHASE-SPECIFIC] |
| `PROMPT_STANDARDS.md` | Human-readable documentation of standardization rules |
| `STANDARDIZATION_SUMMARY.md` | Overview of the standardization system |
| `validate_prompt.py` | Automated validation script |

### Standard Prompt Structure

Every phase prompt follows this exact order:

```
1. HEADER BLOCK
   - title, version, date
   - assembly_line_position (line 4)
   - description

2. DOMAIN RESTRICTIONS
   - only_handle
   - never_touch (must include 4 standard items)
   - respect_assembly_line

3. PERSONA & FRAMEWORK
   - persona (4 fields: name, background, expertise, philosophy)
   - agent_directives (3 fields: persistence, tool_usage, deliberate_planning)
   - anti_hallucination_framework (3 fields: real_world_facts, fictional_world_building, fallback_strategy)

4. SPECIAL NOTES (optional)
   - master_prohibited_list_reference (Phases 2, 6.1, 7, 10)
   - note_on_word_filtering (Phases 5, 6, 8, 9)
   - note_on_statistical_metrics (Phases 9, 10)

5. PHASE-SPECIFIC CONTENT (variable)
   - Use standardized naming conventions
   - processing_instructions (not "core_instructions")
   - detection_criteria or detection_framework
   - enhancement_techniques or optimization_strategies

6. OUTPUT FORMAT (standardized)
   - Identical across all phases except [bracketed] placeholders

7. CRITICAL_FINAL_INSTRUCTION (standardized)
   - Last line of every prompt
```

### Creating a New Phase Prompt

1. **Copy the template:**
   ```bash
   cp PROMPT_TEMPLATE.json new_phase.json
   ```

2. **Replace placeholders:**
   - Change all `[bracketed content]` to phase-specific values
   - Update version and date
   - Add phase-specific sections

3. **Remove template guidance:**
   - Delete all `COMMENT_` fields
   - Remove `_TEMPLATE_INSTRUCTIONS`, `_SECTION_TAGS`, etc.
   - Remove `OPTIONAL_` fields that don't apply

4. **Validate:**
   ```bash
   python validate_prompt.py new_phase.json
   ```

5. **Test:**
   - Verify phase works correctly in isolation
   - Test integration in full pipeline

### Modifying Existing Phase Prompts

1. **Read the phase prompt** to understand domain boundaries
2. **Make your changes** while maintaining standard structure
3. **Update version number** using semantic versioning:
   - MAJOR: Breaking changes
   - MINOR: New functionality
   - PATCH: Bug fixes, clarifications
4. **Update date field** to current date (YYYY-MM-DD)
5. **Validate changes:**
   ```bash
   python validate_prompt.py <phase_file>.json
   ```
6. **Test domain isolation** - ensure phase only affects its domain
7. **Test sequential integration** - run full pipeline

### Validation Script Usage

**Check single file:**
```bash
python validate_prompt.py 3_overwritten_language_reduction.json
```

**Check all phase files:**
```bash
python validate_prompt.py --all
```

**Output interpretation:**
- ✗ **ERROR** (red): Critical issue, must fix
- ⚠ **WARNING** (yellow): Should fix for consistency
- ℹ **INFO** (blue): Suggestion or minor issue

### Standardized Components

**Required in all phases:**
- `never_touch` list must include these 4 items:
  - "Dialogue content (text in quotation marks)"
  - "Markdown formatting (headers, links, code blocks, etc.)"
  - "Character speech patterns"
  - "Work completed by previous phases"

- `agent_directives` must have exactly 3 fields:
  - `persistence`: When to conclude work
  - `tool_usage`: Guidance on tools vs guessing
  - `deliberate_planning`: Planning approach

- `anti_hallucination_framework` must have exactly 3 fields:
  - `real_world_facts`: How to handle factual content
  - `fictional_world_building`: How to handle creative content
  - `fallback_strategy`: What to do when uncertain

- `output_format`: Entire block should be identical across phases except for [bracketed] placeholders

### Naming Conventions

Use these standardized names in phase-specific sections:

| Concept | Use This | Avoid |
|---------|----------|-------|
| Step-by-step instructions | `processing_instructions` | "core_instructions", "processing_steps" |
| Issue identification | `detection_criteria` or `detection_framework` | "identification_rules" |
| Improvement strategies | `enhancement_techniques` or `optimization_strategies` | "improvement_methods" |
| Replacement rules | `replacement_guidelines` or `conversion_strategies` | "replacement_rules" |
| Quality metrics | `quality_standards` or `quality_assurance` | "quality_checks" |

### Benefits of Standardization

**For Development:**
- Easier to create new phases (copy template, fill placeholders)
- Faster updates (know exactly where to find each instruction type)
- Better diffs (changes easier to spot in version control)
- Reduced errors (less chance of omitting critical instructions)

**For Maintenance:**
- Quick audits (run validator on all prompts)
- Consistent updates (change once, apply everywhere)
- Clear structure (anyone can understand prompt organization)

**For LLMs:**
- Predictable context (same structure aids comprehension)
- Consistent priming (standard order ensures critical context comes early)
- Better parsing (well-structured prompts easier to process)

### Optimization Best Practices

**When optimizing prompts:**
1. **Remove redundancy** - Consolidate duplicate instructions
2. **Use compact formats** - Tables and hierarchical lists over verbose prose
3. **Keep functionality** - Never remove essential instructions
4. **Maintain clarity** - Shorter is better only if equally clear
5. **Validate changes** - Run validator and test the phase

**Recent optimizations (v3.1.0):**
- Phase 3: Consolidated passive voice and nominalization sections (~122 lines saved)
- Phase 9: Hierarchical N-gram pattern families (improved clarity)
- Phase 8: Streamlined punctuation inconsistency examples (~47 lines saved)
- Phase 9.5: Compact genre target format (~17 lines saved)

Total: ~200 lines reduced across 6 phases with improved maintainability.

---

For usage instructions and workflow guides, see the [Usage Guide](USAGE_GUIDE.md).
For customization and character-specific configurations, see the [Customization Guide](CUSTOMIZATION.md).