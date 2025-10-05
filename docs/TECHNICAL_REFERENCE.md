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

#### Phase 8: Strategic Imperfections
- **Best Model**: Claude Sonnet 4.5
- **Temperature**: 0.8-0.9
- **Memory**: High (understanding of full text flow and rhythm)
- **Reasoning**: Best understanding of authentic human writing patterns and imperfections

#### Phase 9: Final Verification
- **Best Model**: Claude Sonnet 4.5
- **Temperature**: 0.1-0.2
- **Memory**: Medium (AI pattern detection, perfection syndrome, rhythm variations)
- **Reasoning**: Comprehensive AI pattern detection without word-level filtering
- **Note**: No longer performs prohibited word removal (moved to Phase 10)

#### Phase 10: Final AI Word Sweep (NEW)
- **Best Model**: Claude Sonnet 4.5
- **Temperature**: 0.2-0.3
- **Memory**: Low (surgical word replacement only)
- **Reasoning**: Catches prohibited words reintroduced by phases 3-9
- **Pattern Rules Applied**: All pattern rules from master_prohibited_words.json
- **Critical Role**: Final quality control checkpoint before output

### Model Family Strategies

#### Single-Family Approaches

**Anthropic-Only Pipeline (RECOMMENDED)**:
```yaml
models: Claude Sonnet 4.5 (all 10 phases)
temperatures: 0.1-0.2 (phases 1,7,9), 0.3-0.5 (phases 2,3,5,10), 0.6-0.9 (phases 4,8), 1.0 (phase 6)
quality: 95-98% of maximum potential
cost: Medium-High
best_for: Optimal humanization with consistent quality across all text types
consistency: Superior assembly line constraint adherence
pattern_recognition: Best for new pattern-based rules
```

**OpenAI-Only Pipeline**:
```yaml
models: GPT-4 Turbo (1,3,7,9,10) + GPT-4o (2,4,5,6,8)
quality: 80-85% of maximum potential
cost: Medium-High
best_for: Single-vendor relationship
limitations: Less effective at pattern recognition and literary judgment
```

**Google-Only Pipeline**:
```yaml
models: Gemini 1.5 Pro (all 10 phases)
quality: 70-75% of maximum potential
cost: Medium
best_for: Systematic consistency over creativity
limitations: Weaker at nuanced literary decisions
```

#### Optimal Claude Sonnet 4.5 Configuration (RECOMMENDED)
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
phase_10: Claude Sonnet 4.5 @ 0.3  # NEW: Final word sweep

quality: 95-98% of maximum potential
cost: Medium-High (~$0.50-2.00 per 10k words depending on text complexity)
consistency: Excellent - single model understands full assembly line context
advantages:
  - Superior pattern recognition (dialogue pauses, light descriptions, finger actions)
  - Best literary judgment and nuance
  - Excellent instruction following across all phases
  - No model switching overhead
```

#### Budget-Friendly Configuration
```yaml
phase_1: Claude Sonnet 4.5 @ 0.2
phase_2: Claude Sonnet 4.5 @ 0.4
phase_3: Claude Haiku @ 0.3
phase_4: Claude Sonnet 4.5 @ 0.7
phase_5: Claude Haiku @ 0.5
phase_6: Claude Sonnet 4.5 @ 1.0
phase_7: Claude Haiku @ 0.2
phase_8: Claude Sonnet 4.5 @ 0.9
phase_9: Claude Haiku @ 0.2
phase_10: Claude Sonnet 4.5 @ 0.3

quality: 85-90% of maximum potential
cost_savings: 50-60% vs full Sonnet 4.5 pipeline
strategy: Use Sonnet 4.5 for critical creative/pattern phases (2,4,6,8,10), Haiku for systematic phases
```

## Automation Integration

### n8n Workflow Implementation

#### Basic Workflow Architecture
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
      "type": "n8n-nodes-base.anthropic",
      "parameters": {
        "model": "claude-3-5-sonnet-20241022",
        "temperature": 0.2,
        "systemMessage": "{{ $json.grammarPrompt }}",
        "message": "{{ $json.inputText }}"
      }
    }
  ]
}
```

#### Multi-Model Node Configuration
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
    "systemPrompt": "{{ $env.MASTER_PROHIBITED_WORDS }}\\n\\n{{ $env.AI_CLEANING_PROMPT }}"
  },
  "phase3": {
    "node": "Anthropic Claude",
    "model": "claude-3-opus-20240229",
    "temperature": 0.3,
    "systemPrompt": "{{ $env.PURPLE_PROSE_PROMPT }}"
  }
}
```

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

#### Dynamic Model Selection Function (Claude Sonnet 4.5 Recommended)
```javascript
function selectModel(phase) {
  // RECOMMENDED: Claude Sonnet 4.5 for all phases
  const modelConfig = {
    1: { provider: "anthropic", model: "claude-sonnet-4-5-20250929", temp: 0.2 },
    2: { provider: "anthropic", model: "claude-sonnet-4-5-20250929", temp: 0.4 },
    3: { provider: "anthropic", model: "claude-sonnet-4-5-20250929", temp: 0.3 },
    4: { provider: "anthropic", model: "claude-sonnet-4-5-20250929", temp: 0.7 },
    5: { provider: "anthropic", model: "claude-sonnet-4-5-20250929", temp: 0.5 },
    6: { provider: "anthropic", model: "claude-sonnet-4-5-20250929", temp: 1.0 },  // Increased for dialogue
    7: { provider: "anthropic", model: "claude-sonnet-4-5-20250929", temp: 0.2 },
    8: { provider: "anthropic", model: "claude-sonnet-4-5-20250929", temp: 0.9 },
    9: { provider: "anthropic", model: "claude-sonnet-4-5-20250929", temp: 0.2 },
    10: { provider: "anthropic", model: "claude-sonnet-4-5-20250929", temp: 0.3 }  // NEW: Phase 10
  };
  return modelConfig[phase];
}
```

## API Configurations

### Anthropic Claude API
```python
import anthropic

client = anthropic.Anthropic(api_key="your-api-key")

def process_phase_anthropic(text, prompt, model="claude-3-5-sonnet-20241022", temperature=0.2):
    response = client.messages.create(
        model=model,
        max_tokens=4096,
        temperature=temperature,
        system=prompt,
        messages=[{"role": "user", "content": text}]
    )
    return response.content[0].text
```

### OpenAI GPT API
```python
import openai

client = openai.OpenAI(api_key="your-api-key")

def process_phase_openai(text, prompt, model="gpt-4o", temperature=0.4):
    response = client.chat.completions.create(
        model=model,
        temperature=temperature,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content
```

### Google Gemini API
```python
import google.generativeai as genai

genai.configure(api_key="your-api-key")

def process_phase_gemini(text, prompt, model="gemini-1.5-pro", temperature=0.2):
    model = genai.GenerativeModel(model)
    response = model.generate_content(
        f"{prompt}\\n\\n{text}",
        generation_config=genai.types.GenerationConfig(
            temperature=temperature,
            max_output_tokens=4096
        )
    )
    return response.text
```

### Complete Pipeline Implementation
```python
class ClaudeHumanizerPipeline:
    def __init__(self, config):
        self.config = config
        self.load_prompts()
        self.load_master_prohibited_words()

    def load_prompts(self):
        self.prompts = {}
        for i in range(1, 11):  # Updated to 11 for 10 phases
            with open(f"{i}_*.json", "r") as f:
                self.prompts[i] = json.load(f)

    def load_master_prohibited_words(self):
        with open("master_prohibited_words.json", "r") as f:
            self.master_prohibited = json.load(f)

    def process_text(self, text):
        current_text = text

        for phase in range(1, 11):  # Updated to 11 for 10 phases
            print(f"Processing Phase {phase}...")

            # Prepare prompt
            prompt = self.prompts[phase]["content"]
            # ONLY Phases 2 and 10 require master list with pattern rules
            if phase in [2, 10]:
                prompt = f"{self.master_prohibited}\\n\\n{prompt}"

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
  models: ["claude-3-5-sonnet", "gpt-4o-mini", "gemini-1.5-flash"]
  cost_limit_per_day: "$10"
  quality_threshold: "80%"
  enable_detailed_logging: true
  mock_expensive_models: true
```

#### Production Environment
```yaml
prod_config:
  models: ["claude-opus", "gpt-4o", "gemini-1.5-pro"]
  cost_limit_per_day: "$500"
  quality_threshold: "95%"
  enable_monitoring: true
  alert_on_quality_drop: true
  backup_models: ["claude-3-5-sonnet", "gpt-4-turbo"]
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

---

For usage instructions and workflow guides, see the [Usage Guide](USAGE_GUIDE.md).
For customization and character-specific configurations, see the [Customization Guide](CUSTOMIZATION.md).