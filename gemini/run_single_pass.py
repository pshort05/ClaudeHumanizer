import os
import json
import google.generativeai as genai
import argparse

def load_file(filepath):
    """Loads text from a file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def run_single_pass_humanizer(input_file, output_file, api_key_env_var="GEMINI_API_KEY"):
    """
    Runs the single-pass Gemini humanizer on a given input file.
    """
    
    # 1. Setup API
    api_key = os.environ.get(api_key_env_var)
    if not api_key:
        print(f"Error: {api_key_env_var} environment variable not set.")
        return
    
    genai.configure(api_key=api_key)
    
    # Use Gemini 1.5 Pro for best results with complex instructions
    model = genai.GenerativeModel('gemini-1.5-pro-latest') 

    # 2. Load Resources
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir) # Assuming script is in gemini/ 
    
    prompt_path = os.path.join(script_dir, "single_pass_humanizer_prompt.md")
    prohibited_words_path = os.path.join(project_root, "master_prohibited_words.json")
    
    if not os.path.exists(prompt_path):
        print(f"Error: Prompt file not found at {prompt_path}")
        return
    if not os.path.exists(prohibited_words_path):
        print(f"Error: Prohibited words file not found at {prohibited_words_path}")
        return

    print("Loading resources...")
    base_prompt = load_file(prompt_path)
    prohibited_words_content = load_file(prohibited_words_path)
    
    # 3. Construct System Prompt
    # We inject the prohibited words list into the context as requested by the prompt structure
    system_instruction = base_prompt + "\n\n<reference_file name='master_prohibited_words.json'>\n" + prohibited_words_content + "\n</reference_file>"

    # 4. Load Input Text
    if not os.path.exists(input_file):
        print(f"Error: Input file not found at {input_file}")
        return
        
    user_text = load_file(input_file)
    print(f"Processing '{input_file}' ({len(user_text)} chars)...")

    # 5. Generate
    try:
        response = model.generate_content(
            contents=user_text,
            generation_config=genai.types.GenerationConfig(
                temperature=0.7, # Slightly creative but controlled
                system_instruction=system_instruction
            )
        )
        
        # 6. Save Output
        if response.text:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(response.text)
            print(f"Success! Humanized text saved to: {output_file}")
        else:
            print("Error: Empty response from model.")
            print(response.prompt_feedback)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the Gemini Single-Pass Humanizer")
    parser.add_argument("input_file", help="Path to the markdown file to humanize")
    parser.add_argument("--output", "-o", default="humanized_output.md", help="Path for the output file")
    
    args = parser.parse_args()
    
    run_single_pass_humanizer(args.input_file, args.output)
