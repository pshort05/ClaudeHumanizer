# GEMINI.md

## Directory Overview

This directory, "ClaudeHumanizer," contains a sophisticated, well-documented system for "humanizing" AI-generated text. It is not a traditional code project but rather a collection of configuration files and documentation that define a multi-phase text processing pipeline. The core of the project is a series of JSON files that serve as prompts for a Large Language Model (LLM), designed to be executed sequentially in an "assembly line" fashion. The primary goal is to transform robotic, AI-generated text into prose that reads as if it were written by a human, thereby evading AI detection. The system is heavily optimized for use with Anthropic's Claude models, particularly Claude Sonnet 4.5.

## Key Files

*   **Numbered JSON Files (`1_` to `10_`):** These are the heart of the project. Each file represents a distinct phase in the humanization pipeline, from basic grammar correction to adding strategic imperfections.
*   `master_prohibited_words.json`: A critical data file that contains a curated list of AI-associated words, phrases, and patterns that the pipeline is designed to remove.
*   `README.md`: The main entry point for understanding the project. It provides a high-level overview of the 10-phase assembly line, its key features, and different methods for execution.
*   `docs/`: This directory contains detailed documentation:
    *   `USAGE_GUIDE.md`: Step-by-step instructions for using the pipeline.
    *   `TECHNICAL_REFERENCE.md`: Advanced information for developers, including API configurations and automation.
    *   `How AI Detectors Work.md`: A comprehensive research document that details the statistical, linguistic, and structural methods used by AI detection systems. This document provides the theoretical foundation for the humanization techniques used in the pipeline.
    *   `HUMANIZATION_GAP_ANALYSIS.md`: An internal analysis document identifying potential new features and improvements for the pipeline based on studying other humanization techniques.
*   `examples/`: Contains YAML files with different pipeline configurations (e.g., for maximum quality, cost-effectiveness) and `n8n_workflow_sample.json`.
*   `CLAUDE.md`: A special instruction file specifically for the Claude AI, guiding it on how to interact with and understand the repository's structure and development workflow.

## Usage

The contents of this directory are intended to be used as a complete system for processing text. The workflow is as follows:

1.  Start with a piece of AI-generated text.
2.  Process the text through the 10 phases sequentially, starting with `1_grammar_foundation.json` and ending with `10_final_ai_word_sweep.json`.
3.  For each phase, the corresponding JSON file is used as a system prompt for an LLM (preferably Claude Sonnet 4.5). The text to be processed is provided as the user input.
4.  The output from one phase becomes the input for the next.
5.  Phases 2 and 10 have a special dependency on `master_prohibited_words.json`, which must be included in the prompt.

This process can be executed manually (by copying and pasting into an LLM interface), semi-automatically using Claude Projects, or fully automatically via API calls orchestrated by a tool like n8n or a custom script, as detailed in the `TECHNICAL_REFERENCE.md`.
