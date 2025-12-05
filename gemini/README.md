# Gemini Humanizer Workflow

This directory contains an optimized, 4-stage humanization workflow specifically designed for the Google Gemini API. This new workflow consolidates the 11+ phases of the original Claude-optimized pipeline into a more efficient, cost-effective, and powerful system.

## The Approach to Humanization with Gemini

The core philosophy behind this workflow is to leverage the unique strengths of the Gemini family of models, particularly their large context windows and advanced instruction-following capabilities. By consolidating multiple, highly-specific tasks into larger, logically-grouped "mega-prompts," we can achieve a more holistic and efficient humanization process.

This 4-stage approach provides several advantages:
- **Efficiency:** Reduces the number of API calls from 11+ to just 4, leading to faster processing times and lower operational costs.
- **Holistic Context:** Allows the model to consider multiple aspects of humanization (e.g., grammar, word choice, and weak language) simultaneously, leading to more natural and cohesive revisions.
- **Power:** Leverages the large context window of models like Gemini 1.5 Pro to maintain consistency across long-form documents.
- **Maintainability:** Simplifies the pipeline, making it easier to understand, manage, and adapt.

The workflow is designed to be sequential, with the output of one stage becoming the input for the next. Each stage builds upon the previous one, progressively transforming the text from robotic and predictable to nuanced and authentically human.

## How to Use the Gemini Prompts

There are two primary ways to use the Gemini Humanizer workflow: manually, by interacting directly with a Gemini-powered chat interface, or automatically, using an automation platform like n8n.

### Manual Usage
For those who prefer a hands-on approach, the prompts can be used manually in a chat interface that supports system prompts (like Google's AI Studio).

1.  **Start with your text:** Have your AI-generated text ready.
2.  **Load the prompt:** For each stage, copy the entire JSON content from the corresponding file (e.g., `1_foundational_cleanup.json`).
3.  **Set the system prompt:** Paste the copied JSON content into the "System Prompt" or "System Instructions" field of your chat interface. Note that for Phase 1, you will also need to manually copy and paste the contents of `master_prohibited_words.json` and any optional genre-specific lists into the system prompt as instructed in `1_foundational_cleanup.json`.
4.  **Provide your text:** Paste your text into the user input area.
5.  **Run the prompt:** Send the message and wait for the revised text.
6.  **Repeat for all stages:** Take the output from the previous stage and use it as the input for the next, repeating the process until you have completed all four stages.

### Automated Usage with n8n

The `n8n_gemini_workflow.json` file in this directory provides a pre-built n8n automation workflow to execute this 4-stage humanization pipeline seamlessly. n8n is a powerful, node-based automation tool that allows you to connect different services and APIs to create complex workflows.

**How it Works:**
The workflow is a visual representation of the 4-stage pipeline. Each node in the workflow performs a specific task:
-   **Read File Nodes:** These nodes load your input text and the necessary JSON prompt files into the workflow's memory.
-   **Google Generative AI Nodes:** These are the core processing nodes. Each is configured to call the Gemini API with the text from the previous step and the appropriate system prompt for that stage.
-   **Write File Node:** After the final phase, this node saves the fully humanized text to a new Markdown file.

**Setup Instructions:**
1.  **Place your AI-generated text:** Create a file named `input_text.md` in the same directory where you run n8n (or configure the 'Read Input File' node accordingly) and paste your AI-generated text into it.
2.  **Ensure JSON files are present:**
    *   The four Gemini phase JSON files (`1_foundational_cleanup.json`, `2_stylistic_narrative_enhancement.json`, `3_advanced_structural_statistical_humanization.json`, `4_dialogue_refinement.json`) must be in the `gemini/` subdirectory.
    *   The `master_prohibited_words.json`, `master_prohibited_words_romance.json` (optional), and `master_prohibited_words_erotica.json` (optional) files must be in the root directory (one level above `gemini/`).
3.  **Configure Google Generative AI API credentials:** In your n8n instance, set up your credentials for the Google Generative AI API. This is typically done under the "Credentials" section of n8n.
4.  **Import the workflow:** Import `n8n_gemini_workflow.json` into your n8n instance.
5.  **Run the workflow:** Execute the workflow.
6.  **Retrieve output:** The final humanized text will be written to `output_humanized_gemini.md` in the same directory as your `input_text.md`.

### Model Used:
*   `gemini-1.5-pro-latest` (or an equivalent powerful Gemini model suitable for text generation and complex instruction following).