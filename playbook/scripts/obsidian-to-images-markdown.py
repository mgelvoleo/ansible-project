import os
import re

# Define the path to the Hugo content directory
content_dir = r"/home/mgelvoleo/itlearntv/content"  # Replace with the actual path to your Hugo content directory

# Function to process a single Markdown file
def process_markdown_file(file_path):
    # Read the content of the Markdown file
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find all image references in the format ![[images/1.png]]
    image_references = re.findall(r'!\[\[([^\]]+)\]\]', content)

    # Replace each image reference with the new syntax ![My Image](/images/1.png)
    for image_path in image_references:
        # Ensure the image_path does not already start with a forward slash
        if image_path.startswith('/'):
            image_path = image_path[1:]  # Remove the leading slash

        # Construct the new Markdown image syntax with a leading forward slash
        new_image_syntax = f'![My Image](/{image_path})'

        # Replace the old syntax with the new one
        old_image_syntax = f'![[{image_path}]]'
        content = content.replace(old_image_syntax, new_image_syntax)

    # Write the updated content back to the Markdown file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Processed: {file_path}")

# Traverse the content directory and process all Markdown files
for root, dirs, files in os.walk(content_dir):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            process_markdown_file(file_path)

print("All Markdown files processed successfully.")