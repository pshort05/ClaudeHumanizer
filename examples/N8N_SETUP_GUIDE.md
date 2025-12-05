# n8n ClaudeHumanizer Setup & Usage Guide

## Overview

This guide walks you through setting up and running the ClaudeHumanizer v3.3.0 automation in n8n. The workflow processes AI-generated text through 11 sequential phases, transforming it into natural, human-like writing.

**What the workflow does:**
1. Reads your AI-generated text from `input_text.md`
2. Processes it through 11 specialized phases (grammar → word cleaning → prose reduction → sensory enhancement → subtlety → dialogue → weak language → imperfections → verification → statistics → final sweep)
3. Writes the humanized output to `output_humanized.md`
4. Returns a completion summary

---

## Prerequisites

Before starting, ensure you have:

- **n8n Instance**: Self-hosted or cloud version (v1.0.0+)
- **Anthropic API Key**: From https://console.anthropic.com
- **Local Folder**: A directory where you'll place all files
- **Text Editor**: For creating and editing input files (VS Code, Notepad++, etc.)

---

## Step 1: Obtain Your Anthropic API Key

1. Go to [Anthropic Console](https://console.anthropic.com)
2. Sign in or create an account
3. Navigate to **API Keys** section
4. Click **Create Key**
5. Copy the generated key (starts with `sk-ant-`)
6. **Keep this safe** - you'll need it in n8n

---

## Step 2: Set Up n8n Credentials

### In n8n Dashboard:

1. **Navigate to Credentials**
   - Click the gear icon (⚙️) in the bottom left
   - Select **Credentials**

2. **Create New Credential**
   - Click **Create New** button
   - Search for "Anthropic"
   - Select **Anthropic API**

3. **Enter Your API Key**
   - Paste your API key from Step 1
   - Name it: `ClaudeHumanizer API` (or your preferred name)
   - Click **Save**

4. **Verify Connection**
   - n8n will automatically test the connection
   - You should see a green checkmark confirming success

---

## Step 3: Prepare Your File Directory

Create a working directory for your ClaudeHumanizer workflow. This directory will contain:

```
working_directory/
├── input_text.md                           (create manually)
├── 1_grammar_foundation.json               (copy from ClaudeHumanizer)
├── 2_ai_word_cleaning.json
├── 3_overwritten_language_reduction.json
├── 4_sensory_enhancement.json
├── 5_subtlety_creation.json
├── 6_dialogue_enhancement.json
├── 7_weak_language_cleanup.json
├── 8_strategic_imperfections.json
├── 9_final_verification.json
├── 9.5_statistical_analysis_hub.json
├── 10_final_ai_word_sweep.json
├── master_prohibited_words.json            (required)
├── master_prohibited_words_romance.json    (optional)
├── master_prohibited_words_erotica.json    (optional)
└── output_humanized.md                     (created automatically)
```

### Files to Copy

From the ClaudeHumanizer repository, copy these files to your working directory:

**Required Files:**
- All 11 phase JSON files (1 through 10, plus 9.5)
- `master_prohibited_words.json`

**Optional Files** (for genre-specific filtering):
- `master_prohibited_words_romance.json` - Applied only if author indicates romance content
- `master_prohibited_words_erotica.json` - Applied only if author indicates erotica content

---

## Step 4: Import the n8n Workflow

### Option A: Import from JSON

1. **In n8n**, click **+ New** → **Workflow**
2. Click the three dots (⋯) menu → **Import from file**
3. Select the `n8n_workflow_sample.json` file from ClaudeHumanizer examples
4. Click **Import**

### Option B: Create from Scratch

If you prefer to build it manually, see the **Workflow Architecture** section below (Advanced).

---

## Step 5: Configure Workflow Settings

After importing the workflow:

1. **Select Anthropic Credential**
   - Click any of the Phase nodes (Phase 1, Phase 2, etc.)
   - Under "Authentication," select the credential you created in Step 2
   - Repeat for all 11 phase nodes

2. **Set Working Directory** (if needed)
   - Most n8n installations default to the current directory
   - If your files are in a different location, update file paths in the "Read Input File" and "Write Output File" nodes

3. **Test Phase Nodes** (optional)
   - Click any phase node → **Test Step**
   - n8n will verify the connection to Anthropic API

---

## Step 6: Create Your Input File

Before running the workflow, create your input file:

1. **Create `input_text.md`**
   - In your working directory, create a new file named exactly `input_text.md`
   - Add your AI-generated text to this file
   - Save as UTF-8 (default in most editors)

2. **Example Input** (minimal test):
   ```markdown
   # My Story

   The sun filtered brilliantly through the diaphanous curtains, casting
   luminescent patterns across the room. She felt an overwhelming surge of
   emotions crashing through her consciousness. The weight of his words hung
   heavily in the air between them, suspended like a tangible entity.
   ```

3. **For Longer Texts**
   - Copy your entire document into `input_text.md`
   - The workflow can handle texts up to ~8,000 words (adjust maxTokens in nodes if needed)

---

## Step 7: Run the Workflow

### Execution

1. **In n8n**, with your workflow open, click **Execute Workflow**
   - Or press `Ctrl+Enter` (Windows/Linux) or `Cmd+Enter` (Mac)

2. **Monitor Progress**
   - Watch the node execution flow in real-time
   - Green checkmarks indicate successful completion
   - Red warnings indicate errors (see Troubleshooting below)

3. **Execution Time**
   - Full workflow typically takes **2-5 minutes** depending on text length
   - Each phase processes sequentially
   - Phase 9.5 (statistics) takes longest (~20-30 seconds)

### View Results

After execution completes:

1. **Check Output File**
   - Look in your working directory for `output_humanized.md`
   - This contains your fully humanized text

2. **Review Execution Log**
   - Click the **Execution** tab in n8n
   - View detailed output from each phase
   - See the `Completion Summary` node for final metrics

---

## Step 8: Optional - Genre-Specific Filtering

If you want the workflow to apply genre-specific pattern filtering:

### For Romance Content

1. The workflow automatically loads `master_prohibited_words_romance.json`
2. **To apply romance-specific filtering**, you would need to:
   - Modify Phase 10's instructions to indicate romance content
   - OR manually specify in the workflow context that genre filtering is desired
   - Currently, romance patterns are loaded but not applied automatically (author control)

### For Erotica Content

Similar to romance - the list is loaded but only applied if explicitly requested.

**Note**: As designed, genre-specific filtering requires explicit author indication. To enable automatic filtering:
- Edit Phase 10 node's system message
- Add a condition that checks for genre indicators in the input text
- This requires custom n8n JavaScript/expression knowledge

---

## Workflow Architecture

### Phase Processing Order

```
Input File → Phase 1 → Phase 2 → Phase 3 → Phase 4 → Phase 5 →
Phase 6 → Phase 7 → Phase 8 → Phase 9 → Phase 9.5 → Phase 10 → Output File
```

### Phase Domains

| Phase | What It Does | Temperature |
|-------|-------------|-------------|
| **1** | Grammar errors only | 0.2 |
| **2** | AI vocabulary removal | 0.2 |
| **3** | Purple prose & nominalization | 0.3 |
| **4** | Sensory enhancement | 0.7 |
| **5** | Subtlety creation | 0.5 |
| **6** | Dialogue enhancement | 1.0 |
| **7** | Weak language cleanup | 0.2 |
| **8** | Strategic imperfections | 0.9 |
| **9** | Pattern detection verification | 0.2 |
| **9.5** | Statistical analysis (optional) | 0.4 |
| **10** | Final AI word sweep | 0.2 |

### Node Types

**File I/O Nodes:**
- `Read Input File` - Reads `input_text.md`
- `Load Master Prohibited Words` - Loads word list
- `Load Phase [X] Prompt` - Loads phase instructions
- `Write Output File` - Writes to `output_humanized.md`

**Processing Nodes:**
- `Phase 1-10` - Anthropic API calls (Claude Sonnet 4.5)
- `Phase 9.5` - Optional statistical analysis

**Completion Node:**
- `Completion Summary` - Returns success/failure status

---

## Troubleshooting

### Error: "File not found"

**Problem**: Workflow can't find `input_text.md`

**Solutions:**
1. Verify `input_text.md` exists in the working directory
2. Check filename is exactly `input_text.md` (case-sensitive on Linux)
3. Verify file is not empty (minimum 10 characters needed)
4. Check file encoding is UTF-8

### Error: "Invalid API key"

**Problem**: Anthropic credential isn't working

**Solutions:**
1. Verify API key is correct (should start with `sk-ant-`)
2. Check key hasn't been revoked in Anthropic console
3. Ensure API key has not expired (check Anthropic dashboard)
4. Try re-entering the key in n8n credentials

### Error: "Context length exceeded"

**Problem**: Text is too long for Claude

**Solutions:**
1. Reduce input text length (aim for <8000 words)
2. In Phase nodes, increase `maxTokens` (currently 8192)
3. Or split text into multiple runs (process in chunks)

### Error: "Rate limit exceeded"

**Problem**: Too many API calls to Anthropic

**Solutions:**
1. Wait 1-2 minutes before running workflow again
2. Check Anthropic API usage in their dashboard
3. Verify you haven't hit your monthly quota

### Workflow Runs but Output is Incomplete

**Problem**: `output_humanized.md` exists but has truncated content

**Solutions:**
1. Check the `Write Output File` node output in n8n logs
2. Increase `maxTokens` in Phase 10 node
3. Verify input text isn't too long (>10,000 words)

### Phase Nodes Show Errors

**Problem**: Individual phase processing fails

**Solutions:**
1. Click the failed phase node to see error details
2. Most errors are due to file loading issues
3. Verify all phase JSON files are in the working directory
4. Check JSON files are valid (use a JSON validator online)

---

## Advanced Usage

### Custom Temperature Settings

To adjust how creative or deterministic each phase is:

1. Click a Phase node (e.g., "Phase 4 - Sensory Enhancement")
2. Find the `temperature` field in options
3. Adjust value:
   - **0.0-0.3**: Very deterministic (grammar, facts)
   - **0.4-0.6**: Balanced (word choices, descriptions)
   - **0.7-0.9**: Creative (dialogue, variations)
   - **1.0**: Most creative (for dialogue, unrestricted variation)

### Batch Processing

To process multiple documents:

1. Create multiple input files: `input_1.md`, `input_2.md`, etc.
2. Modify the "Read Input File" node to loop through files
3. Requires n8n Loop extension

### Custom Phase Prompts

To modify how a phase works:

1. Edit the corresponding JSON file (e.g., `2_ai_word_cleaning.json`)
2. Update the phase instructions
3. Update the version number (e.g., 2.2.1 → 2.2.2)
4. Save and reload in n8n

---

## Best Practices

### Before Running

- ✅ Test your API key connection first
- ✅ Validate all phase JSON files are present
- ✅ Backup your original input text
- ✅ Keep input text between 500-8000 words for best results
- ✅ Test with a small sample first

### During Execution

- ⏸️ Don't modify input file while workflow is running
- 📊 Monitor execution progress in n8n
- 🔍 Check node outputs if execution fails

### After Completion

- ✅ Review the output file for quality
- ✅ Check completion summary for any warnings
- ✅ Keep execution logs for debugging if needed
- ✅ Back up your output before re-running

### Performance Tips

- Use shorter texts for faster processing (1000-2000 words)
- Run during off-peak hours if on a shared n8n instance
- Increase node concurrency in n8n settings if available
- Consider running Phase 9.5 (statistics) manually if not needed

---

## FAQ

**Q: Can I use this with Claude Opus or Claude Haiku?**
- A: The workflow is optimized for Claude Sonnet 4.5. Other models may produce different results. You can change the model in any Phase node, but quality may vary.

**Q: How long does a full run take?**
- A: Typically 2-5 minutes for texts up to 3000 words. Longer texts take proportionally longer.

**Q: Can I skip phases?**
- A: Yes, but not recommended. Each phase builds on the previous one. If you want to skip Phase 9.5 (statistics), you can disconnect it, but all other phases should run in order.

**Q: What if my text has dialogue?**
- A: Phases are designed to preserve dialogue (in quotation marks). Phase 6 specifically enhances dialogue naturalness. Other phases skip quoted text.

**Q: Can I use this for non-English text?**
- A: The system is optimized for English. Other languages may work but haven't been extensively tested.

**Q: How do I know if the output is better?**
- A: Compare original vs. humanized text manually. Check for:
  - Removed repetitive phrases
  - More natural dialogue
  - Better pacing and rhythm
  - Eliminated AI patterns

**Q: Can I schedule this to run automatically?**
- A: Yes! n8n supports scheduled workflows. Set a trigger to run on a schedule instead of manually.

**Q: What about cost?**
- A: You pay Anthropic's API rates (typically $0.003-0.015 per 1K input tokens, $0.015-0.06 per 1K output tokens). A full humanization run typically costs $0.05-0.20 depending on text length.

---

## Next Steps

1. **Set up your working directory** (Step 3)
2. **Create your input file** (Step 6)
3. **Run the workflow** (Step 7)
4. **Review the output** in `output_humanized.md`
5. **Iterate and refine** by adjusting phase temperatures or custom prompts

---

## Support & Resources

- **n8n Documentation**: https://docs.n8n.io
- **Anthropic API Docs**: https://docs.anthropic.com
- **ClaudeHumanizer Repository**: See CLAUDE.md for detailed phase documentation
- **GitHub Issues**: Report bugs in the ClaudeHumanizer repository

---

## Version Information

- **Workflow Version**: 3.3.0
- **Last Updated**: 2025-12-04
- **Claude Model**: Claude Sonnet 4.5 (claude-sonnet-4-5-20250929)
- **n8n Compatibility**: v1.0.0+

---

## Workflow Optimizations (v3.3.0)

This workflow includes the latest ClaudeHumanizer v3.3.0 optimizations:

- ✨ **JSON File Optimization**: All phase files optimized with 23.5% size reduction
- 🎯 **Genre-Specific Lists**: Optional romance and erotica pattern detection (author-controlled)
- 📄 **STYLE_GUIDE Integration**: References one-page writing style guide for consistency
- 🚀 **Performance**: Faster loading and parsing with compressed JSON structure
- 📊 **Complete Chaining**: True assembly line with each phase feeding into the next

All functionality preserved with only structure and verbosity compressed.

---

## License & Attribution

ClaudeHumanizer v3.3.0 - Text humanization system for AI-generated content
Developed with [Claude Code](https://claude.com/claude-code)

For full project documentation, see the ClaudeHumanizer repository.
