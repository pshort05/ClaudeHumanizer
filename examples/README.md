# ClaudeHumanizer Examples & Workflows

This directory contains ready-to-use n8n workflows and pipeline configuration files for automating the ClaudeHumanizer assembly line.

---

## n8n Workflows (RECOMMENDED)

### Chapter Loop Workflow ⭐ NEW - Best for Books

**Files:**
- `n8n_chapter_loop_workflow.json` - Ready-to-import n8n workflow
- `N8N_CHAPTER_LOOP_GUIDE.md` - Complete setup and usage documentation

**Description:**
Automatically processes entire books chapter-by-chapter through all 10 phases. Loops through each chapter sequentially until complete.

**Key Features:**
- ✅ Automatic looping through all chapters
- ✅ Claude Sonnet 4.5 for all phases
- ✅ Optional Phase 9.5 (statistical analysis)
- ✅ Progress tracking
- ✅ Returns original + humanized text for each chapter
- ✅ ~3-4 minutes per chapter
- ✅ ~$1.00-1.20 per chapter

**Best For:**
- Novels and book-length manuscripts
- Processing 5-50+ chapters in one request
- Automated end-to-end book humanization

**Quick Start:**
```bash
# Import n8n_chapter_loop_workflow.json into n8n
# Configure file paths and Anthropic API credentials
# Send POST request:
curl -X POST https://your-n8n-instance.com/webhook/claudehumanizer-chapters \
  -H "Content-Type: application/json" \
  -d '{
    "chapters": [
      {"number": 1, "title": "Chapter One", "text": "..."},
      {"number": 2, "title": "Chapter Two", "text": "..."}
    ],
    "include_phase_9_5": false
  }'
```

**Full Documentation:** See `N8N_CHAPTER_LOOP_GUIDE.md`

---

### Single Text Workflow

**File:** `n8n_workflow_sample.json`

**Description:**
Processes a single text document through all 10 phases sequentially. Simple linear flow.

**Best For:**
- Articles
- Short stories
- Single chapters
- Testing and experimentation

**Documentation:** See `docs/TECHNICAL_REFERENCE.md`

---

## YAML Pipeline Configurations

This directory also contains sample YAML configuration files for different ClaudeHumanizer assembly line setups. Each configuration represents a different optimization strategy balancing quality, cost, and specific model ecosystem preferences.

## Available Configurations

### 1. Maximum Quality Pipeline
**File:** `maximum_quality_pipeline.yaml`
- **Cost:** Premium ($4.00-7.00 per 1000 words)
- **Quality Score:** 100%
- **Models:** Latest generation cutting-edge models
- **Best For:** Premium quality humanization with no budget constraints
- **Key Features:** Claude 4.0, GPT-5, Gemini 3.5 Ultra

### 2. Cost-Effective High Quality Pipeline
**File:** `cost_effective_high_quality_pipeline.yaml`
- **Cost:** Budget-conscious ($1.20-2.00 per 1000 words)
- **Quality Score:** 90%
- **Models:** Strategic mix of current-generation models
- **Best For:** High quality results with budget consciousness
- **Key Features:** 40-50% cost savings vs premium, smart model selection

### 3. Anthropic-Only Pipeline
**File:** `anthropic_only_pipeline.yaml`
- **Cost:** High ($3.00-5.00 per 1000 words)
- **Quality Score:** 95%
- **Models:** Only Anthropic Claude models
- **Best For:** Users prioritizing literary quality and consistency
- **Key Features:** Consistent instruction following, excellent voice preservation

### 4. OpenAI-Only Pipeline
**File:** `openai_only_pipeline.yaml`
- **Cost:** Medium-High ($2.50-4.00 per 1000 words)
- **Quality Score:** 85%
- **Models:** Only OpenAI GPT models
- **Best For:** Single-vendor relationship preference
- **Key Features:** Strong dialogue generation, good all-around performance

### 5. Google-Only Pipeline
**File:** `google_only_pipeline.yaml`
- **Cost:** Medium ($1.50-2.50 per 1000 words)
- **Quality Score:** 70%
- **Models:** Only Google Gemini models
- **Best For:** Systematic consistency over creativity
- **Key Features:** Long context window, cost-effective, systematic approach

### 6. Hybrid Budget-Conscious Pipeline
**File:** `hybrid_budget_conscious_pipeline.yaml`
- **Cost:** Budget-friendly ($0.80-1.50 per 1000 words)
- **Quality Score:** 90%
- **Models:** Strategic mix including open-source options
- **Best For:** Maximum quality per dollar spent
- **Key Features:** Uses Llama 3.1 405B for cost savings, premium models where needed

### 7. Single-Family Anthropic (Optimized)
**File:** `single_family_anthropic_pipeline.yaml`
- **Cost:** High ($3.00-5.00 per 1000 words)
- **Quality Score:** 95%
- **Models:** Optimized distribution of Sonnet and Opus
- **Best For:** Anthropic ecosystem with optimal model selection
- **Key Features:** Sonnet for precision, Opus for creativity

## Universal Features

### All Configurations Include:
- ✅ **Complete 10-phase assembly line** (Phases 1-10)
- ✅ **Optional Phase 6.1** (Character-specific dialogue enhancement)
- ✅ **Optional Phase 9.5** (Statistical analysis hub)
- ✅ **Master prohibited words list integration** for phases requiring it (2 and 10)
- ✅ **Proper temperature and parameter optimization** for each phase
- ✅ **Cost and quality metadata** for easy comparison
- ✅ **Usage tracking** for cost monitoring

### Phase Breakdown (Current Architecture):
1. **Grammar Foundation** - Critical grammar fixes only
2. **AI Word Cleaning** - Remove AI-associated vocabulary (requires master list)
3. **Overwritten Language Reduction** - Eliminate purple prose and nominalization
4. **Sensory Enhancement** - Add vivid details to flat passages
5. **Subtlety Creation** - Convert obvious statements to sophisticated implications
6. **Dialogue Enhancement** - Improve character voices (temperature 1.0)
7. **Phase 6.1: Character-Specific Dialogue** (OPTIONAL) - Targeted character voice refinement
8. **Weak Language Cleanup** - Remove 12 categories of weak language patterns
9. **Strategic Imperfections** - Add authentic human rhythm and punctuation variation
10. **Phase 9: Final Verification** - AI pattern detection (qualitative)
11. **Phase 9.5: Statistical Analysis Hub** (OPTIONAL) - Quantitative metrics optimization
12. **Phase 10: Final AI Word Sweep** - Prohibited word filtering (requires master list)

## How to Use These Configurations

### Method 1: With OpenRouter Interface Chain Runner
```bash
# Copy desired configuration to your working directory
cp examples/cost_effective_high_quality_pipeline.yaml my_config.yaml

# Run the chain
PYTHONPATH=src python3 -m openrouter_interface.chain -c my_config.yaml --debug
```

### Method 2: Manual Phase Execution
1. Choose your preferred configuration
2. Follow the phase execution order specified in each YAML
3. Include `master_prohibited_words.json` for phases marked as requiring it
4. Use the model and temperature settings specified for each phase

### Method 3: Automation Integration
These configurations are designed to work with:
- **n8n workflows** - For visual automation
- **Make.com scenarios** - For robust integration
- **Custom scripts** - Using the metadata for cost tracking

## Configuration Selection Guide

### Choose Based on Priority:

**Quality First:**
- Maximum Quality Pipeline (100% quality)
- Single-Family Anthropic (95% quality)
- Anthropic-Only Pipeline (95% quality)

**Cost First:**
- Hybrid Budget-Conscious (90% quality, lowest cost)
- Google-Only Pipeline (70% quality, medium cost)
- Cost-Effective High Quality (90% quality, good balance)

**Ecosystem Preference:**
- Anthropic-Only or Single-Family Anthropic
- OpenAI-Only Pipeline
- Google-Only Pipeline

**Balanced Approach:**
- Cost-Effective High Quality Pipeline
- Hybrid Budget-Conscious Pipeline

## Customization Guidelines

### Model Substitution:
- Replace model names with available alternatives
- Maintain temperature ranges appropriate for each phase type
- Keep provider preferences consistent within single-family configs

### Parameter Tuning:
- **Grammar/Verification phases:** Low temperature (0.1-0.3)
- **Creative phases:** Higher temperature (0.7-0.9)
- **Analytical phases:** Medium temperature (0.4-0.6)

### Cost Optimization:
- Use faster/cheaper models for phases 1, 7, 9 (systematic tasks)
- Invest in premium models for phases 4, 5, 6, 8 (creative tasks)
- Monitor usage tracking to optimize spending

## Quality Expectations by Configuration

| Configuration | AI Detection Pass Rate | Voice Preservation | Creative Enhancement | Cost Efficiency |
|---------------|------------------------|-------------------|---------------------|-----------------|
| Maximum Quality | 99%+ | Excellent | Superior | Low |
| Cost-Effective | 95%+ | Very Good | Good | High |
| Anthropic-Only | 98%+ | Excellent | Very Good | Medium |
| OpenAI-Only | 90%+ | Good | Good | Medium |
| Google-Only | 85%+ | Fair | Limited | High |
| Hybrid Budget | 95%+ | Very Good | Good | Very High |
| Anthropic Optimized | 98%+ | Excellent | Very Good | Medium |

## Prerequisites

### Required Files:
- All phase JSON prompt files (1-10)
- Optional: `6.1_character_dialogue_pass.json`
- Optional: `9.5_statistical_analysis_hub.json`
- `master_prohibited_words.json`
- Input text file(s) or chapter array

### Environment Setup:
- OpenRouter API key configured
- Appropriate model access permissions
- Chain runner environment (if using automated execution)

## Troubleshooting

### Common Issues:
- **Model not available:** Check OpenRouter model availability
- **Cost overruns:** Monitor usage metadata and adjust model selection
- **Quality degradation:** Ensure phases run in correct order with proper dependencies
- **Character voices unclear:** Customize Phase 6.5 specifications

### Performance Optimization:
- Use streaming for long creative phases
- Implement rate limiting for high-volume processing
- Monitor token usage to optimize max_tokens settings
- Cache results for repeated processing of similar content

## Support and Updates

These configurations are maintained alongside the main ClaudeHumanizer project. For the latest model recommendations and pricing updates, refer to the main README.md file's LLM Optimization Guide appendix.

**Last Updated:** 2025-10-26
- Added n8n Chapter Loop Workflow for automated book processing
- Updated to 10-phase architecture with optional Phase 9.5
- Updated phase breakdown and prerequisites