# Developmental Editor - Usage Guide

## What Is This Tool?

The Developmental Editor is an **interactive, pre-pipeline tool** for reviewing outlines and early chapter drafts. It provides structural, character, plot, and pacing feedback to help you fix big-picture story issues before investing time in polish.

**This is NOT part of the ClaudeHumanizer 10-phase pipeline.** Use this tool first, make developmental changes, then run through the pipeline for final polish.

---

## When to Use This Tool

### ✅ USE THIS FOR:
- Chapter outlines (bullet points, scene summaries)
- Early chapter drafts (rough first drafts)
- Scene breakdowns
- Story structure outlines
- Character arc summaries
- **Developmental editing concerns**: plot, structure, character, pacing, stakes

### ❌ DON'T USE THIS FOR:
- Final drafts ready for publication
- AI detection removal (use ClaudeHumanizer phases 1-10)
- Line editing or copyediting (use phases 1-10)
- Grammar correction (use Phase 1)
- Purple prose removal (use Phase 3)
- Dialogue polishing (use Phase 6)

---

## Three Operation Modes

### Mode 1: Analysis & Feedback (DEFAULT)

**When it activates:** You submit an outline or chapter and ask for review, feedback, or analysis.

**What it does:** Provides detailed developmental feedback organized by priority. **Does NOT make changes** unless you explicitly ask.

**Example prompts:**
- "Review this chapter outline"
- "What are the biggest problems with this draft?"
- "Give me feedback on this chapter"
- "Is this outline ready to draft?"

**Output format:** Structured feedback report with:
- Summary Assessment
- Critical Issues (must fix)
- Major Issues (should fix)
- Moderate Issues (consider fixing)
- Strengths (what's working)
- Recommendations (next steps)

---

### Mode 2: Interactive Revision (ON REQUEST)

**When it activates:** You explicitly request changes, revisions, or rewrites.

**What it does:** Makes specific requested changes while maintaining your voice and intent. Asks clarifying questions if needed.

**Example prompts:**
- "Rewrite this scene to increase stakes"
- "Restructure this chapter to improve pacing"
- "Add more conflict to this outline"
- "Fix the plot hole where..."
- "Strengthen the character motivation in scene 3"

**Output format:** Revised text with changes implemented.

---

### Mode 3: Collaborative Discussion

**When it activates:** You ask questions, discuss options, or explore alternatives.

**What it does:** Engages in back-and-forth discussion. Presents multiple approaches. Helps you make informed decisions.

**Example prompts:**
- "Should I cut scene 4 or combine it with scene 5?"
- "What are different ways to raise the stakes here?"
- "I'm stuck on how to structure the midpoint - what are my options?"
- "Would it work better if the protagonist..."

**Output format:** Conversational responses with options, trade-offs, and recommendations.

---

## What The Tool Evaluates

### 10 Developmental Editing Domains

1. **Story Structure & Pacing**
   - Inciting incident, rising action, climax, resolution
   - Act structure (3-act, 4-act, or 5-act)
   - Turning points and escalation
   - Opening hook and earned ending

2. **Character Development & Arc**
   - Character goals (external and internal)
   - Motivation that drives action
   - Character arc with growth or change
   - Character agency (protagonist drives story)
   - Distinct voice and personality

3. **Conflict & Stakes**
   - Clear opposition (antagonist or obstacle)
   - Stakes that matter and escalate
   - Personal consequences for failure
   - Emotional investment for reader
   - Urgency element (ticking clock)

4. **Scene Effectiveness**
   - Every scene has clear goal/purpose
   - Scene advances plot OR develops character OR deepens theme
   - Scene has mini-arc (goal, conflict, outcome)
   - Scenes build momentum

5. **Plot Logic & Coherence**
   - Character actions make sense
   - Events follow cause-and-effect
   - No convenient coincidences
   - Consistent world rules
   - Proper foreshadowing

6. **Emotional Impact**
   - Reader connection to protagonist
   - Emotional beats given proper weight
   - Variety of emotions
   - Earned emotional payoffs
   - Authentic reactions

7. **Chapter Structure**
   - Strong chapter opening
   - Chapter advances overall arc
   - Effective chapter ending (hook or momentum)
   - Appropriate chapter length
   - Consistent POV

8. **Outline Completeness**
   - All essential story beats present
   - Logical scene progression
   - Clear cause-and-effect chain
   - Setup and payoff identified
   - Character arc mapped

9. **Genre Expectations**
   - Story delivers on genre promises
   - Genre conventions met or deliberately subverted
   - Tone matches genre
   - Pacing appropriate for genre

10. **Reader Engagement**
    - Opening hooks readers
    - Forward momentum maintained
    - Questions created and answered
    - Surprises and subversions
    - Satisfying payoffs

---

## Priority Levels

### 🔴 CRITICAL (Must Fix Before Proceeding)
- No clear protagonist goal
- Stakes absent or unclear
- Plot holes that destroy logic
- Character motivation missing/contradictory
- Conflict nonexistent
- Scenes that advance nothing
- Missing essential story beats

### 🟠 MAJOR (Should Address Before Final Draft)
- Weak or generic stakes
- Passive protagonist
- Predictable or clichéd plot
- Underdeveloped character relationships
- Pacing problems
- Scenes that could be combined/cut
- Missing emotional beats

### 🟡 MODERATE (Consider During Revision)
- Unclear scene goals
- Weak chapter hooks/endings
- Underutilized secondary characters
- Missed conflict opportunities
- Predictable character reactions
- Generic world-building

### ⚪ POLISH (Address During Line Editing)
- Could add sensory details
- Opportunity for deeper emotion
- Could strengthen thematic elements
- Sentence structure variety
- **→ Use ClaudeHumanizer pipeline for these**

---

## How to Use the Tool

### Step 1: Submit Your Content

Paste your outline or chapter draft, then specify what you want:

**For Analysis:**
```
Here's my chapter outline. Please review and provide feedback.

[paste outline]
```

**For Specific Revision:**
```
This chapter feels too slow. Please restructure to improve pacing.

[paste chapter]
```

**For Discussion:**
```
I'm not sure if this scene should come before or after the reveal.
What are the pros and cons of each approach?

[paste relevant content]
```

---

### Step 2: Review Feedback

**Analysis Mode Output Structure:**

```markdown
## Summary Assessment
[High-level overview of strengths and primary concerns]

## 🔴 Critical Issues
1. ISSUE: No clear stakes established
   EXAMPLE: "Protagonist wants to win the race but there's no consequence for losing"
   IMPACT: Reader has no reason to care about outcome
   SOLUTION: Add personal stakes - losing means losing scholarship/disappointing father/etc.

## 🟠 Major Issues
[Numbered list with examples and solutions]

## 🟡 Moderate Issues
[Bulleted list with quick fixes]

## ✅ Strengths
[What's working well - 3-5 elements]

## 📋 Recommendations
[Prioritized next steps]
1. First, fix the stakes issue (critical)
2. Then address passive protagonist problem
3. Consider restructuring scene 4...
```

---

### Step 3: Iterate

The tool is **interactive**. You can:

- Ask follow-up questions
- Request clarification on feedback
- Ask for specific revisions
- Explore alternative approaches
- Discuss trade-offs between options

**Example conversation:**
```
You: Review this outline
Tool: [provides analysis with 3 critical issues]

You: I understand the stakes problem. What are 3 different ways I could fix it?
Tool: [presents 3 options with trade-offs]

You: I like option 2. Can you rewrite the outline incorporating that change?
Tool: [returns revised outline]

You: That's better, but now scene 5 feels redundant. What do you think?
Tool: [discusses scene 5, suggests combination with scene 6]
```

---

## Example Use Cases

### Use Case 1: Outline Review

**Input:**
```
Please review this chapter outline for developmental issues.

Chapter 3: The Discovery
- Sarah wakes up and has breakfast
- She goes to the library to research
- She finds an old book with mysterious symbols
- She checks out the book and goes home
- She reads the book and learns about the prophecy
- She decides to tell her friend Marcus
```

**Output (Analysis Mode):**
```markdown
## Summary Assessment
This outline has a potentially interesting discovery (mysterious book), but
suffers from passive structure and lacks conflict. The protagonist moves
through locations without obstacles or meaningful choices.

## 🔴 Critical Issues

1. ISSUE: No conflict in any scene
   EXAMPLE: Sarah encounters zero obstacles - library has book, she checks
   it out, reads it, learns information
   IMPACT: Chapter will feel flat and uneventful
   SOLUTION: Add opposition - library restricted section requiring sneaking
   in, book is encrypted/hard to decode, someone else wants the book, etc.

2. ISSUE: Protagonist is completely passive
   EXAMPLE: Events happen TO Sarah (finds book, reads it) not BECAUSE of her
   IMPACT: Protagonist feels reactive rather than driving story
   SOLUTION: Sarah should make active choices with consequences - chooses to
   break rules to access book, chooses to hide discovery from authorities, etc.

## 🟠 Major Issues

1. Opening with mundane activity (waking up, breakfast)
   - Start with Sarah already pursuing her goal or encountering first obstacle

2. Information dump risk
   - "Reads book and learns about prophecy" will likely become exposition dump
   - Consider: drip information across multiple scenes, have her decode pieces,
     create mystery about missing information

## ✅ Strengths
- Clear goal (research)
- Discovery that advances plot
- Logical scene progression
- Natural ending (decision to share info)

## 📋 Recommendations
1. Cut wake-up/breakfast - start with library scene
2. Add conflict to library scene (restricted access, rival seeker, time pressure)
3. Make Sarah active - she should break a rule or make a difficult choice
4. Split prophecy reveal - don't give all information at once
5. Add complication to "tell Marcus" decision - reason she shouldn't trust him
```

---

### Use Case 2: Chapter Revision Request

**Input:**
```
This chapter feels too slow and the stakes are weak. Please revise to
increase pacing and make the stakes more urgent.

[paste chapter draft]
```

**Output (Revision Mode):**
Returns revised chapter with:
- Faster pacing (scenes tightened, cuts made)
- Increased stakes (higher consequences, ticking clock added)
- Maintains your voice and style
- Brief summary of major changes made

---

### Use Case 3: Collaborative Discussion

**Input:**
```
I have a plot problem. My protagonist needs to escape the prison, but I don't
want them to succeed too easily. What are some ways to make this harder
without feeling contrived?
```

**Output (Discussion Mode):**
```markdown
Great instinct to avoid an easy escape. Here are several approaches:

## Option 1: Internal Obstacle (Character-Based)
Add internal conflict - protagonist could escape alone but won't leave
someone behind (cellmate, sibling, etc.)
- PRO: Deepens character, raises emotional stakes
- CON: Requires established relationship earlier
- WORKS BEST IF: You want character growth moment

## Option 2: Escalating External Complications
Stage the escape with increasing difficulty:
- Stage 1: Get out of cell (achievable)
- Stage 2: Navigate guards (harder, requires plan)
- Stage 3: External wall (seems impossible)
- Each success raises next obstacle
- PRO: Maintains momentum, feels earned
- CON: Requires careful balance so it's not frustrating
- WORKS BEST IF: You want action-focused sequence

## Option 3: Betrayal/Unexpected Reversal
Protagonist almost succeeds, then ally betrays them OR guard catches them
at last moment
- PRO: Dramatic, raises tension
- CON: Can feel contrived if not properly foreshadowed
- WORKS BEST IF: You've planted seeds of distrust earlier

## Option 4: Pyrrhic Victory
They escape but at significant cost (injured, someone dies, now hunted)
- PRO: Success with consequences, raises future stakes
- CON: Can feel unsatisfying if cost too high
- WORKS BEST IF: You want long-term story ramifications

Which direction interests you? Or would you like to explore combinations?
```

---

## Recommended Workflow

### The Complete Writing Process

```
1. ⭐ Outline/Draft → Developmental Editor (THIS TOOL)
   ↓
2. Make structural changes based on feedback
   ↓
3. Revise draft with developmental improvements
   ↓
4. ⭐ Run through ClaudeHumanizer 10-Phase Pipeline
   ↓
   Phase 1: Grammar Foundation
   Phase 2: AI Word Cleaning
   Phase 3: Purple Prose Reduction
   Phase 4: Sensory Enhancement
   Phase 5: Subtlety Creation
   Phase 6: Dialogue Enhancement
   Phase 7: Weak Language Cleanup
   Phase 8: Strategic Imperfections
   Phase 9: Final Verification
   Phase 10: Final AI Word Sweep
   ↓
5. Final draft ready for publication
```

**Key principle:** Fix big-picture story problems BEFORE investing time in line-level polish.

---

## Tips for Best Results

### ✅ DO:
- Be specific about what kind of feedback you want
- Provide context (genre, target audience, series vs standalone)
- Ask follow-up questions if feedback unclear
- Request examples or alternatives
- Engage in discussion about trade-offs
- Use for outlines AND early drafts

### ❌ DON'T:
- Submit final drafts expecting line editing (use pipeline instead)
- Ask for grammar correction (use Phase 1)
- Request AI detection removal (use full pipeline)
- Expect the tool to write your story for you
- Ignore critical/major issues in favor of polish

---

## Common Questions

### Q: Can I use this for non-fiction?
**A:** The tool is optimized for fiction, but many principles apply to narrative non-fiction. Structure, pacing, and reader engagement concepts translate well.

### Q: What if I disagree with the feedback?
**A:** You should! This is YOUR story. Use feedback as input, not commandments. Engage in discussion mode to explore why recommendations were made and whether they align with your vision.

### Q: How long should my submission be?
**A:** Ideal: 1 chapter (3,000-8,000 words) or detailed outline. Can handle longer submissions but feedback may be less detailed on later sections.

### Q: Can I use this multiple times on the same chapter?
**A:** Absolutely! Iterate as much as needed. Submit → get feedback → revise → resubmit → discuss → revise again.

### Q: Should I fix everything before moving to the pipeline?
**A:** Fix CRITICAL and MAJOR issues. MODERATE issues can wait. POLISH items should definitely wait for the pipeline.

### Q: Can this replace a human developmental editor?
**A:** No tool replaces human editorial expertise, but this can help identify issues and provide structured feedback for revision.

---

## Troubleshooting

### "The feedback is too general"
→ Provide more context: genre, target audience, where you're stuck
→ Ask specific questions: "Is the pacing in scene 3 too slow?"
→ Request examples: "Show me what stronger stakes would look like here"

### "I don't understand a recommendation"
→ Ask: "Can you explain why you recommended [X]?"
→ Request alternatives: "What are other ways to solve this problem?"
→ Engage discussion mode: "Let's talk through the options"

### "The tool changed my voice when revising"
→ Provide guidance: "Revise but keep my informal/dark/humorous tone"
→ Give examples: "Here's a paragraph that captures my voice"
→ Iterate: "That's closer but make it [more specific direction]"

### "I got feedback on line-level issues instead of structure"
→ Be explicit: "Focus only on developmental issues - plot, character, structure"
→ Redirect: "I'll handle prose polish later - what are the story-level problems?"

---

## Integration with ClaudeHumanizer Pipeline

**This tool is a PRECURSOR, not part of the 10-phase pipeline.**

### Workflow:
```
Developmental Editor → Structural Revision → ClaudeHumanizer Pipeline → Publication
     (big picture)      (your work)         (line-level polish)
```

### Division of Labor:

| Developmental Editor | ClaudeHumanizer Pipeline |
|---------------------|--------------------------|
| Story structure | Grammar & mechanics |
| Character development | AI word removal |
| Plot logic | Purple prose reduction |
| Pacing | Sensory detail |
| Scene effectiveness | Subtlety enhancement |
| Stakes & conflict | Dialogue polish |
| Chapter structure | Weak language cleanup |
| Outline evaluation | Rhythm & flow |
| Genre expectations | Strategic imperfections |
| Reader engagement | AI pattern detection |

**Use both tools in sequence for best results.**

---

## Version History

### v1.0.0 (2025-01-12)
- Initial release
- Three operation modes (Analysis, Revision, Discussion)
- 10 evaluation domains
- 4-tier priority system
- Interactive feedback framework
- Designed as pre-pipeline developmental tool

---

## Related Documentation

- **ClaudeHumanizer USAGE_GUIDE.md** - How to use the 10-phase pipeline
- **ClaudeHumanizer TECHNICAL_REFERENCE.md** - LLM optimization tips
- **character_patterns.md** - Character naming patterns to avoid
- **PROMPT_TEMPLATE.json** - Standard prompt structure for phases

---

**Questions or feedback?** This tool is designed to be iterative and conversational.
If something isn't working, ask the tool to adjust its approach!
