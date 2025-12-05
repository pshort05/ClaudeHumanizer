# Master Prohibited Words Enhancement Plan

**Date**: 2025-12-04
**Version**: 2.0.0 (Proposed)
**Status**: Ready for Implementation
**Priority**: Critical gaps from BANNED_WORDS_ANALYSIS.md

---

## Overview

The BANNED_WORDS_ANALYSIS.md identified 56% coverage gaps in master_prohibited_words.json (v1.8.0). This document provides a structured plan to add 16 new pattern rule sections addressing the most critical gaps (Priority 1 - 0-20% current coverage).

**Current Status**: 158/360+ terms covered (44%)
**After Implementation**: ~298/360 terms covered (83%)
**New Terms to Add**: ~140 terms across 16 new sections

---

## Priority 1 - CRITICAL GAPS (0-20% Coverage)

These 14 sections have virtually no coverage and represent the most common AI-generated patterns.

### 1. Physical Tells Patterns (0% Coverage)

**Section Name**: `physical_tells_patterns`

**Description**: AI identifies emotions through physical reactions, but uses the same limited set of tells repeatedly. Humans show emotion more variably.

**Terms to Add** (20 terms):
- hands (trembling, shaking, clenching, flexing, whitening, curling, balling into fists, uncurling)
- breath (catching, hitching, stalling, hitched, shallow, ragged, held, released in a rush, short, quick)
- jaw (tightening, clenching, tensing, working, loosening)
- throat (tightening, constricting, tightens, constricts, closing)
- chest (tightens, aches, something cracks, shifts, loosens)
- stomach (clenching, twisting, flipping, dropping, sinking, tightening)

**Detection Rule**: Any physical reaction described with verbs like tightening, clenching, trembling, catching breath, etc. in emotional context.

**Replacement Strategy**:
- Preferred: Remove the description entirely and let action speak
- Alternative: Use specific action: "She gripped the edge of the table" instead of "Her hands trembled"
- Alternative: Describe the consequence, not the feeling: "He held his breath" instead of "His breath caught"

**Example**:
- Bad: "Her hands trembled, betraying her anxiety."
- Good: "She gripped her coffee cup. The liquid sloshed over the rim."

---

### 2. Emotion Intensifiers (14% Coverage)

**Section Name**: `emotion_intensifier_bans`

**Description**: AI uses paper-thin descriptors that "sound profound but mean nothing." These intensifiers appear in nearly every AI-generated passage.

**Terms to Add** (12 terms):
- visceral, primal
- paper-thin, gossamer-thin, razor-thin (always modifying control/patience/composure)
- threadbare, frayed edges, worn thin (same usage)
- stretched to breaking, worn down, stretched taut

**Detection Rule**: Any descriptor that adds intensity through texture/fragility language without specific evidence.

**Replacement Strategy**:
- Preferred: Remove the intensifier
- Alternative: Show what the emotion actually looks like in action
- Never: These descriptors with control-related nouns

**Example**:
- Bad: "His control was paper-thin, stretched to breaking."
- Good: "He hadn't slept. His hands shook slightly."

---

### 3. Transition/Beat Placeholders (13% Coverage)

**Section Name**: `transition_beat_placeholders`

**Description**: Mechanical delay tactics that interrupt action. Completely unnecessary and pure AI default.

**Terms to Add** (7 terms):
- "for a long moment", "for a beat", "for a suspended moment"
- "after a moment", "a pause then"
- Phrase pattern: "when [he/she] speaks, [his/her] voice is [adjective]"
- Phrase pattern: "the silence that follows is [adjective]"

**Detection Rule**: Any temporal/pause phrase between action beats designed to delay revelation.

**Replacement Strategy**:
- Preferred: Delete entirely and continue to next beat
- Alternative: Use one-word: "Silence." or "A pause."
- Never: Elaborate descriptions of delays

**Example**:
- Bad: "For a long moment, neither of them spoke. The silence that followed was heavy with implication."
- Good: "Silence. She waited for him to continue."

---

### 4. Gaze Descriptors (0% Coverage)

**Section Name**: `gaze_descriptors`

**Description**: These create the appearance of depth and communication without actual substance. Extremely common in AI.

**Terms to Add** (10 terms):
- Assessing, appraising, cataloguing, cataloging
- Tracking, watchful, guarded
- Shuttered, unreadable, inscrutable, illegible
- Too knowing, seeing too much
- Penetrating, measuring

**Detection Rule**: Any adjective describing eyes/gaze that implies knowledge or evaluation without showing evidence.

**Replacement Strategy**:
- Preferred: Remove and show what the look actually communicates through dialogue or action
- Alternative: Use specific emotion: "His eyes narrowed" (shows something, not just labels it)
- Never: These abstract gaze descriptors

**Example**:
- Bad: "His gaze was too knowing, cataloguing every hesitation."
- Good: "His gaze didn't move from her face. 'You're lying.'"

---

### 5. Temperature Emotion Metaphors (25% Coverage)

**Section Name**: `temperature_emotion_bans`

**Description**: Temperature is "the most generic descriptor for emotion, narrowing emotional spectrum to two options: hot (angry/passionate) and cold (distant/afraid)."

**Terms to Add** (6 terms):
- Frozen (in position), ice in veins
- Warmth spread through [body], heat pooled low
- Heat between them, heat in the air
- Fire licked up spine, something molten
- Cold settled in bones

**Detection Rule**: Temperature metaphors applied to emotion or describe emotional shift.

**Replacement Strategy**:
- Preferred: Delete entirely
- Alternative: Show specific physical symptom that's NOT temperature: "His hands shook" instead of "Cold fear filled him"
- Never: Temperature metaphors for emotion

**Example**:
- Bad: "Cold dread settled in her bones as she read the letter."
- Good: "She read the letter twice. Three times. Her hands wouldn't stop shaking."

---

### 6. Breaking/Cracking Metaphors (13% Coverage)

**Section Name**: `breaking_cracking_metaphors`

**Description**: Every emotional shift becomes "something broke." No differentiation between different emotional states.

**Terms to Add** (7 terms):
- "something cracked open", "split open", "shattered"
- "broke something loose", "broke apart", "fractured"
- Phrases: "hairline fractures", "fault lines", "cracks in the foundation"
- "splintered", "shattered something fragile"

**Detection Rule**: Structural failure metaphors applied to emotional/psychological states.

**Replacement Strategy**:
- Preferred: Delete entirely
- Alternative: Show the specific consequence of the emotional shift: "She started crying" instead of "Something inside her broke"
- Never: Structural damage metaphors for emotion

**Example**:
- Bad: "Something inside him shattered at her words."
- Good: "Her words hit him like a punch. He had to sit down."

---

### 7. Anchor/Tether Metaphors (20% Coverage)

**Section Name**: `anchor_tether_metaphors`

**Description**: "Turns connection into passivity—something that happens rather than something chosen."

**Terms to Add** (4 terms):
- "tethered to", "the only thing keeping [grounded/present/sane]"
- "held in place", "moored", "anchored to"

**Detection Rule**: Anchor/tether metaphors implying someone is kept in place by another person or emotion.

**Replacement Strategy**:
- Preferred: Remove and show active choice
- Alternative: Show what the person does because of connection, not what keeps them in place
- Never: Anchor metaphors for relationships

**Example**:
- Bad: "She was the only thing keeping him grounded."
- Good: "When she left, he couldn't focus. Couldn't sleep. Nothing mattered until she came back."

---

### 8. Edge/Precipice Metaphors (0% Coverage)

**Section Name**: `edge_precipice_metaphors`

**Description**: Abstract geography substituting for specific psychological state.

**Terms to Add** (5 terms):
- "on the edge of something", "on the edge of breaking/crying/screaming"
- "teetering on the precipice", "one wrong word from [falling/breaking/shattering]"
- "barely holding on", "hanging by a thread"

**Detection Rule**: Any edge/height/falling language describing emotional state.

**Replacement Strategy**:
- Preferred: Delete entirely
- Alternative: Show what happens when the precipice is reached: concrete action/consequence
- Never: Metaphorical ledges for emotion

**Example**:
- Bad: "He was teetering on the edge of losing control."
- Good: "He opened his mouth. Closed it. Stood up and walked to the window without speaking."

---

### 9. Time/Moment Suspension Phrases (17% Coverage)

**Section Name**: `time_moment_phrases`

**Description**: "Evokes camera, not consciousness. Tells when to feel tension rather than creating it."

**Terms to Add** (5 terms):
- "time stretched", "suspended in amber", "crystallized"
- "frozen in place", "the world narrowed to"
- "everything else fell away", "the world held its breath"

**Detection Rule**: Any phrase suggesting time suspension or world-narrowing in emotional context.

**Replacement Strategy**:
- Preferred: Delete and let the moment stand on its own
- Alternative: Show what the character actually does/feels, not the metaphysical state
- Never: Narrative intrusion suggesting time suspension

**Example**:
- Bad: "Time seemed to suspend as their eyes met. The world fell away."
- Good: "She looked up. He was watching her. Neither moved."

---

### 10. Permission/Allowance Constructions (0% Coverage)

**Section Name**: `permission_allowance_patterns`

**Description**: "Labels release rather than showing what changes when restraint drops."

**Terms to Add** (5 terms):
- "allowed [himself/herself] to [verb]"
- "let [himself/herself] [verb]", "permitted [himself/herself] the luxury of"
- "gave [himself/herself] permission to", "finally let go of"

**Detection Rule**: Any sentence structure using "allowed/let/permitted + self + action" in emotional context.

**Replacement Strategy**:
- Preferred: Delete the permission framing, just show the action
- Alternative: Show consequence of the restraint being released
- Never: These self-permission constructions

**Example**:
- Bad: "She allowed herself to cry for the first time."
- Good: "She cried. Actually cried, shoulders shaking, face in her hands."

---

### 11. Realization/Understanding Tells (17% Coverage)

**Section Name**: `realization_understanding_patterns`

**Description**: "Tells that realization happened rather than showing thought process or consequence."

**Terms to Add** (5 terms):
- "it clicked into place", "pieces slotted together"
- "clarity crashed over", "truth settled", "landed with the force of"
- "crystallized" (used for realization specifically)

**Detection Rule**: Any phrase suggesting sudden understanding or realization without showing what was understood.

**Replacement Strategy**:
- Preferred: Delete and show the understanding through dialogue or action
- Alternative: Show what changes after understanding
- Never: These sudden-realization phrases

**Example**:
- Bad: "Suddenly, clarity crashed over her. She understood everything."
- Good: "She read the letter again. Oh. Oh god. He'd never told her any of it."

---

### 12. Danger/Threat Descriptors (0% Coverage)

**Section Name**: `danger_threat_descriptors`

**Description**: "Every dangerous character gets same predator-animal vocabulary. No differentiation."

**Terms to Add** (8 terms):
- "lethal grace", "lethal smile", "lethal efficiency"
- "predatory stillness", "coiled to strike", "dangerous edge"
- "barely contained violence", "quiet menace", "soft threat"
- "the promise of violence", "menacing", "menacingly"

**Detection Rule**: Predator/animal danger vocabulary applied to character descriptions.

**Replacement Strategy**:
- Preferred: Delete entirely
- Alternative: Show dangerous behavior through action, not descriptor
- Never: These predator/animal threat terms

**Example**:
- Bad: "He moved with lethal grace, predatory stillness in every line."
- Good: "He didn't move. Just watched her. She had the sudden sense that if she ran, he'd catch her."

---

### 13. Possession/Claiming Phrases (0% Coverage)

**Section Name**: `possession_claiming_phrases`

**Description**: "Same branding metaphor for every intense connection. No differentiation."

**Terms to Add** (5 terms):
- "staked a claim", "marked [him/her]", "claimed [him/her]"
- "branded into", "written into skin", "carved into bones"
- "imprinted on"

**Detection Rule**: Ownership/branding metaphors applied to relationships or emotional states.

**Replacement Strategy**:
- Preferred: Delete entirely
- Alternative: Show what the character actually does/thinks because of the connection
- Never: These possession metaphors

**Example**:
- Bad: "He'd branded her into his very bones."
- Good: "Every smell reminded him of her. Every song on the radio. He couldn't escape her."

---

### 14. Religious Exclamations (0% Coverage)

**Section Name**: `religious_exclamations`

**Description**: "Reflexive intensity markers that tell nothing about character. Universal default."

**Terms to Add** (6 terms):
- "Oh God", "Oh my God", "God yes", "God no"
- "Jesus", "Christ", "Lord" (when used as exclamation)

**Detection Rule**: Religious terms used as exclamations in emotional moments.

**Replacement Strategy**:
- Preferred: Delete entirely
- Alternative: Use specific to character voice/background
- Alternative: Show what triggers the exclamation through action
- Never: Generic religious exclamations

**Example**:
- Bad: "'Oh God, I can't—' she gasped."
- Good: "She gasped. 'I can't. Please, I can't.'"

---

### 15. Ending Clichés (0% Coverage)

**Section Name**: `ending_cliches`

**Description**: "Summary posing as closure. Labels emotional meaning rather than letting it emerge."

**Terms to Add** (5 terms):
- "And for now, that was enough"
- "It was a start", "They would figure it out. Somehow."
- "Nothing would ever be the same", "Everything had changed"

**Detection Rule**: Final summary lines that label emotional impact rather than showing it.

**Replacement Strategy**:
- Preferred: Delete entirely
- Alternative: Let the last action/dialogue speak for itself
- Never: Summary closures
- Never: "that was enough" constructions

**Example**:
- Bad: "They stood together in the dark. And for now, that was enough."
- Good: "They stood together in the dark."

---

### 16. Description Clichés (20% Coverage)

**Section Name**: `description_cliches`

**Description**: "So common they're invisible. Create no specific visual impression."

**Terms to Add** (8 terms):
- "orbs" (for eyes), "pools" (for eyes), "mane" (for hair)
- "column of neck", "delicate wrists"
- "the line of jaw", "broad shoulders", "lean muscle"
- "sharp planes", "high cheekbones"

**Detection Rule**: Formulaic descriptor clichés that appear identically in thousands of stories.

**Replacement Strategy**:
- Preferred: Delete and describe specific physical detail unique to character
- Alternative: Use individual feature: "dark eyes" instead of "pools of darkness"
- Never: These cliché descriptors

**Example**:
- Bad: "His sharp planes and lean muscle were a study in controlled power."
- Good: "He'd lost weight. The scar on his cheekbone was more visible now."

---

## Priority 2 - HIGH PRIORITY GAPS (21-50% Coverage)

These 2 sections have significant gaps that should be addressed in Phase 2 of implementation:

### 17. Dialogue Tag Bans (40% Coverage)

**Section Name**: `dialogue_tag_bans` (expand existing)

**Terms to Add** (9 terms):
- Voice adverbs: softly, quietly, carefully, flatly, evenly, roughly, harshly
- Voice verbs: drops, tightens, goes flat, breaks, hardens, softens
- Phrase patterns: "pitched low", "barely above a whisper"
- Qualifiers: "deceptively soft/mild", "deliberately light", "falsely casual", "too casual"

**Implementation Note**: This can be added to existing dialogue_pause_pattern_rules section or created separately.

---

### 18. Competence Porn Descriptors (33% Coverage)

**Section Name**: `competence_porn` (expand existing)

**Terms to Add** (6 terms):
- "graceful economy" (of movement), "wasted no movement"
- "efficient brutality", "quiet competence"
- "easy confidence", "contained power"
- "coiled energy", "deceptive stillness"

**Implementation Note**: Expand existing section if present, or create new section.

---

## Implementation Timeline

### Phase 1 (IMMEDIATE - v2.0.0)
Add all 16 Critical Gap sections from Priority 1 above.
- Sections: 1-16
- Terms: ~140
- Expected coverage: 83%+

### Phase 2 (NEXT UPDATE)
Expand existing sections with Priority 2 gaps
- Sections: 17-18
- Terms: ~15
- Final expected coverage: 87%+

### Phase 3 (FUTURE)
Content-type specific patterns (romance, erotica-specific terms from Part 4 of BANNED document)

---

## JSON Structure Template

For consistency with existing master_prohibited_words.json, each new section should follow this template:

```json
"section_name": {
  "description": "What this pattern addresses and why it matters",
  "detection_rule": "How to identify instances of this pattern",
  "common_ai_patterns": [
    "specific pattern 1",
    "specific pattern 2",
    "phrase pattern with *"
  ],
  "allowed_replacements_only": [
    "replacement option 1",
    "replacement option 2",
    "[Delete entirely if not essential]"
  ],
  "replacement_strategy": {
    "preferred": "Best approach",
    "simple_alternative": "Second option",
    "never_use": "What not to do"
  },
  "examples": {
    "bad_ai_writing": [
      "Example of pattern in bad writing"
    ],
    "good_human_writing": [
      "Example of good alternative"
    ]
  },
  "pattern_matching_instruction": "Specific instruction for detection"
}
```

---

## Version Update

**From**: v1.8.0 (158 terms covered)
**To**: v2.0.0 (298+ terms covered)
**Change Type**: MAJOR (significant expansion)

### Version Notes
- Added 16 new pattern rule sections
- ~140 new terms/phrases
- Coverage increased from 44% to 83%+
- Updated date: 2025-12-04
- All sections follow standardized JSON structure
- Backward compatible (no existing terms removed)

---

## Benefits

✅ **Coverage**: Increases from 44% to 83%
✅ **AI Detection**: Catches 39% more common AI patterns
✅ **Consistency**: All 16 patterns have standardized documentation
✅ **Usability**: Each section includes examples, detection rules, and replacement strategies
✅ **Maintainability**: Follows existing structural patterns in master list

---

## Integration Notes

- This enhancement should be coordinated with Phase 8.5 (structural patterns) and Phase 2/10 (word filtering)
- Phase 2 and Phase 10 will benefit most from these additions
- Consider combining Phase 8.5 and updated master list for maximum effect
- Test with BANNED document sample text to verify coverage

---

**Status**: Ready for implementation
**Next Step**: Integrate into master_prohibited_words.json v2.0.0

