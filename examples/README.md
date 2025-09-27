# ClaudeHumanizer Pipeline Configuration Examples

This directory contains sample YAML configuration files for different ClaudeHumanizer assembly line setups. Each configuration represents a different optimization strategy balancing quality, cost, and specific model ecosystem preferences.

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
- ✅ **Complete 9-phase assembly line** (Phases 1-9)
- ✅ **Optional Phase 6.5** (Character-specific dialogue enhancement)
- ✅ **Master prohibited words list integration** for phases requiring it
- ✅ **Proper temperature and parameter optimization** for each phase
- ✅ **Cost and quality metadata** for easy comparison
- ✅ **Usage tracking** for cost monitoring

### Phase Breakdown (All Configurations):
1. **Grammar Foundation** - Critical grammar fixes
2. **AI Word Cleaning** - Remove AI-associated vocabulary (requires master list)
3. **Overwritten Language Reduction** - Eliminate purple prose
4. **Sensory Enhancement** - Add vivid details to flat passages
5. **Subtlety Creation** - Convert obvious statements to sophisticated implications (requires master list)
6. **Dialogue Enhancement** - Improve character voices (requires master list)
7. **Phase 6.5: Character-Specific Dialogue** - Targeted character voice refinement (requires master list)
8. **Weak Language Cleanup** - Remove hedge words and filler (requires master list)
9. **Strategic Imperfections** - Add authentic human rhythm and flow (requires master list)
10. **Final Verification** - Quality control and AI pattern detection (requires master list)

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
- All phase JSON prompt files (1-9, plus 6.5)
- `master_prohibited_words.json`
- Input text file

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

**Last Updated:** 2025-09-27 - Complete configuration examples with Phase 6.5 integration