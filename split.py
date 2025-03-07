import os
import re
import sys

def split_markdown(input_file, output_dir):
    """Splits a Markdown file into separate files at each `#` header."""
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Read the input Markdown file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split at each `#` header, keeping the header
    sections = re.split(r'(?=\n# )', content)  

    for i, section in enumerate(sections):
        if not section.strip():
            continue  # Skip empty sections
        
        # Extract title from first line
        lines = section.strip().split("\n")
        title = lines[0].strip("#").strip()
        
        # Create a filename from the title
        filename = re.sub(r'[^a-zA-Z0-9_-]', '_', title.lower()) + ".md"
        filepath = os.path.join(output_dir, filename)
        
        # Write to a new file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(section.strip() + "\n")
        
        print(f"Created: {filepath}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python split_md.py INPUT_FILE OUTPUT_DIR")
        sys.exit(1)

    input_file = sys.argv[1]
    output_dir = sys.argv[2]

    split_markdown(input_file, output_dir)

