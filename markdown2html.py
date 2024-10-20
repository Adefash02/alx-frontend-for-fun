#!/usr/bin/env python3
import sys
import os

# Check if there are exactly two arguments
if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

# Get file names from arguments
markdown_file = sys.argv[1]
html_file = sys.argv[2]

# Check if the Markdown file exists
if not os.path.isfile(markdown_file):
    print(f"Missing {markdown_file}", file=sys.stderr)
    sys.exit(1)

# Read the Markdown file
with open(markdown_file, 'r') as md_file:
    content = md_file.read()

# Very basic conversion from markdown to HTML
# (just wraps the content in <p> tags for this example)
html_content = "<html>\n<body>\n"
for line in content.split('\n'):
    if line.strip():  # Avoid empty lines
        html_content += f"<p>{line}</p>\n"
html_content += "</body>\n</html>\n"

# Write the HTML content to the output file
with open(html_file, 'w') as html_output:
    html_output.write(html_content)

# Exit with success
sys.exit(0)

