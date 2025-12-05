# AI BANNED Construction.md - Analysis & Integration Recommendations

**Document Analysis Date**: 2025-12-04
**Analyzed Against**: ClaudeHumanizer v3.1.0 (Phases 1-10, plus 6.1 and 9.5)

---

## EXECUTIVE SUMMARY

**Finding**: "AI BANNED Construction.md" identifies 29 high-value syntactic and structural patterns that are **currently underrepresented** in the existing ClaudeHumanizer system.

**Current Coverage**: ✓ Partial (~40% coverage)
- Most patterns are implicitly addressed across multiple phases
- Few patterns have explicit, dedicated detection rules
- Critical gap: no phase explicitly targets **structural construction patterns** as primary domain

**Recommendation**: **ADD as Phase 8.5 (or enhance Phase 3/7)** - These patterns warrant dedicated phase treatment due to their:
1. **High detectability** by AI detectors
2. **Cross-phase signature** (appear in many phases as secondary concerns)
3. **Mechanical nature** (easily automated to detect and fix)
4. **Human variation** (humans rarely use these patterns; AI defaults to them)

---

## PART 1: PATTERN-BY-PATTERN ANALYSIS

### INVENTORY OF 29 PATTERNS FROM "AI BANNED CONSTRUCTION"

| Pattern | Current Coverage | Where Handled | Recommendation |
|---------|------------------|---|---|
| 1.1 Sequential Action Pairs (", then") | ⚠️ Implicit | Phase 8 (rhythm) | **Elevate to explicit** |
| 1.2 Vague Interiority ("something shifts") | ✓ Partial | Phase 5 (subtlety) | Add to Phase 5 examples |
| 1.3 Anthropomorphized Silence | ❌ Missing | None | **Add new rule** |
| 1.4 Negation Formula ("not X, but Y") | ✓ Explicit | Phase 7 (weak language) | Already covered |
| 1.5 Triple-Beat Lists | ⚠️ Implicit | Phase 3 (purple prose) | Add to Phase 3 |
| 1.6 Staccato Verb Fragments | ✓ Explicit | Phase 8 (strategic imperfections) | Already covered |
| 1.7 Conjunction Starts (And/But) | ✓ Explicit | Phase 8 (rhythm variation) | Already covered |
| 1.8 Standalone "Because" Fragments | ⚠️ Implicit | Phase 5/7 | **Needs explicit rule** |
| 1.9 Hedged Reactions ("isn't quite") | ✓ Explicit | Master list + Phase 2 | Already covered |
| 1.10 Echo-Line Poetics | ❌ Missing | None | **Add new rule** |
| 1.11 Mood-Prop Negation | ❌ Missing | None | **Add new rule** |
| 1.12 Meta-Narrative Intrusion | ❌ Missing | None | **Add new rule** |
| 1.13 Atmospheric Front-Loading | ❌ Missing | None | **Add new rule** |
| 1.14 Gravitational Metaphors | ✓ Master List | Phase 2 (master list) | Already covered |
| 1.15 Suspension Phrases ("hangs") | ✓ Master List | Phase 2 (master list) | Already covered |
| 1.16 Impact Similes ("like a blow") | ✓ Master List | Phase 2 (master list) | Already covered |
| 1.17 Ripple/Stillness Similes | ✓ Master List | Phase 2 (master list) | Already covered |
| 1.18 Precision/Control Cluster | ✓ Master List | Phase 2 (master list) | Already covered |
| 1.19 Quality/Texture Defaults ("steel/velvet") | ✓ Master List | Phase 2 (master list) | Already covered |
| 1.20 Blank Desire Statements | ⚠️ Implicit | Phase 5 (subtlety) | Add explicit examples |
| 1.21 Articulation by Proxy ("a look that said") | ✓ Master List | Phase 2 (master list) | Already covered |
| 1.22 Hollow Restraint ("held it together") | ❌ Missing | None | **Add new rule** |
| 1.23 Aestheticized Damage | ⚠️ Implicit | Phase 3 (purple prose) | Add to Phase 3 |
| 1.24 Faux-Intellectual Aphorism | ✓ Explicit | Phase 7 (weak language) + Phase 9 (AI patterns) | Already covered |
| 1.25 Misapplied Epic Tone | ⚠️ Implicit | Phase 3 (purple prose) | Add to Phase 3 |
| 1.26 Elegant Variation | ✓ Explicit | Master list | Already covered |
| 1.27 False Range Construction | ❌ Missing | None | **Add new rule** |
| 1.28 Superficial Analysis as Narration | ✓ Explicit | Phase 9 (AI patterns) | Already covered |
| 1.29 Negative Parallelism | ⚠️ Implicit | Phase 7/9 | Add explicit rule |

---

## PART 2: COVERAGE ANALYSIS

### Missing Patterns (Require New Rules): 7 patterns
1. **Anthropomorphized Silence** - Critical catch (very AI-like)
2. **Echo-Line Poetics** - High value (easy to detect)
3. **Mood-Prop Negation** - Medium value (common in erotica)
4. **Meta-Narrative Intrusion** - High value (immersion breaker)
5. **Atmospheric Front-Loading** - Medium value (film language intrusion)
6. **Hollow Restraint** - High value (emotional vagueness)
7. **False Range Construction** - Medium value (promotional language)

### Implicit/Underrepresented Patterns (Need Elevation): 6 patterns
1. **Sequential Action Pairs** - Currently in Phase 8 as secondary; needs explicit detection rule
2. **Standalone "Because" Fragments** - Scattered across phases; needs dedicated section
3. **Blank Desire Statements** - In Phase 5 but needs more detailed examples
4. **Aestheticized Damage** - In Phase 3 but deserves dedicated subsection
5. **Misapplied Epic Tone** - Spread across Phase 3/9; needs clearer flagging criteria
6. **Negative Parallelism** - In Phase 7/9 but could be more explicit

### Already Well-Covered (12 patterns)
- Negation Formula ✓
- Staccato Verb Fragments ✓
- Conjunction Starts ✓
- Hedged Reactions ✓
- Gravitational Metaphors ✓
- Suspension Phrases ✓
- Impact Similes ✓
- Ripple/Stillness Similes ✓
- Precision/Control Cluster ✓
- Quality/Texture Defaults ✓
- Articulation by Proxy ✓
- Elegant Variation ✓
- Faux-Intellectual Aphorism ✓
- Superficial Analysis as Narration ✓

---

## PART 3: DECISION MATRIX

### Do These Patterns Add Value to Existing Structure?

**YES - Strong Value Add**

✓ **All 29 patterns are structurally different from existing Humanizer phases**

Current Humanizer phases handle:
- **Phase 1**: Grammar (rules-based)
- **Phase 2**: AI vocabulary (list-based)
- **Phase 3**: Overwritten language (adjective/adverb density, passive voice)
- **Phase 4**: Flat prose (add sensory details)
- **Phase 5**: Obvious statements (add subtlety)
- **Phase 6**: Dialogue (voice development)
- **Phase 7**: Weak language patterns (12 categories of hedge words/transitions)
- **Phase 8**: Rhythm + Strategic imperfections (sentence variation)
- **Phase 9**: AI pattern detection (N-grams, perfection syndrome)
- **Phase 10**: Word filtering (reintroduced prohibited terms)

**"AI BANNED Construction" patterns focus on:**
- **Syntactic structures** that appear correct grammatically but are mechanical/robotic
- **Narrative mechanics intrusion** (breaking immersion)
- **Emotional shorthand** that substitutes form for content
- **Metaphorical defaults** (distinct from vocabulary filtering)

**Critical Gap Identified**: No existing phase targets **structural construction patterns** as a primary domain. These patterns are:
- Syntactically correct (Phase 1 won't catch them)
- Not vocabulary-based (Phase 2 won't catch them)
- About structure, not density (Phase 3 focuses on density, not structure)
- Not about sensory details (Phase 4 is about adding, not restructuring)
- Related to emotional clarity, but distinct from Phase 5's approach (Phase 5 adds subtext; these patterns remove false text)

**Verdict**: **HIGH NOVELTY VALUE** - These patterns represent an entirely new detection domain.

---

### Do These Rules Make Sense?

**YES - With qualifications**

Each pattern is:

✓ **Mechanically detectable** - Clear trigger phrases/structures
✓ **Humanly avoidable** - Humans rarely write this way without noticing
✓ **AI-characteristic** - These appear consistently in AI output
✓ **Purpose-driven** - Each pattern substitutes form for content (the core principle)

**Qualifications**:

⚠️ **Context matters** - Some patterns are valid in specific genres/contexts:
- Echo-line poetics: Valid in literary fiction (intentional stylistic choice)
- Anthropomorphized silence: Valid in high-end literary prose
- False range construction: Valid in persuasive/rhetorical writing

**Recommendation**: When implementing, add **context awareness**:
- In literary fiction: Some patterns (echo-line poetics, anthropomorphized silence) may be intentional
- In commercial fiction/erotica: All patterns should be minimized
- In expository writing: Apply all rules strictly

---

### Recommendation: Where to Add These Rules

## OPTION 1: CREATE NEW PHASE 8.5 (PREFERRED)

**Phase 8.5: Structural Construction Cleanup**
- **Position**: Between Phase 8 (Strategic Imperfections) and Phase 9 (AI Pattern Detection)
- **Domain**: Syntactic structure patterns that simulate depth/emotion without creating it
- **Coverage**: 29 patterns from "AI BANNED Construction"
- **Output**: Restructured text with mechanical patterns eliminated

**Advantages**:
- ✓ Clear domain isolation (structural patterns only)
- ✓ Doesn't interfere with existing phases
- ✓ Can be optional or required based on writing type
- ✓ Aligns with architecture principle of phase specialization
- ✓ Easy to debug if issues arise

**Disadvantages**:
- ✗ Adds 11th phase (slight complexity increase)
- ✗ Introduces optional phase between core phases 8 and 9

---

## OPTION 2: ENHANCE PHASE 3 (OVERWRITTEN LANGUAGE REDUCTION)

**Add "Structural Construction Patterns" subsection to Phase 3**

**Affected patterns** (14 of 29 fit Phase 3 domain):
- Triple-Beat Lists → Reduce to single impact element
- Echo-Line Poetics → Consolidate parallelism
- Blank Desire Statements → Convert to specific actions
- Aestheticized Damage → Show cost, not performance
- Misapplied Epic Tone → Scale language proportionally
- Atmospheric Front-Loading → Start with character
- Meta-Narrative Intrusion → Stay in POV
- Sequential Action Pairs → Show consequence, not choreography
- Vague Interiority → Name what's happening
- Hollow Restraint → Name what's contained
- Standalone "Because" → Integrate into action
- Mood-Prop Negation → Remove unnecessary negation
- False Range Construction → Use actual scales
- Negative Parallelism → State directly

**Advantages**:
- ✓ No new phase required
- ✓ Fits Phase 3's existing domain (sentence-level overwriting)
- ✓ Consolidates related rules in one place
- ✓ Phase 3 already handles similar patterns

**Disadvantages**:
- ✗ Phase 3 would become significantly larger (~50% expansion)
- ✗ Mixes two distinct problems: density (current) + structure (new)
- ✗ Makes Phase 3 harder to maintain and explain

---

## OPTION 3: ENHANCE PHASE 7 (WEAK LANGUAGE CLEANUP)

**Add "Structural Weakness Patterns" subsection to Phase 7**

**Affected patterns** (8 of 29 fit Phase 7 domain):
- Negation Formula ("not X, but Y")
- Faux-Intellectual Aphorism
- Articulation by Proxy ("a look that said")
- Hedged Reactions ("isn't quite")
- Negative Parallelism ("not only... but...")
- Conjunction Starts (overuse)
- Vague Interiority ("something shifts")
- Superficial Analysis as Narration

**Advantages**:
- ✓ Some patterns already in Phase 7
- ✓ Weak language and structural weakness are adjacent concepts

**Disadvantages**:
- ✗ Only 8 of 29 patterns fit (incomplete)
- ✗ Doesn't address structural problems (anthropomorphized silence, echo-line poetics, etc.)
- ✗ Would require Phase 7 + Phase 3 modifications (messy)

---

## OPTION 4: ENHANCE PHASE 9 (AI PATTERN DETECTION)

**Add "Construction Pattern Detection" subsection to Phase 9**

**Rationale**: Phase 9 detects "AI patterns" - these construction patterns ARE AI patterns

**Advantages**:
- ✓ Philosophically aligned (these are AI characteristic patterns)
- ✓ Phase 9 already has pattern detection infrastructure
- ✓ No new phase required

**Disadvantages**:
- ✗ Phase 9 is about N-grams and perplexity optimization, not structure
- ✗ Would create confusion about Phase 9's scope
- ✗ Phase 9 already has heavy load (pattern families, rhythm variations)
- ✗ Would violate Phase 9's domain restriction: "QUALITATIVE pattern replacement ONLY"

**Note**: Phase 9 does handle some of these (e.g., "Superficial Analysis as Narration") but not systematically.

---

## FINAL RECOMMENDATION

### PRIMARY: **CREATE PHASE 8.5** ✓✓✓

**Phase 8.5: Structural Construction Elimination**

**Placement**: After Phase 8 (Strategic Imperfections), Before Phase 9 (AI Pattern Detection)

**Why this is best**:
1. **Architecture alignment**: Follows phase specialization principle
2. **No scope creep**: Existing phases stay focused
3. **Optional insertion point**: Can be used selectively for commercial fiction/erotica
4. **Clear domain**: 29 syntactic patterns (not handled by any existing phase)
5. **Easy debugging**: If issues arise, isolated to this phase
6. **Maintenance**: Easier to update when new patterns discovered

**Processing order** (revised 10-phase sequence):
```
1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 8.5 → 9 → 9.5 (opt) → 10
```

**Cost**: ~8 hours to create template, test, document

---

### SECONDARY: **ENHANCE PHASE 3** ✓✓

If creating a new phase is problematic, enhance Phase 3 with dedicated "Structural Construction Patterns" section.

**Affected patterns** (14 fit cleanly):
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

**Remaining 15 patterns** would be distributed to:
- Phase 5 (3 patterns: Blank Desire refinement, Subtlety edge cases)
- Phase 7 (4 patterns: Weak language structure issues)
- Phase 9 (5 patterns: AI mechanical patterns)
- Master List (3 patterns: Word-level detection)

**Cost**: ~4 hours to integrate into Phase 3

---

## PART 4: SPECIFIC IMPLEMENTATION DETAILS

### IF CREATING PHASE 8.5:

**Phase Name**: "Structural Construction Elimination"

**Domain**: Syntactic and structural patterns that simulate depth/emotion/tension without creating actual content

**Detection Triggers** (from quick-scan table in document):
```
", then" → Rewrite as fluid motion or consequence
"something" + verb → Name what's actually happening
"silence" + stretches/hangs/sits → Show effect through behavior
"not [X], but [Y]" → Commit to what it is
"isn't quite" → Describe the gesture specifically
"hangs in the air" → Show consequence, not suspension
"like a blow/punch/freight train" → Show sensation directly
"like a stone" + water → Cut—dead metaphor
triple noun/fragment sequence → Cut to what matters or integrate
[Verb]. [Verb]. [Verb]. → Vary syntax
"And" / "But" sentence start → Use sparingly
"Because [X]." fragment → Integrate or show through action
"surgical precision" / "practiced ease" → Show actual movement
"steel" / "iron" / "velvet" / "silk" → Find different texture
"wanted her/him" without object → Specify what's wanted and why
"a look that said" / "didn't need words" → Show the actual exchange
"held it together" / "swallowed it down" → Name what's being contained
"changed everything" / "broke forever" → Scale to proportion
weather/skyline as scene opener → Start with character
"from X to Y" (abstract) → Check if actual scale exists
"the older man" / "the younger woman" → Use names
participle + highlighting/underscoring → Delete editorial narration
"not only... but" → State directly or cut
```

**Output Format**: Restructured prose with mechanical patterns eliminated

**Never Touch**: Dialogue, Markdown, established character voice

---

### IF ENHANCING PHASE 3:

**New Subsection**: "Structural Construction Patterns - Phase 3 Focus"

**Addition to existing detection criteria**:

After current subsections (excessive adjectives, melodrama, complex sentences, etc.), add:

```json
"structural_construction_patterns": {
  "definition": "Syntactic structures that simulate content/emotion without creating it",
  "detection_markers": [...14 patterns from recommended list...],
  "fix_strategy": "Restructure sentence to show actual content, consequence, or action"
}
```

**Integration point**: After "narrative_stagnation" subsection, before current output_format

---

## PART 5: MASTER LIST INTEGRATION

### Patterns Already in Master List (12 of 29):

These can remain in Phase 2 as word-level catches:
- Gravitational Metaphors ("pulled toward," "drawn to," "orbits")
- Suspension Phrases ("hangs in the air," "hangs between")
- Impact Similes ("like a blow," "like a punch")
- Ripple/Stillness Similes ("like a stone," "rippled through")
- Precision/Control Cluster ("surgical precision," "practiced ease," "economical")
- Quality/Texture Defaults ("velvet," "silk," "steel," "iron," "granite")
- Articulation by Proxy ("a look that said," "didn't need words")
- Elegant Variation ("the older man" / "the younger woman")
- Superficial Analysis ("highlighting," "underscoring," "emphasizing")
- Hedged Reactions ("isn't quite a laugh," "isn't quite a smile")
- Faux-Intellectual Aphorism ("we are all just stories," "pain is love with nowhere to go")
- Negation Formula ("not X, but Y" patterns)

**Recommendation**: Keep these in Master List (Phase 2) + add structural/context-awareness to Phase 8.5 or Phase 3

---

## PART 6: DOES THE RULE MAKE SENSE?

**Philosophical Alignment Check**:

✓ **Core principle of "AI BANNED Construction"**: "Every construction listed here substitutes form for content."

✓ **Core principle of ClaudeHumanizer**: Eliminate AI detection markers while preserving meaning and voice

✓ **Perfect alignment**: These patterns ARE substituting form for content, which is exactly what the Humanizer targets

**Consistency Check**:

✓ Each pattern has:
- Clear trigger phrase/structure
- Explanation of why it fails
- Concrete examples of good vs. bad
- Specific fix strategy

✓ All 29 patterns follow the same analytical framework

✓ No contradictions between patterns

**Practical Check**:

✓ Patterns are mechanically detectable (high confidence detection rules possible)

✓ Fixes are structurally sound (rewriting doesn't introduce new problems)

✓ Human writers naturally avoid these patterns

✓ AI consistently produces these patterns

**Verdict**: **YES - The rules make strong sense and integrate naturally with Humanizer philosophy**

---

## SUMMARY TABLE: INTEGRATION ROADMAP

| Implementation | Effort | Coverage | Cleanliness | Recommendation |
|---|---|---|---|---|
| Create Phase 8.5 | 8 hrs | 100% (29/29) | Perfect | **PRIMARY** ✓✓✓ |
| Enhance Phase 3 | 4 hrs | 48% (14/29) | Good | SECONDARY ✓✓ |
| Enhance Phase 7 | 3 hrs | 28% (8/29) | Poor | Not recommended |
| Enhance Phase 9 | 5 hrs | 40% (12/29) | Confusing | Not recommended |

---

## NEXT STEPS

1. **Decision**: Choose between Phase 8.5 creation or Phase 3 enhancement
2. **Development**: Create template and test rules on sample texts
3. **Documentation**: Add to CLAUDE.md, CHANGELOG.md, PROMPT_STANDARDS.md
4. **Testing**: Run through full pipeline with diverse text samples
5. **Validation**: Confirm no interference with other phases

---

## APPENDIX: PATTERN COVERAGE BY EXISTING PHASE

### Phase 1 (Grammar) - 0 patterns covered
(These are all syntactically correct)

### Phase 2 (AI Word Cleaning) - 12 patterns covered
- Gravitational Metaphors
- Suspension Phrases
- Impact Similes
- Ripple/Stillness Similes
- Precision/Control Cluster
- Quality/Texture Defaults
- Articulation by Proxy
- Elegant Variation
- Superficial Analysis (word-level)
- Hedged Reactions (word-level)
- Faux-Intellectual Aphorism (word-level)
- Negation Formula (word-level)

### Phase 3 (Overwritten Language) - 6 patterns implicitly covered
- Triple-Beat Lists (as excessive structure)
- Echo-Line Poetics (as excessive parallelism)
- Blank Desire Statements (as melodrama)
- Aestheticized Damage (as melodrama)
- Misapplied Epic Tone (as purple prose)
- Atmospheric Front-Loading (as narrative stagnation)

### Phase 4 (Sensory Enhancement) - 0 patterns covered
(These are about structure, not sensory details)

### Phase 5 (Subtlety Creation) - 2 patterns implicitly covered
- Vague Interiority (as improving specificity)
- Blank Desire Statements (as improving psychological grounding)

### Phase 6 (Dialogue) - 0 patterns covered
(These patterns mostly avoid dialogue; Phase 6 only modifies dialogue)

### Phase 7 (Weak Language) - 4 patterns explicitly covered
- Negation Formula ("not X, but Y")
- Conjunction Starts (And/But overuse, as weak transitions)
- Faux-Intellectual Aphorism (as pretentious language)
- Negative Parallelism (as weak structure)

### Phase 8 (Strategic Imperfections) - 3 patterns explicitly covered
- Staccato Verb Fragments (as rhythm variation)
- Conjunction Starts (as earned emphasis)
- Sequential Action Pairs (implicitly, through rhythm variation)

### Phase 9 (AI Pattern Detection) - 4 patterns explicitly covered
- Superficial Analysis as Narration (editorial intrusion detection)
- Faux-Intellectual Aphorism (AI insight patterns)
- Meta-Narrative Intrusion (narrative structure intrusion)
- Perfection syndrome (overall mechanical patterns)

### Phase 10 (Word Filtering) - 0 patterns covered
(Word-level filtering only)

### NOT COVERED BY ANY PHASE: 7 critical patterns
❌ Anthropomorphized Silence
❌ Echo-Line Poetics (only implicit in Phase 3)
❌ Mood-Prop Negation
❌ Meta-Narrative Intrusion (only implicit in Phase 9)
❌ Atmospheric Front-Loading (only implicit in Phase 3)
❌ Hollow Restraint
❌ False Range Construction

---

**END OF ANALYSIS**
