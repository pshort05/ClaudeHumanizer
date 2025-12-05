# AI BANNED Construction Analysis - Quick Reference

## THREE CRITICAL QUESTIONS ANSWERED

### 1) Do They Add Anything to the Existing Structure?

**ANSWER: YES - Significant Gap Identified**

**Current Coverage**: ~40% (14 of 29 patterns partially covered)
- 12 patterns already in Master List (Phase 2)
- 6 patterns implicitly handled across multiple phases
- **7 critical patterns NOT covered by ANY phase**

**The Gap**: No existing phase targets **syntactic construction patterns** as a primary domain

**Why it matters**:
- These 29 patterns represent an entirely new detection category
- They're syntactically correct (Phase 1 won't catch them)
- They're not vocabulary problems (Phase 2 won't catch them)
- They're about structure, not density (distinct from Phase 3)
- They're about mechanical repetition, not sensory details (distinct from Phase 4)

**Critical Missing Patterns** (not covered anywhere):
1. Anthropomorphized Silence ("silence stretches," "silence hangs")
2. Echo-Line Poetics (parallel structure repetition)
3. Mood-Prop Negation ("grabbed the thing he didn't need")
4. Meta-Narrative Intrusion ("this was the moment")
5. Atmospheric Front-Loading (setting before character)
6. Hollow Restraint ("held it together," "swallowed it down")
7. False Range Construction ("from X to Y" with non-comparable scales)

---

### 2) Does the Rule Make Sense?

**ANSWER: YES - Exceptionally Strong Alignment**

**Core Principle Match**:
- AI BANNED Construction: "Every construction substitutes form for content"
- ClaudeHumanizer: "Eliminate AI detection markers while preserving meaning"
- **Result**: Perfect philosophical alignment

**Quality of Rules**:
✓ All 29 patterns have clear trigger phrases
✓ All have explicit "why it fails" explanations
✓ All include concrete good/bad examples
✓ All specify fix strategies
✓ All are mechanically detectable

**Humanness Test**:
- Humans naturally avoid these patterns (rarely write this way)
- AI consistently produces these patterns (algorithmic defaults)
- Fix strategies don't introduce new problems
- No contradictions between patterns

**Genre Considerations** (important caveat):
- Literary fiction: Some patterns (echo-line poetics, anthropomorphized silence) may be intentional stylistic choices
- Commercial fiction/erotica: All patterns should be minimized
- Expository writing: Apply all rules strictly

**Verdict**: Rules make strong sense with appropriate context awareness

---

### 3) Where Should These Rules Go?

## RECOMMENDATION: CREATE PHASE 8.5 ✓✓✓ PRIMARY

**Phase Name**: "Structural Construction Elimination"

**Position in Pipeline**:
```
Phase 8 (Strategic Imperfections)
    ↓
Phase 8.5 (Structural Construction Elimination) ← NEW
    ↓
Phase 9 (AI Pattern Detection)
    ↓
Phase 9.5 (Statistical Analysis - optional)
    ↓
Phase 10 (Final Word Sweep)
```

### Why Phase 8.5 is Best:

| Criterion | Phase 8.5 | Enhance Phase 3 | Enhance Phase 7 | Enhance Phase 9 |
|-----------|-----------|---|---|---|
| Coverage | 100% (29/29) | 48% (14/29) | 28% (8/29) | 40% (12/29) |
| Domain Isolation | Perfect | Some scope creep | Incomplete | Confusing |
| Architecture Fit | Excellent | Good | Poor | Poor |
| Development Time | 8 hrs | 4 hrs | 3 hrs | 5 hrs |
| Maintenance | Excellent | Good | Poor | Confusing |

### Phase 8.5 Characteristics:

**Domain**: Syntactic/structural patterns that simulate depth/emotion/tension without creating actual content

**Input**: Text from Phase 8 (Strategic Imperfections)

**Output**: Restructured prose with mechanical patterns eliminated

**Examples of Fixes**:
- `"The silence stretched between them"` → Show WHO breaks silence, not the silence's action
- `"She grabbed the soy sauce she didn't need"` → Either remove the action OR name why she needs it
- `"Not angry, but resigned"` → Commit to ONE emotional state and show it through action
- `"Something flickered in his expression"` → Name the actual expression/emotion
- `"He stands, then sits"` → Show consequence of the transition, not choreography
- `"The New York skyline glowed..."` → Start with character/action, not setting

**Never Modifies**:
- Dialogue (preserved exactly)
- Markdown formatting (preserved exactly)
- Character voice/style (enhanced, not changed)
- Work from previous phases (builds on it)

---

## IMPLEMENTATION ROADMAP

### Phase 8.5 Template Structure:

```json
{
  "title": "Structural Construction Elimination",
  "version": "1.0.0",
  "date": "YYYY-MM-DD",
  "assembly_line_position": "Phase 8.5: Syntactic Structure Cleanup",
  "description": "Eliminate mechanical/robotic syntactic patterns that simulate depth/emotion without creating it",
  "domain_restrictions": {
    "only_handle": [
      "Syntactic/structural patterns",
      "Mechanical repetition patterns",
      "Narrative mechanics intrusion",
      "False emotional shorthand"
    ],
    "never_touch": [
      "Dialogue content",
      "Markdown formatting",
      "Character voice",
      "Grammar (Phase 1 domain)",
      "Vocabulary (Phases 2/10 domain)",
      "Sensory details (Phase 4 domain)"
    ]
  },
  "detection_frameworks": {
    "anthropomorphized_silence": {...},
    "echo_line_poetics": {...},
    "mood_prop_negation": {...},
    "meta_narrative_intrusion": {...},
    "atmospheric_front_loading": {...},
    "hollow_restraint": {...},
    "false_range_construction": {...},
    "sequential_action_pairs": {...},
    "vague_interiority": {...},
    "standalone_because_fragments": {...},
    "blank_desire_statements": {...},
    "aestheticized_damage": {...},
    "misapplied_epic_tone": {...},
    "negative_parallelism": {...}
  },
  "output_format": {...}
}
```

### Development Path:

1. **Copy PROMPT_TEMPLATE.json** as starting point
2. **Add 29 patterns** from AI BANNED Construction document
3. **Create detection rules** for each pattern (using quick-scan table)
4. **Add fix examples** for each pattern
5. **Test on sample texts** (especially erotica/romance - heavy users of these patterns)
6. **Validate** with existing pipeline (ensure Phase 8→8.5→9 flow works)
7. **Document** in CHANGELOG.md, CLAUDE.md, USAGE_GUIDE.md

**Estimated Effort**: 8-10 hours

---

## ALTERNATIVE: Enhance Phase 3 (Simpler but Incomplete)

If creating a new phase is problematic:

**Add subsection to Phase 3**: "Structural Construction Patterns"

**Coverage**: 14 of 29 patterns that fit Phase 3's "overwritten language" domain:
- Triple-Beat Lists
- Echo-Line Poetics
- Blank Desire Statements
- Aestheticized Damage
- Misapplied Epic Tone
- Atmospheric Front-Loading
- Meta-Narrative Intrusion
- Sequential Action Pairs
- Vague Interiority
- Hollow Restraint
- Standalone "Because"
- Mood-Prop Negation
- False Range Construction
- Negative Parallelism

**Remaining 15 patterns** distributed to:
- Phase 5: 3 patterns (Subtlety domain)
- Phase 7: 4 patterns (Weak language domain)
- Phase 9: 5 patterns (AI pattern domain)
- Master List: 3 patterns (Word-level)

**Effort**: 4 hours
**Coverage**: 48%
**Result**: Incomplete but still valuable

---

## SUMMARY

| Question | Answer | Status |
|----------|--------|--------|
| Do they add value? | YES - Major gap identified | ✓ CONFIRMED |
| Do the rules make sense? | YES - Exceptional alignment | ✓ CONFIRMED |
| Where should they go? | **Phase 8.5 (PRIMARY)** or Phase 3 (SECONDARY) | ✓ RECOMMENDED |

---

## FILES CREATED

1. **BANNED_CONSTRUCTION_ANALYSIS.md** (527 lines)
   - Comprehensive analysis of all 29 patterns
   - Pattern-by-pattern coverage mapping
   - Decision matrix with implementation options
   - Detailed integration recommendations
   - Coverage analysis by existing phase

2. **BANNED_CONSTRUCTION_QUICK_REFERENCE.md** (this file)
   - Executive summary
   - Three critical questions answered
   - Implementation roadmap
   - Alternative approaches

---

## RECOMMENDED NEXT STEPS

### If Going with Phase 8.5:
1. Read full BANNED_CONSTRUCTION_ANALYSIS.md
2. Create PROMPT_TEMPLATE.json-based Phase 8.5
3. Test with sample texts (especially long texts and erotica)
4. Update documentation
5. Run through full pipeline validation

### If Going with Phase 3 Enhancement:
1. Read Phase 3 section of BANNED_CONSTRUCTION_ANALYSIS.md
2. Add "Structural Construction Patterns" subsection to Phase 3
3. Test with focus on Phase 3's new rules
4. Distribute remaining 15 patterns to appropriate phases
5. Update documentation

---

**Analysis Date**: 2025-12-04
**Analyzed Document**: AI BANNED Construction.md
**Analysis Against**: ClaudeHumanizer v3.1.0
