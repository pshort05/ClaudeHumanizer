# ClaudeHumanizer Customization Guide

Advanced customization options for tailoring the ClaudeHumanizer assembly line to specific needs, including character-specific dialogue enhancement and master prohibited words management.

## Table of Contents

- [Character-Specific Dialogue Customization](#character-specific-dialogue-customization)
- [Master Prohibited Words Management](#master-prohibited-words-management)
- [Custom Phase Development](#custom-phase-development)
- [Project-Specific Configurations](#project-specific-configurations)
- [Advanced Workflow Customization](#advanced-workflow-customization)

## Character-Specific Dialogue Customization

Phase 6.1 provides targeted character voice refinement beyond general dialogue enhancement. This section explains how to customize the sample prompt for your specific characters and projects.

### Understanding Character Specifications

The `6.1_character_dialogue_pass.json` file contains a `character_specifications` section that you can customize for your project's characters.

#### Basic Character Template Structure

```json
{
  "character_name": "[Your Character's Name]",
  "voice_requirements": {
    "background_integration": "[Character's education, profession, regional background, family history]",
    "speech_patterns": "[Sentence length preferences, rhythm, unique grammatical patterns]",
    "vocabulary_preferences": "[Specific word choices, technical terminology, slang usage]",
    "signature_phrases": ["[List of 3-5 phrases character uses frequently]"],
    "disfluencies": "[How character speaks imperfectly - filler words, hesitations, etc.]",
    "formality_level": "[Formal, casual, code-switching patterns]",
    "emotional_expression": "[How character expresses or avoids expressing emotions]"
  },
  "specific_adjustments": [
    "[Specific instruction 1]",
    "[Specific instruction 2]",
    "[Specific instruction 3]",
    "[Additional targeted changes needed]"
  ]
}
```

### Step-by-Step Customization Process

#### Step 1: Identify Characters Needing Voice Refinement

Use Phase 6.1 for characters requiring:
- **Unclear distinction** after general Phase 6 enhancement
- **Specific cultural/professional speech patterns**
- **Series continuity matching** for established character voices
- **Personality shifts** requiring voice evolution mid-story

#### Step 2: Replace Example Characters

Remove example characters and add your actual characters:

```json
"character_specifications": {
  "usage_note": "Customized for [Your Project Name]",

  "main_character_name": {
    "character_name": "Sarah Chen",
    "voice_requirements": {
      "background_integration": "Second-generation immigrant, software engineer, Silicon Valley tech culture",
      "speech_patterns": "Precise, analytical. Uses technical metaphors. Short sentences when stressed.",
      "vocabulary_preferences": "Tech jargon naturally integrated, avoids corporate buzzwords",
      "signature_phrases": ["Let me think about this", "That doesn't compute", "Running the numbers"],
      "disfluencies": "Says 'um' when processing complex ideas, trails off when overwhelmed",
      "formality_level": "Professional but approachable. Uses contractions with friends.",
      "emotional_expression": "Processes emotions like debugging - systematic, step-by-step"
    },
    "specific_adjustments": [
      "Replace flowery language with precise technical descriptions",
      "Add subtle tech metaphors for emotional states",
      "Include occasional coding references in casual speech",
      "Ensure dialogue reflects logical thinking patterns"
    ]
  }
}
```

#### Step 3: Define Voice Requirements Components

**Background Integration:**
- Education level and type (formal education, self-taught, trade school)
- Professional experience and current job
- Regional/cultural background
- Family and socioeconomic history
- Life experiences that shape worldview

**Speech Patterns:**
- Sentence length preference (short and clipped vs. long and flowing)
- Rhythm and pacing (fast talker vs. deliberate speaker)
- Question vs. statement tendency
- Complex vs. simple sentence structures

**Vocabulary Preferences:**
- Professional jargon and technical terms
- Regional dialect or slang
- Generational language markers
- Words they would never use
- Preferred synonyms for common concepts

**Signature Phrases:**
- Catchphrases or verbal tics
- Common expressions they overuse
- Transitional phrases
- Emotional outlet phrases
- Professional expressions

**Disfluencies:**
- Filler words (um, uh, like, you know)
- Speech patterns when nervous/excited/angry
- Tendency to interrupt or be interrupted
- Incomplete thoughts or trailing sentences

**Formality Level:**
- Code-switching patterns (formal with authority, casual with peers)
- Contraction usage
- Polite vs. direct communication style
- Professional vs. personal speech differences

**Emotional Expression:**
- How they show happiness, anger, sadness, fear
- Tendency to be direct vs. indirect with feelings
- Use of humor, sarcasm, or deflection
- Physical expressions that accompany speech

#### Step 4: Write Specific Adjustments

Provide concrete, actionable instructions for the AI:

**Good Examples:**
- "Replace academic language with street-smart expressions"
- "Add occasional Spanish words during emotional moments"
- "Include military rank structure references in casual conversation"
- "Remove contractions to reflect formal upbringing"

**Avoid Vague Instructions:**
- "Make them sound more professional" ❌
- "Add personality" ❌
- "Make dialogue better" ❌

### Character Type Examples

#### The Academic Professor
```json
"professor_martinez": {
  "character_name": "Dr. Elena Martinez",
  "voice_requirements": {
    "background_integration": "Literature PhD, 20 years teaching, multilingual Spanish/English",
    "speech_patterns": "Long, complex sentences. Pauses to choose precise words.",
    "vocabulary_preferences": "Literary references, avoids slang, precise word choice",
    "signature_phrases": ["Precisely", "That's fascinating", "Consider this", "In my experience"],
    "disfluencies": "Hmm when thinking, occasional Spanish under breath",
    "formality_level": "Formal with students, warmer with colleagues, never crude",
    "emotional_expression": "Uses metaphor and literary allusion to express feelings"
  },
  "specific_adjustments": [
    "Expand simple statements into more nuanced expressions",
    "Add subtle literary references or metaphors",
    "Include occasional Spanish during emotional moments",
    "Ensure vocabulary reflects education level and precision"
  ]
}
```

#### The Street-Smart Detective
```json
"detective_burke": {
  "character_name": "Detective Mike Burke",
  "voice_requirements": {
    "background_integration": "20 years NYPD, working-class Brooklyn, high school education",
    "speech_patterns": "Short, direct sentences. Rapid-fire when excited.",
    "vocabulary_preferences": "Police procedural terms, street slang, avoids academic language",
    "signature_phrases": ["What've we got", "Copy that", "Let's roll", "You kidding me"],
    "disfluencies": "Rarely hesitates except when dealing with personal topics",
    "formality_level": "Professional with superiors, casual with partners, blunt with suspects",
    "emotional_expression": "Shows emotion through action rather than words"
  },
  "specific_adjustments": [
    "Replace academic language with street-smart expressions",
    "Add police procedural terminology naturally",
    "Keep responses short and action-oriented",
    "Include Brooklyn dialect markers without phonetic spelling"
  ]
}
```

#### The Teenager Character
```json
"maya_teenager": {
  "character_name": "Maya",
  "voice_requirements": {
    "background_integration": "16 years old, Gen Z, social media native, suburban middle class",
    "speech_patterns": "Run-on sentences when excited, fragments when texting-influenced",
    "vocabulary_preferences": "Current slang, social media terms, avoids formal language",
    "signature_phrases": ["literally", "like", "no cap", "that's so random", "I can't even"],
    "disfluencies": "Like as filler word, trails off when distracted by phone",
    "formality_level": "Casual with everyone, slightly more respectful with teachers",
    "emotional_expression": "Dramatic emotional expression, everything is 'literally the worst/best'"
  },
  "specific_adjustments": [
    "Add current Gen Z slang and expressions",
    "Include social media influenced speech patterns",
    "Replace formal language with casual alternatives",
    "Add appropriate generational markers without overdoing it"
  ]
}
```

### Advanced Character Customization

#### Multiple Characters in One Pass

Target multiple characters simultaneously:

```json
"character_specifications": {
  "main_protagonist": { ... },
  "love_interest": { ... },
  "antagonist": { ... }
}
```

#### Character Arc Considerations

For characters who change throughout the story:

```json
"character_development_notes": {
  "early_story_voice": "Formal, hesitant, academic language",
  "mid_story_transition": "Mixing formal with street language",
  "late_story_voice": "Confident, direct, more casual expressions"
}
```

#### Relationship-Specific Speech

Characters may speak differently depending on who they're addressing:

```json
"contextual_speech_patterns": {
  "with_authority_figures": "Formal, deferential, uses titles",
  "with_peers": "Casual, uses slang, more interrupting",
  "with_subordinates": "Direct, commanding, less hedging"
}
```

### Quality Control for Character Dialogue

After running Phase 6.1, verify:

- [ ] Each targeted character has a distinct voice
- [ ] Speech patterns match established background
- [ ] Vocabulary choices feel authentic
- [ ] Signature phrases appear naturally
- [ ] Emotional expression style is consistent
- [ ] Formality levels match situational context
- [ ] Character remains recognizable without dialogue tags
- [ ] Voice changes don't contradict established personality

### Common Customization Mistakes

**❌ Over-Specification:**
- Too many conflicting requirements
- Overly complex speech patterns
- Too many signature phrases (limit to 3-5)

**❌ Under-Specification:**
- Vague background descriptions
- Generic personality traits
- No specific adjustments listed

**❌ Inconsistent Requirements:**
- Formal education but casual speech without explanation
- Shy personality but bold speech patterns
- Regional background that doesn't match vocabulary

**✅ Best Practices:**
- Focus on 2-3 key voice elements
- Provide specific, actionable adjustments
- Consider relationship contexts
- Test with sample dialogue first

## Master Prohibited Words Management

The `master_prohibited_words.json` file serves as the single source of truth for AI-associated terms that should be avoided across all phases.

### Understanding the Master List Structure

```json
{
  "version": "2.0",
  "last_updated": "2025-09-25",
  "categories": {
    "ai_buzzwords": [
      "delve", "harness", "leverage", "optimize", "synergize"
    ],
    "overused_transitions": [
      "furthermore", "moreover", "in conclusion", "ultimately"
    ],
    "artificial_descriptors": [
      "captivating", "breathtaking", "awe-inspiring", "mind-blowing"
    ],
    "corporate_speak": [
      "synergy", "paradigm", "disrupt", "streamline", "scalable"
    ]
  },
  "contextual_exceptions": {
    "technical_writing": ["optimize", "leverage"],
    "business_documents": ["synergy", "paradigm"]
  }
}
```

### Customizing the Master List

#### Adding Project-Specific Terms

```json
{
  "project_specific": {
    "your_project_name": [
      "specific_term_to_avoid_1",
      "specific_term_to_avoid_2"
    ]
  }
}
```

#### Managing Categories

**Add new categories:**
```json
"scientific_jargon": [
  "utilize", "facilitate", "demonstrate", "indicate"
]
```

**Remove categories:**
Simply delete the category from the JSON file.

#### Contextual Exceptions

Some words may be appropriate in specific contexts:

```json
"contextual_exceptions": {
  "technical_documentation": ["utilize", "implement"],
  "academic_writing": ["demonstrate", "facilitate"],
  "legal_documents": ["pursuant", "heretofore"]
}
```

### Version Management

#### Updating the Master List

1. **Increment version number**
2. **Update last_updated date**
3. **Document changes in changelog**
4. **Test with sample texts**

```json
{
  "version": "2.1",
  "last_updated": "2025-09-28",
  "changelog": [
    {
      "version": "2.1",
      "date": "2025-09-28",
      "changes": "Added scientific jargon category, removed outdated terms"
    }
  ]
}
```

#### Backup and Rollback

Keep versioned backups:
- `master_prohibited_words_v2.0.json`
- `master_prohibited_words_v2.1.json`

## Custom Phase Development

For projects requiring specialized processing beyond the standard 10 phases (plus optional phases 6.1 and 9.5).

### Creating Custom Phases

#### Phase Template Structure

```json
{
  "phase_name": "Custom Phase Name",
  "version": "1.0",
  "dependencies": ["master_prohibited_words.json"],
  "domain": "Specific processing domain",
  "prompt": {
    "system_message": "Your custom prompt here...",
    "instructions": [
      "Specific instruction 1",
      "Specific instruction 2"
    ],
    "never_touch": [
      "Domain 1 handled by other phases",
      "Domain 2 to preserve"
    ]
  },
  "assembly_line_position": "After Phase X, before Phase Y",
  "temperature_recommendation": 0.5,
  "model_recommendation": "claude-3-5-sonnet"
}
```

#### Example Custom Phase: Genre-Specific Enhancement

```json
{
  "phase_name": "Sci-Fi Technical Enhancement",
  "version": "1.0",
  "dependencies": ["master_prohibited_words.json", "scifi_terminology.json"],
  "domain": "Science fiction technical accuracy and authenticity",
  "prompt": {
    "system_message": "You are a science fiction technical consultant. Enhance technical descriptions for authenticity without changing dialogue or narrative structure.",
    "instructions": [
      "Replace vague technical terms with specific alternatives",
      "Add realistic technical constraints and limitations",
      "Ensure scientific plausibility where possible",
      "Maintain consistency with established technology"
    ],
    "never_touch": [
      "Character dialogue (Phase 6 handles this)",
      "Grammar corrections (Phase 1 handles this)",
      "Overall prose style"
    ]
  },
  "assembly_line_position": "After Phase 4 (Sensory Enhancement), before Phase 5 (Subtlety Creation)",
  "temperature_recommendation": 0.4,
  "model_recommendation": "claude-opus"
}
```

### Integration with Main Pipeline

#### Sequential Integration

Insert custom phases at appropriate points:

```
Phase 1 → Phase 2 → Phase 3 → Phase 4 → Custom Phase → Phase 5 → ...
```

#### Parallel Processing

Some custom phases can run in parallel:

```
Main Pipeline:     Phase 1 → Phase 2 → Phase 3 → ...
Parallel Custom:   Custom Analysis Phase → Results Integration
```

## Project-Specific Configurations

### Configuration File Structure

Create project-specific config files:

```json
{
  "project_name": "Your Project Name",
  "version": "1.0",
  "configuration": {
    "enabled_phases": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "optional_phases": [6.1, 9.5],
    "custom_phases": ["scifi_technical"],
    "character_dialogue_enabled": true,
    "master_prohibited_words": "custom_prohibited_words.json",
    "model_preferences": {
      "primary": "anthropic",
      "budget_mode": false,
      "quality_threshold": 95
    }
  },
  "character_specifications": {
    // Your character definitions here
  },
  "project_specific_terms": {
    "avoid": ["term1", "term2"],
    "preserve": ["technical_term1", "proper_noun1"]
  }
}
```

### Genre-Specific Configurations

#### Fantasy Configuration

```json
{
  "genre": "fantasy",
  "special_considerations": {
    "archaic_language_preservation": true,
    "magical_terminology_consistency": true,
    "world_building_terms": ["realm", "kingdom", "magic"]
  },
  "custom_phases": ["fantasy_consistency_check"],
  "character_voice_complexity": "high"
}
```

#### Technical Writing Configuration

```json
{
  "genre": "technical_documentation",
  "special_considerations": {
    "precision_over_style": true,
    "preserve_technical_accuracy": true,
    "formal_tone_maintenance": true
  },
  "enabled_phases": [1, 2, 7, 9, 10],  // Skip creative enhancement phases
  "model_preferences": {
    "temperature_override": 0.1,
    "consistency_priority": true
  }
}
```

## Advanced Workflow Customization

### Conditional Processing

Process different content types with different phase combinations:

```python
def get_phase_configuration(content_type, text_analysis):
    if content_type == "dialogue_heavy":
        return {
            "phases": [1, 2, 6, 6.1, 7, 9, 10],
            "character_focus": True,
            "skip_9_5": True  # Skip statistical analysis for dialogue-focused content
        }
    elif content_type == "technical_description":
        return {
            "phases": [1, 2, 3, 7, 9, 10],
            "preserve_precision": True,
            "skip_9_5": True  # Skip statistical analysis for technical content
        }
    elif content_type == "creative_narrative":
        return {
            "phases": [1, 2, 3, 4, 5, 8, 9, 9.5, 10],
            "enhance_creativity": True,
            "include_9_5": True  # Include statistical analysis for creative content
        }
    else:
        return {
            "phases": list(range(1, 11)),  # Full pipeline phases 1-10
            "optional_phases": [9.5],  # Optional statistical analysis
            "standard_processing": True
        }
```

### Quality-Based Iteration

Automatically retry phases based on quality metrics:

```python
def quality_based_processing(text, target_quality=95):
    current_text = text
    quality_score = 0
    iteration = 0
    max_iterations = 3

    while quality_score < target_quality and iteration < max_iterations:
        current_text = process_full_pipeline(current_text)
        quality_score = assess_quality(current_text)
        iteration += 1

        if quality_score < target_quality:
            # Adjust processing parameters
            adjust_parameters_for_quality(quality_score)

    return current_text, quality_score
```

### Multi-Pass Processing

Some content benefits from multiple passes through specific phases:

```python
def multi_pass_processing(text):
    # First pass: Full pipeline
    result = process_standard_pipeline(text)

    # Second pass: Focus on dialogue refinement
    if has_dialogue(result):
        result = process_phase_6_enhanced(result)

    # Third pass: Final polish
    result = process_phases([8, 9], result)

    return result
```

### Content-Aware Processing

Analyze content to determine optimal processing approach:

```python
def analyze_content_needs(text):
    analysis = {
        "dialogue_percentage": calculate_dialogue_ratio(text),
        "technical_content": detect_technical_language(text),
        "creativity_level": assess_creative_content(text),
        "ai_detection_risk": initial_ai_detection_scan(text)
    }

    recommendations = {
        "use_character_phase": analysis["dialogue_percentage"] > 0.3,
        "skip_creative_phases": analysis["technical_content"] > 0.7,
        "extra_polish_needed": analysis["ai_detection_risk"] > 0.8
    }

    return analysis, recommendations
```

---

For basic usage instructions, see the [Usage Guide](USAGE_GUIDE.md).
For technical implementation details, see the [Technical Reference](TECHNICAL_REFERENCE.md).