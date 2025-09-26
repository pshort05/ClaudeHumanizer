# Claude Humanizer

A comprehensive collection of Claude prompts designed to transform AI-generated text into natural, human-like writing. These specialized editors work together to eliminate AI detection markers while preserving meaning, voice, and quality.

## Overview

These prompts operate in **silent mode** by default - they process text and return only the improved version without commentary or analysis, unless explicitly asked for feedback. All prompts preserve dialogue, titles, headers, and markdown formatting while enhancing the narrative prose.

## Recommended Processing Order

For optimal results, run the prompts in this sequence:

### 1. Silent Strunk & White Editor
**File:** `strunk_white_editor.json`
**Description:** Silent editor that fixes only critical grammar and style violations while preserving all other elements unchanged

**How it works:** This foundational editor corrects clear grammatical errors (possessive apostrophes, comma splices, sentence fragments, subject-verb agreement, pronoun case, dangling modifiers) while leaving all stylistic choices, dialogue, and creative decisions intact. It operates with surgical precision, changing only what is objectively wrong.

### 2. Text Quality Enhancement Editor
**File:** `text_quality_prompt.json`
**Description:** Precision text editor that eliminates low-quality language while preserving meaning and style

**How it works:** Systematically removes weak language patterns including puff words (utilize→use), empty calorie words (something, stuff), inflation words (very, extremely), weasel words (may, might), hedge words (sort of, kind of), filter phrases (he watched, she saw), clichés, formal hedging, and redundant phrases. Replaces them with stronger, more direct alternatives.

### 3. Claude Humanizer - Detection and Replacement System
**File:** `claude_humanizer_V1.json`
**Description:** Comprehensive prompt system for detecting AI-generated text patterns and replacing them with natural, human-like alternatives - enhanced with silent mode operation and dialogue preservation

**How it works:** Advanced pattern recognition system that identifies and replaces AI-specific language markers with human alternatives. Adds strategic imperfections, varies sentence structure, incorporates authentic human speech patterns, and eliminates robotic phrasing while maintaining the original meaning and voice.

### 4. AI Text Cleaner - Grounded Language Editor
**File:** `ai_text_cleaner.json`
**Description:** Professional text editor that replaces AI-associated words and phrases with natural, grounded alternatives while preserving dialogue

**How it works:** Specifically targets AI-associated vocabulary and phrases that commonly appear in generated text. Replaces artificial-sounding language with more natural, grounded alternatives. Focuses on word-level improvements to make text sound more authentically human.

### 5. Purple Prose Detection and Revision Specialist
**File:** `purple_prose_removal.json`
**Description:** Expert prose editor specializing in identifying and eliminating purple prose while preserving purposeful descriptive writing

**How it works:** Identifies and eliminates six categories of purple prose: excessive adjectives/adverbs, melodramatic tone, overly complex sentences, unnecessary vocabulary, figurative language overuse, and narrative stagnation. Maintains genre-appropriate ornate language when it serves world-building or character development purposes.

### 6. Silent On the Nose Editor
**File:** `on_the_nose_editor.json`
**Description:** Expert editor that silently identifies and fixes on-the-nose prose, returning only the improved text without commentary or analysis

**How it works:** Transforms obvious, literal prose into sophisticated, nuanced writing by replacing direct emotion statements with physical manifestations, embedding themes in actions rather than statements, showing motivations through behavior, demonstrating relationships through dialogue patterns, and creating atmosphere through specific sensory details.

### 7. Vivid Prose Enhancement System
**File:** `fix_boring_prose.json`
**Description:** Advanced prose analysis and enhancement system that transforms boring, flat descriptions into vivid, immersive writing using systematic editing techniques

**How it works:** Applies four core improvements: eliminates vague words (seemed, somewhat, probably), reduces excessive adverbs by replacing with stronger verbs, enhances sensory balance (sight, sound, smell, touch, taste), and replaces clichés with original metaphors. Creates immersive experiences that place readers directly in the character's perspective.

### 8. Dialogue Enhancer System
**File:** `dialogue_enhancer.json`
**Description:** Advanced silent dialogue improvement system incorporating comprehensive voice authenticity techniques

**How it works:** Specializes in refining dialogue while maintaining character authenticity. Enhances speech patterns, improves conversational flow, eliminates stilted or artificial-sounding dialogue, and ensures each character maintains a distinctive voice. Works across cultures, eras, and demographics while avoiding stereotypical traps.

### 9. Enhanced Human-Style Writing Editor
**File:** `human_writing_editor_v2.json`
**Description:** Comprehensive editing system that transforms AI-generated or problematic prose into natural, human-like writing that passes detection while maintaining fiction quality standards

**How it works:** The final comprehensive pass that combines multiple editing approaches. Eliminates remaining AI detection markers, optimizes readability, creates authentic human voice, and ensures the text passes AI detection tools while maintaining high literary quality. Applies advanced techniques for creating prose indistinguishable from skilled human writing.

## Usage Notes

- All editors operate in **silent mode** - they return only the improved text unless you explicitly request analysis
- **Dialogue preservation** - Character speech remains untouched across all editors
- **Structure preservation** - Titles, headers, markdown formatting, and document structure are maintained
- **Incremental improvement** - Each editor builds upon the previous improvements
- **Voice consistency** - Original author voice and style are preserved while eliminating technical weaknesses

## File Versions

All prompts are regularly updated with the latest version information and dates. Check the individual JSON files for specific version numbers and last updated dates.