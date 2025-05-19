


import os
import re

# Define the path to the Markdown file
md_file_path = r"/home/mgelvoleo/itlearntv/content/about.md"  # Replace with the actual path to your Markdown file

# Read the content of the Markdown file
with open(md_file_path, "r", encoding="utf-8") as f:
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
with open(md_file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Markdown file processed successfully.")