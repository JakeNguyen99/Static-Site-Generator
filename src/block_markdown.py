import re

def markdown_to_blocks(markdown):
  blocks = re.split(r'\n\s*\n', markdown.strip())
  return blocks

