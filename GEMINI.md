# GEMINI.md

## Directory Overview

This directory, "ClaudeHumanizer," contains a sophisticated, well-documented system for "humanizing" AI-generated text. It is not a traditional code project but rather a collection of configuration files and documentation that define a multi-phase text processing pipeline. The core of the project is a series of JSON files that serve as system prompts for a Large Language Model (LLM), designed to be executed sequentially in an "assembly line" fashion. The primary goal is to transform robotic, AI-generated text into prose that reads as if it were written by a human, thereby evading AI detection. The system is heavily optimized for use with Anthropic's Claude models but is also compatible with other high-end LLMs like Gemini and GPT.

## Key Files

*   **Numbered JSON Files (`1_` to `10_` plus optionals):** These are the heart of the project. Each file represents a distinct phase in the humanization pipeline. The pipeline consists of 10 core phases and several optional ones (6.1, 8.5, 9.5) that can be inserted for more specialized tasks.
    *   **Phase 8.5 (`8.5_structural_construction_elimination.json`)**: A significant recent addition for eliminating common AI syntactic patterns.
    *   **Phase 9.5 (`9.5_statistical_analysis_hub.json`)**: Consolidates all quantitative statistical analysis (like burstiness, lexical diversity) into a single, optional step.

*   **Prohibited Words Lists:**
    *   `master_prohibited_words.json`: A critical data file containing a curated list of AI-associated words, phrases, and patterns. It is a required dependency for phases 2 and 10.
    *   `master_prohibited_words_romance.json` & `master_prohibited_words_erotica.json`: Optional, genre-specific word lists that can be used with Phase 10 for more targeted filtering.

*   **`README.md`**: The main entry point for understanding the project. It provides a high-level overview of the assembly line, its key features, model recommendations, and different methods for execution.

*   **`docs/`**: This directory contains extensive documentation, crucial for understanding the system's depth. Key documents include:
    *   `USAGE_GUIDE.md`: Step-by-step instructions for using the pipeline.
    *   `TECHNICAL_REFERENCE.md`: Advanced information for developers, including API configurations and automation.
    *   `How AI Detectors Work.md`: A comprehensive research document that details the statistical, linguistic, and structural methods used by AI detection systems. This document provides the theoretical foundation for the humanization techniques used in the pipeline.
    *   `CHANGELOG.md`: Documents the evolution of the system.

*   **Development & Standardization Files:**
    *   `PROMPT_TEMPLATE.json`: A master template for creating new phase prompts.
    *   `PROMPT_STANDARDS.md`: Defines the rules and conventions for prompt development.
    *   `validate_prompt.py`: A Python script to ensure all prompts adhere to the defined standards.

*   **`examples/`**: Contains various pipeline configurations (as YAML files) for different LLMs and use cases, as well as a pre-built n8n automation workflow (`n8n_workflow_sample.json`).

*   **`CLAUDE.md`**: A special instruction file specifically for the Claude AI, guiding it on how to interact with and understand the repository's structure and development workflow.

## Usage & Architecture

The contents of this directory are intended to be used as a complete system for processing text. The workflow is as follows:

1.  Start with a piece of AI-generated text.
2.  Process the text through the phases sequentially (e.g., Phase 1 -> 2 -> 3...). The output from one phase becomes the input for the next.
3.  The optional phases (6.1, 8.5, 9.5) can be inserted into the sequence as needed.
4.  For each phase, the corresponding JSON file is used as a system prompt for an LLM. The text to be processed is provided as the user input.
5.  **Dependencies are critical**:
    *   **Phase 2** and **Phase 10** require the contents of `master_prohibited_words.json` to be included in the prompt.
    *   **Phase 10** can also optionally include the genre-specific lists for romance or erotica.

This process can be executed manually (by copying and pasting into an LLM interface), semi-automatically (using features like Claude Projects or custom GPTs), or fully automatically via API calls orchestrated by a tool like n8n or a custom script, as detailed in the `TECHNICAL_REFERENCE.md`.