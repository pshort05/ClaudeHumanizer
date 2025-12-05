# Plan: Gemini-Optimized Humanizer Workflow

This document outlines the plan to create a new, optimized version of the Humanizer workflow, specifically tailored for the Google Gemini API.

## Objective

To create an efficient, powerful, and maintainable humanization pipeline that leverages the specific strengths of the Gemini family of models, namely their large context windows and advanced instruction-following capabilities. This new workflow will be housed in a new `gemini/` subdirectory.

## Proposed 4-Stage Workflow

The 11+ phases of the original Claude-optimized workflow will be consolidated into four logical "mega-prompts" or stages. This consolidation will reduce the total number of API calls, leading to faster processing and lower operational costs.

### Stage 1: Foundational Cleanup
*   **Purpose:** To perform all foundational text correction and cleaning in a single pass.
*   **Consolidates:**
    *   Phase 1: Grammar Foundation
    *   Phase 2: AI Word Cleaning
    *   Phase 7: Weak Language Cleanup
    *   Phase 10: Final AI Word Sweep

### Stage 2: Stylistic & Narrative Enhancement
*   **Purpose:** To improve the artistic and narrative quality of the prose.
*   **Consolidates:**
    *   Phase 3: Overwritten Language Reduction
    *   Phase 4: Sensory Enhancement
    *   Phase 5: Subtlety Creation

### Stage 3: Advanced Structural & Statistical Humanization
*   **Purpose:** To execute the core anti-detection and structural rewriting tasks.
*   **Consolidates:**
    *   Phase 8: Strategic Imperfections
    *   Phase 8.5: Structural Construction Elimination
    *   Phase 9: Final Verification (AI Patterns)
    *   Phase 9.5: Statistical Analysis Hub

### Stage 4: Dialogue Refinement
*   **Purpose:** To perform a focused pass on dialogue to improve naturalness and character voice, keeping it separate from narrative styling.
*   **Consolidates:**
    *   Phase 6: Dialogue Enhancement
    *   Phase 6.1: Character Dialogue Pass

## Plan of Action

1.  **Create Directory:** Create a new `gemini/` subdirectory.
2.  **Author Gemini Prompts:** Write four new, optimized JSON prompt files corresponding to the stages above and save them in the new directory.
3.  **Create Gemini n8n Workflow:** Build a new `n8n_gemini_workflow.json` file that orchestrates the four new stages.
4.  **Write Documentation:** Create a `README.md` within the `gemini/` directory to explain the new workflow.
