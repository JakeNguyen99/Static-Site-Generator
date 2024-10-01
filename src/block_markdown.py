import re
from htmlnode import HTMLNode, ParentNode , LeafNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

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
  
def text_to_leaf_node(text):
  return [node.to_html_node() for node in text_to_textnodes(text)]
  
def markdown_to_html_node(markdown):
  nodes = []
  blocks = markdown_to_blocks(markdown)
  for block in blocks:
    block_type = block_to_block_type(block)
    if block_type == block_type_heading:
      hashes, content = block(" ", 1)
      node = ParentNode(f"h{len(hashes)}", text_to_leaf_node(content))
    elif block_type == block_type_code:
      content = block[3:-3].strip()
      node = ParentNode("pre", [ParentNode("code", text_to_leaf_node(content))])
    elif block_type == block_type_quote:
      lines = block.split("\n")
      content = "\n".join(map(lambda line: line.removeprefix("> "), lines))
      node = ParentNode("blockquote", text_to_leaf_node(content))
    elif block_type == block_type_unordered_list:
      lines = block.split("\n")
      list_items = []
      for line in lines:
        line_content = line[2:]
        line_nodes = text_to_leaf_node(line_content)
        list_items.append(ParentNode("li", line_nodes))
      node = ParentNode("ul", list_items)
    elif block_type == block_type_ordered_list:
      lines = block.split("\n")
      list_items = []
      for i, line in enumerate(lines):
        line_content = line.removeprefix(f"{i+1}. ")
        line_nodes = text_to_leaf_node(line_content)
        list_items.append(ParentNode("li", line_nodes))
      node = ParentNode("ol", list_items)
    elif block_type == block_type_paragraph:
      node = ParentNode("p", text_to_leaf_node(block))
    else:
      raise ValueError("Invalid block")
    nodes.append(node)
  return ParentNode("div", nodes)
