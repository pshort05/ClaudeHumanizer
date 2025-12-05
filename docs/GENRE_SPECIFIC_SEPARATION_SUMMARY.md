# Genre-Specific Word Lists - Separation Complete

**Date**: 2025-12-04
**Status**: ✓ Complete
**Impact**: Master prohibited words list restructured with optional genre-specific lists

---

## Overview

Romance and erotica-specific word patterns have been separated from the master prohibited words list into dedicated, optional genre-specific lists. This allows authors to choose whether genre-specific filtering applies to their content.

---

## What Changed

### 1. Three Separate Lists (instead of one monolithic list)

**master_prohibited_words.json** (REQUIRED - Core List)
- Version: 2.1.0
- Size: 83 KB
- Sections: 27 (core patterns)
- Coverage: 83%+ (core patterns only)
- Includes:
  - prohibited_single_words
  - prohibited_multi_word_phrases
  - contextual_patterns
  - dialogue_pause_pattern_rules
  - dialogue_tag_bans (22 patterns)
  - light_description_pattern_rules
  - finger_hand_action_pattern_rules
  - physical_tells_patterns
  - emotion_intensifier_bans
  - transition_beat_placeholders
  - gaze_descriptors
  - temperature_emotion_bans
  - breaking_cracking_metaphors
  - anchor_tether_metaphors
  - edge_precipice_metaphors
  - time_moment_phrases
  - permission_allowance_patterns
  - realization_understanding_patterns
  - danger_threat_descriptors
  - possession_claiming_phrases
  - religious_exclamations
  - ending_cliches
  - description_cliches
  - And 4 additional pattern sections

**master_prohibited_words_romance.json** (OPTIONAL - Genre-Specific)
- Version: 1.0.0
- Size: 4.9 KB
- Patterns: 41 (genre-specific for romance)
- Usage: Include ONLY when author indicates romance fiction and requests genre-specific filtering
- Contains:
  - romance_specific_bans section with:
    - Emotional escalation patterns: "need crashed over", "need unfurled", "want *ed through"
    - Attraction clichés: "chemistry between", "electricity *", "drawn to like"
    - Vulnerability patterns: "walls crumbled", "defenses crumbling"
    - Possession language: "she was his", "completion with"
    - Generic emotional states: "couldn't deny anymore", "changed everything"

**master_prohibited_words_erotica.json** (OPTIONAL - Genre-Specific)
- Version: 1.0.0
- Size: 5.8 KB
- Patterns: 50 (genre-specific for erotica)
- Usage: Include ONLY when author indicates erotica/explicit content and requests genre-specific filtering
- Contains:
  - erotica_specific_bans section with:
    - Generic sensation: "heat pooled", "wetness *", "throbbing *"
    - Euphemism overload: "core ached", "inner walls", "velvety", "silken"
    - Mechanical verbs: "thrust", "plunged", "buried", "drove", "sheathed"
    - Emotional distance: "felt * watching", "couldn't help", "nothing else mattered"

---

## Why This Change?

### Benefits of Separation

1. **Author Control**: Writers can opt-in to genre-specific filtering rather than having it applied automatically
2. **Core + Optional Model**: Essential patterns (dialogue tag bans) are always included; genre-specific patterns are optional
3. **Clarity**: Obvious when a pattern is genre-specific vs. universally applicable
4. **Flexibility**: Authors can choose to use master list only, or add genre-specific lists based on their content
5. **Reduced False Positives**: Non-romance/non-erotica content won't be incorrectly filtered for genre-specific patterns

### Decision Framework

- **Always Use**: master_prohibited_words.json (required for all content)
- **Use Only When**:
  - master_prohibited_words_romance.json → Author writes romance AND requests genre-specific filtering
  - master_prohibited_words_erotica.json → Author writes erotica AND requests genre-specific filtering

---

## Phase 10 Updates

Phase 10 (Final AI Word Sweep) has been updated to reflect this optional model.

### Key Changes to Phase 10

**Version**: 3.0.0 → 3.1.0
**Date**: 2025-10-26 → 2025-12-04

**New Sections Added**:
1. `optional_genre_specific_lists` - Documents when each optional list should be included
2. `critical_author_choice_note` - Emphasizes that optional lists are author-selected
3. Updated `master_list_integration` with:
   - `required_reference_file`: master_prohibited_words.json
   - `optional_reference_files`: Lists for romance and erotica (conditional)
   - `author_choice_requirement`: Critical instruction that optional lists only included with explicit author request

**Processing Steps Updated**:
- **step_0** (NEW): Determine which word lists to use based on author input
- **step_2**: Scan using master_prohibited_words.json (REQUIRED)
- **step_3** (NEW): IF author selected romance filtering → also scan master_prohibited_words_romance.json
- **step_4** (NEW): IF author selected erotica filtering → also scan master_prohibited_words_erotica.json

---

## Usage Guidance for Phase 10

### When to Include Each List

**master_prohibited_words.json (ALWAYS)**
- Every document
- All genres
- All content types

**master_prohibited_words_romance.json (OPTIONAL - Author Choice)**
- Include if: Author indicates content is romance fiction (contemporary, paranormal, historical, etc.)
- Include if: Author explicitly requests genre-specific pattern detection
- Skip if: Author has not indicated romance fiction
- Skip if: Author prefers not to use genre-specific filtering

**master_prohibited_words_erotica.json (OPTIONAL - Author Choice)**
- Include if: Author indicates content is erotica or explicit sexual content
- Include if: Author explicitly requests genre-specific pattern detection
- Skip if: Author has not indicated erotica content
- Skip if: Author prefers not to use genre-specific filtering

---

## File Structure Overview

```
/home/paul/Dropbox/Writing/ClaudeHumanizer/
├── master_prohibited_words.json (required, 83KB)
├── master_prohibited_words_romance.json (optional, 4.9KB)
├── master_prohibited_words_erotica.json (optional, 5.8KB)
├── 10_final_ai_word_sweep.json (updated to v3.1.0)
└── [other phase files...]
```

---

## Validation Results

✓ All three lists created successfully
✓ Romance sections removed from master list
✓ Erotica sections removed from master list
✓ Genre-specific lists properly structured with metadata
✓ Phase 10 updated with conditional processing
✓ JSON validation: PASSED
✓ All lists properly formatted and valid

---

## Impact on Processing

### Before This Change
- Master list included all patterns (core + genre-specific)
- All romance and erotica patterns applied to all content
- No author control over genre-specific filtering

### After This Change
- Master list contains only core patterns (dialogue tag bans + other universal patterns)
- Romance patterns applied ONLY if author indicates romance content
- Erotica patterns applied ONLY if author indicates erotica content
- Author has explicit control over which optional lists are used

---

## Backwards Compatibility

⚠️ **Note**: This is a structural change to how lists are organized:
- Phase 2 (AI Word Cleaning) may need to be updated to reference all three lists
- Phase 10 has been updated to handle conditional inclusion
- Documentation should reflect optional nature of genre-specific lists

---

## Next Steps

### For Phase 2 Integration (Optional Future Work)
Phase 2 (AI Word Cleaning) may benefit from similar optional list references:
- Include master_prohibited_words.json (required)
- Include genre-specific lists based on author preference

### For Documentation Updates
- Update USAGE_GUIDE.md with information about optional genre-specific lists
- Update README.md to document three-list model
- Create author guidance on choosing genre-specific filtering

---

## Summary

Romance and erotica-specific prohibited words are now in separate, optional lists:
- **master_prohibited_words_romance.json**: 41 patterns for romance fiction
- **master_prohibited_words_erotica.json**: 50 patterns for erotica content

Authors can choose whether to apply genre-specific filtering through Phase 10's conditional processing. The core master list continues to apply to all content, ensuring consistent removal of universal AI patterns.

**Status**: ✓ Complete and validated
