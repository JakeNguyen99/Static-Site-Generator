import re

def markdown_to_blocks(markdown):
  blocks = re.split(r'\n\s*\n', markdown.strip())
  return blocks

def block_to_block_type(block):
  if re.match(r'^#{1,6} ', block):
    return 'heading'
  
  if re.match(r'^```', block):
    return 'code'
  
  if re.match(r'^> ', block):
    return 'quote'
  
  if re.match(r'^\* ', block) or re.match(r'^\- ', block):
    return 'unordered_list'
  
  if re.match(r'^\d{1}. ', block):
    return'ordered_list'
  
  return 'paragraph'
  
