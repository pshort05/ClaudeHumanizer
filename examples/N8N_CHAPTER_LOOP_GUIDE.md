# n8n Chapter Loop Workflow Guide

**ClaudeHumanizer - Automated Chapter-by-Chapter Processing with Claude Sonnet 4.5**

This n8n workflow processes book chapters sequentially through all 10 phases of the ClaudeHumanizer assembly line, looping through each chapter until all are complete.

---

## Features

✅ **Fully Automated**: Processes chapters sequentially without manual intervention
✅ **Claude Sonnet 4.5**: Uses optimal model for all phases
✅ **Correct Temperatures**: Each phase uses its recommended temperature setting
✅ **Master List Integration**: Phases 2 and 10 include master_prohibited_words.json
✅ **Optional Phase 9.5**: Statistical analysis can be included or skipped
✅ **Loop Management**: Automatically tracks progress and continues until all chapters complete
✅ **Detailed Results**: Returns original + humanized text for each chapter

---

## Prerequisites

### 1. n8n Installation

```bash
# Install n8n globally
npm install n8n -g

# OR use Docker
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n
```

### 2. Anthropic API Credentials

1. Get API key from https://console.anthropic.com/
2. In n8n, go to **Credentials** → **New Credential** → **Anthropic API**
3. Enter your API key and save
4. Note the credential ID for workflow configuration

### 3. ClaudeHumanizer Files

Ensure you have:
- All 10 phase JSON files (1-10)
- `9.5_statistical_analysis_hub.json` (optional phase)
- `master_prohibited_words.json`

---

## Installation

### Step 1: Import Workflow

1. Download `n8n_chapter_loop_workflow.json`
2. Open n8n (http://localhost:5678)
3. Click **Workflows** → **Import from File**
4. Select the downloaded JSON file
5. Click **Import**

### Step 2: Configure File Paths

Update ALL file path nodes with your actual ClaudeHumanizer directory:

**Nodes to update:**
1. **Load Master Prohibited Words** - Update path to `master_prohibited_words.json`
2. **Load Phase 1 Prompt** - Update path to `1_grammar_foundation.json`
3. **Load Phase 2 Prompt** - Update path to `2_ai_word_cleaning.json`
4. **Load Phase 3 Prompt** - Update path to `3_overwritten_language_reduction.json`
5. **Load Phase 4 Prompt** - Update path to `4_sensory_enhancement.json`
6. **Load Phase 5 Prompt** - Update path to `5_subtlety_creation.json`
7. **Load Phase 6 Prompt** - Update path to `6_dialogue_enhancement.json`
8. **Load Phase 7 Prompt** - Update path to `7_weak_language_cleanup.json`
9. **Load Phase 8 Prompt** - Update path to `8_strategic_imperfections.json`
10. **Load Phase 9 Prompt** - Update path to `9_final_verification.json`
11. **Load Phase 9.5 Prompt** - Update path to `9.5_statistical_analysis_hub.json`
12. **Load Phase 10 Prompt** - Update path to `10_final_ai_word_sweep.json`

**Example path format:**
```
/home/username/ClaudeHumanizer/1_grammar_foundation.json
```

### Step 3: Configure Anthropic Credentials

Update ALL Anthropic nodes (Phases 1-10 + 9.5):

1. Click each "Phase X" node
2. In the **Credentials** section, select your Anthropic API credential
3. Save each node

**Nodes to update:**
- Phase 1 - Grammar Foundation
- Phase 2 - AI Word Cleaning
- Phase 3 - Overwritten Language
- Phase 4 - Sensory Enhancement
- Phase 5 - Subtlety Creation
- Phase 6 - Dialogue Enhancement
- Phase 7 - Weak Language Cleanup
- Phase 8 - Strategic Imperfections
- Phase 9 - Final Verification
- Phase 9.5 - Statistical Analysis (optional)
- Phase 10 - Final AI Word Sweep

### Step 4: Activate Workflow

1. Click **Active** toggle in top-right corner
2. Workflow is now ready to receive requests

---

## Usage

### Input Format

Send a POST request to the webhook URL with this JSON structure:

```json
{
  "chapters": [
    {
      "number": 1,
      "title": "Chapter One: The Beginning",
      "text": "Your chapter text here..."
    },
    {
      "number": 2,
      "title": "Chapter Two: The Journey",
      "text": "Your chapter text here..."
    },
    {
      "number": 3,
      "title": "Chapter Three: The Discovery",
      "text": "Your chapter text here..."
    }
  ],
  "include_phase_9_5": false
}
```

**Fields:**
- `chapters` (array, required): Array of chapter objects
  - `number` (integer): Chapter number
  - `title` (string): Chapter title
  - `text` (string): Full chapter text
- `include_phase_9_5` (boolean, optional): Include statistical analysis phase (default: false)

### Example Request (cURL)

```bash
curl -X POST https://your-n8n-instance.com/webhook/claudehumanizer-chapters \
  -H "Content-Type: application/json" \
  -d '{
    "chapters": [
      {
        "number": 1,
        "title": "Chapter One",
        "text": "It was a dark and stormy night. The protagonist delved into the mystery..."
      },
      {
        "number": 2,
        "title": "Chapter Two",
        "text": "The investigation continued. Furthermore, the detective discovered..."
      }
    ],
    "include_phase_9_5": false
  }'
```

### Example Request (Python)

```python
import requests
import json

url = "https://your-n8n-instance.com/webhook/claudehumanizer-chapters"

payload = {
    "chapters": [
        {
            "number": 1,
            "title": "Chapter One: The Awakening",
            "text": "Your AI-generated chapter text here..."
        },
        {
            "number": 2,
            "title": "Chapter Two: The Discovery",
            "text": "Your AI-generated chapter text here..."
        }
    ],
    "include_phase_9_5": False  # Set to True for statistical analysis
}

response = requests.post(url, json=payload)
result = response.json()

print(json.dumps(result, indent=2))
```

### Example Request (JavaScript)

```javascript
const axios = require('axios');

const url = 'https://your-n8n-instance.com/webhook/claudehumanizer-chapters';

const payload = {
  chapters: [
    {
      number: 1,
      title: 'Chapter One',
      text: 'Your AI-generated chapter text here...'
    },
    {
      number: 2,
      title: 'Chapter Two',
      text: 'Your AI-generated chapter text here...'
    }
  ],
  include_phase_9_5: false
};

axios.post(url, payload)
  .then(response => {
    console.log(JSON.stringify(response.data, null, 2));
  })
  .catch(error => {
    console.error('Error:', error);
  });
```

---

## Output Format

### Successful Completion

When all chapters are processed, you'll receive:

```json
{
  "status": "completed",
  "total_chapters": 3,
  "processed_chapters": [
    {
      "number": 1,
      "title": "Chapter One: The Beginning",
      "original_text": "Original AI-generated text...",
      "humanized_text": "Humanized text after all 10 phases...",
      "processed_at": "2025-10-26T14:30:00.000Z"
    },
    {
      "number": 2,
      "title": "Chapter Two: The Journey",
      "original_text": "Original AI-generated text...",
      "humanized_text": "Humanized text after all 10 phases...",
      "processed_at": "2025-10-26T14:35:00.000Z"
    },
    {
      "number": 3,
      "title": "Chapter Three: The Discovery",
      "original_text": "Original AI-generated text...",
      "humanized_text": "Humanized text after all 10 phases...",
      "processed_at": "2025-10-26T14:40:00.000Z"
    }
  ],
  "completed_at": "2025-10-26T14:40:00.000Z"
}
```

### No Chapters Provided

```json
{
  "status": "no_chapters",
  "message": "No chapters to process"
}
```

---

## How the Loop Works

### Processing Flow

1. **Webhook receives chapters array**
2. **Initialize variables**:
   - `chapters`: Full array of chapters
   - `total_chapters`: Count
   - `current_chapter_index`: Starts at 0
   - `processed_chapters`: Empty array for results
3. **Load all prompt files** (done once at start)
4. **Enter chapter loop**:
   - Get current chapter from array
   - Process through Phase 1
   - Process through Phase 2 (with master list)
   - Process through Phase 3
   - Process through Phase 4
   - Process through Phase 5
   - Process through Phase 6 (temperature 1.0)
   - Process through Phase 7
   - Process through Phase 8
   - Process through Phase 9
   - **IF** `include_phase_9_5 = true`: Process through Phase 9.5
   - Process through Phase 10 (with master list)
   - Package result (chapter number, title, original + humanized text)
   - Add to `processed_chapters` array
   - Increment `current_chapter_index`
5. **Check if more chapters exist**:
   - **YES**: Loop back to step 4 with next chapter
   - **NO**: Return final results with all processed chapters

### Loop Control

The workflow uses n8n's **Loop Over Items** pattern:

- **Continue Loop?** node checks if `current_chapter_index < total_chapters`
- **True path**: Loops back to "Get Current Chapter" node
- **False path**: Proceeds to "Prepare Final Response"

This creates an automatic loop that processes each chapter sequentially until complete.

---

## Monitoring Progress

### n8n Execution View

1. Open the workflow in n8n
2. Click **Executions** tab
3. View the current running execution
4. Each phase completion will show as a green checkmark
5. Watch the loop progress through chapters

### Execution Time Estimates

**Per Chapter (approximate):**
- Phase 1 (Grammar): ~10-15 seconds
- Phase 2 (AI Words): ~15-20 seconds
- Phase 3 (Purple Prose): ~10-15 seconds
- Phase 4 (Sensory): ~15-20 seconds
- Phase 5 (Subtlety): ~15-20 seconds
- Phase 6 (Dialogue): ~20-30 seconds (temp 1.0 = more creative)
- Phase 7 (Weak Language): ~10-15 seconds
- Phase 8 (Imperfections): ~20-25 seconds
- Phase 9 (Verification): ~10-15 seconds
- Phase 9.5 (Statistical): ~15-20 seconds (optional)
- Phase 10 (Final Sweep): ~10-15 seconds

**Total per chapter**: ~2.5-4 minutes (without Phase 9.5), ~3-4.5 minutes (with Phase 9.5)

**Example book (20 chapters)**: ~50-90 minutes total

---

## Cost Estimates

### Claude Sonnet 4.5 Pricing
- **Input**: $3 per 1M tokens
- **Output**: $15 per 1M tokens

### Estimated Costs per Chapter

**Assumptions:**
- Chapter length: ~3,000 words (~4,000 tokens)
- Each phase adds ~10-15% to token count
- Final output: ~5,500 tokens

**Cost per chapter (estimated):**
- Input tokens (10 phases): ~50,000 tokens = $0.15
- Output tokens (10 phases): ~55,000 tokens = $0.83
- **Total per chapter**: ~$0.98-1.20

**Cost per book (20 chapters)**: ~$20-25

**With Phase 9.5 included**: Add ~10-15% = ~$22-29 per book

### Cost Optimization Options

To reduce costs:
1. **Skip Phase 9.5**: Set `include_phase_9_5: false` (saves 10-15%)
2. **Use hybrid strategy**: See TECHNICAL_REFERENCE.md for Gemini 2.5 Pro options
3. **Process fewer chapters**: Test with 2-3 chapters first
4. **Batch by priority**: Process high-priority chapters first

---

## Troubleshooting

### Common Issues

**1. Workflow doesn't start**
- Check webhook is activated
- Verify webhook URL is correct
- Ensure JSON payload is properly formatted

**2. Phase fails with "File not found"**
- Update file paths in all "Load Phase X Prompt" nodes
- Ensure absolute paths are used
- Check file permissions

**3. Anthropic API errors**
- Verify API key is correct in credentials
- Check API rate limits (Claude Sonnet 4.5: 50 requests/min)
- Ensure sufficient API credits

**4. Loop doesn't continue**
- Check "Update Loop State" node for errors
- Verify chapter array structure is correct
- Review "Continue Loop?" condition logic

**5. Out of memory errors**
- Reduce chapter count per request
- Process smaller batches (5-10 chapters at a time)
- Increase n8n memory allocation

### Debug Mode

Enable debug output:

1. Edit "Package Chapter Result" node
2. Add additional fields:
   ```json
   {
     "debug_info": {
       "phase_1_length": "={{ $('Phase 1 - Grammar Foundation').item.json.content[0].text.length }}",
       "phase_10_length": "={{ $('Phase 10 - Final AI Word Sweep').item.json.content[0].text.length }}",
       "phases_completed": 10
     }
   }
   ```

### Viewing Intermediate Results

To see output from each phase:

1. Click any Phase node
2. Click **Run Node** (test mode)
3. View output in right panel
4. Compare input vs output for that phase

---

## Advanced Configuration

### Custom Temperature Settings

To modify temperatures for specific phases:

1. Click the Phase node (e.g., "Phase 6 - Dialogue Enhancement")
2. Find **Options** → **Temperature**
3. Modify value (current: 1.0 for Phase 6)
4. Save node

**Recommended temperatures** (already configured):
- Phases 1, 7, 9: 0.2 (precision)
- Phase 2: 0.4 (pattern matching)
- Phase 3: 0.3 (literary judgment)
- Phase 4: 0.7 (creative)
- Phase 5: 0.5 (subtlety)
- Phase 6: 1.0 (dialogue naturalness - CRITICAL)
- Phase 8: 0.9 (rhythm variation)
- Phase 9.5: 0.4 (statistical precision)
- Phase 10: 0.3 (surgical cleanup)

### Adding Chapter Metadata

Extend the input format:

```json
{
  "chapters": [
    {
      "number": 1,
      "title": "Chapter One",
      "text": "Chapter content...",
      "metadata": {
        "word_count": 3500,
        "genre": "mystery",
        "pov": "first-person"
      }
    }
  ]
}
```

Update "Package Chapter Result" node to include metadata in output.

### Parallel Processing (Advanced)

For faster processing, you can modify the workflow to process multiple chapters in parallel:

**Warning**: This will:
- Use more API requests simultaneously
- May hit rate limits
- Increase cost but reduce total time

See TECHNICAL_REFERENCE.md for parallel processing strategies.

---

## Integration Examples

### Python Script - Full Book Processing

```python
import requests
import json
from pathlib import Path

def process_book(chapters, n8n_url, include_stats=False):
    """
    Process a full book through ClaudeHumanizer.

    Args:
        chapters: List of dicts with 'number', 'title', 'text'
        n8n_url: Your n8n webhook URL
        include_stats: Include Phase 9.5 statistical analysis

    Returns:
        Dict with processed chapters
    """
    payload = {
        "chapters": chapters,
        "include_phase_9_5": include_stats
    }

    print(f"Processing {len(chapters)} chapters...")
    print(f"Estimated time: {len(chapters) * 3} minutes")
    print(f"Estimated cost: ${len(chapters) * 1.10:.2f}")

    response = requests.post(n8n_url, json=payload)

    if response.status_code == 200:
        result = response.json()
        if result['status'] == 'completed':
            print(f"✓ Successfully processed {result['total_chapters']} chapters")
            return result
        else:
            print(f"⚠ Warning: {result}")
            return result
    else:
        print(f"✗ Error: {response.status_code}")
        print(response.text)
        return None

def load_chapters_from_files(chapter_dir):
    """Load chapters from individual text files."""
    chapters = []
    chapter_files = sorted(Path(chapter_dir).glob("chapter_*.txt"))

    for i, filepath in enumerate(chapter_files, start=1):
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()

        chapters.append({
            "number": i,
            "title": f"Chapter {i}",
            "text": text
        })

    return chapters

# Example usage
if __name__ == "__main__":
    n8n_webhook = "https://your-n8n-instance.com/webhook/claudehumanizer-chapters"

    # Load chapters from files
    chapters = load_chapters_from_files("./raw_chapters")

    # Process through ClaudeHumanizer
    result = process_book(chapters, n8n_webhook, include_stats=False)

    # Save results
    if result:
        for chapter in result['processed_chapters']:
            output_file = f"humanized_chapter_{chapter['number']}.txt"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(chapter['humanized_text'])
            print(f"Saved: {output_file}")
```

### Node.js Script - Batch Processing

```javascript
const axios = require('axios');
const fs = require('fs').promises;
const path = require('path');

async function processBook(chapters, n8nUrl, includeStats = false) {
  const payload = {
    chapters: chapters,
    include_phase_9_5: includeStats
  };

  console.log(`Processing ${chapters.length} chapters...`);
  console.log(`Estimated time: ${chapters.length * 3} minutes`);
  console.log(`Estimated cost: $${(chapters.length * 1.10).toFixed(2)}`);

  try {
    const response = await axios.post(n8nUrl, payload);

    if (response.data.status === 'completed') {
      console.log(`✓ Successfully processed ${response.data.total_chapters} chapters`);
      return response.data;
    } else {
      console.log(`⚠ Warning:`, response.data);
      return response.data;
    }
  } catch (error) {
    console.error('✗ Error:', error.message);
    return null;
  }
}

async function loadChaptersFromFiles(chapterDir) {
  const chapters = [];
  const files = await fs.readdir(chapterDir);
  const chapterFiles = files
    .filter(f => f.startsWith('chapter_') && f.endsWith('.txt'))
    .sort();

  for (let i = 0; i < chapterFiles.length; i++) {
    const filepath = path.join(chapterDir, chapterFiles[i]);
    const text = await fs.readFile(filepath, 'utf-8');

    chapters.push({
      number: i + 1,
      title: `Chapter ${i + 1}`,
      text: text
    });
  }

  return chapters;
}

// Example usage
(async () => {
  const n8nWebhook = 'https://your-n8n-instance.com/webhook/claudehumanizer-chapters';

  // Load chapters
  const chapters = await loadChaptersFromFiles('./raw_chapters');

  // Process
  const result = await processBook(chapters, n8nWebhook, false);

  // Save results
  if (result && result.processed_chapters) {
    for (const chapter of result.processed_chapters) {
      const outputFile = `humanized_chapter_${chapter.number}.txt`;
      await fs.writeFile(outputFile, chapter.humanized_text, 'utf-8');
      console.log(`Saved: ${outputFile}`);
    }
  }
})();
```

---

## Best Practices

### 1. Test with Small Batches First

Start with 2-3 chapters to:
- Verify configuration
- Check output quality
- Estimate costs and timing
- Identify any issues

### 2. Monitor API Usage

- Track Claude API usage in Anthropic Console
- Set up billing alerts
- Monitor rate limits (50 requests/min for Sonnet 4.5)

### 3. Save Intermediate Results

Modify workflow to save after each chapter:
- Add "Write Binary File" node after "Package Chapter Result"
- Save to `/processed_chapters/chapter_X.json`
- Provides backup if workflow fails mid-process

### 4. Handle Long Chapters

For chapters >8,000 words:
- Consider splitting into scenes
- Process scenes separately
- Recombine after humanization

### 5. Quality Checks

After processing:
- Run sample chapters through AI detectors
- Spot-check Phase 6 dialogue for naturalness
- Verify Phase 10 removed all prohibited words
- Compare Phase 9 output quality

---

## Support

For issues or questions:

1. **Workflow Issues**: Check n8n community forums
2. **ClaudeHumanizer Questions**: See USAGE_GUIDE.md and TECHNICAL_REFERENCE.md
3. **API Issues**: Contact Anthropic support
4. **Bug Reports**: Create issue at ClaudeHumanizer repository

---

## License

Same license as ClaudeHumanizer project.

**Version**: 1.0
**Last Updated**: 2025-10-26
**Optimized For**: Claude Sonnet 4.5
**n8n Version**: 1.0+
