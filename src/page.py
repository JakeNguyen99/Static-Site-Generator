import re
import os
from block_markdown import block_to_block_type, markdown_to_blocks, markdown_to_html_node


def extract_title(markdown):
  blocks = markdown_to_blocks(markdown)
  for block in blocks:
    if re.match(r'^# ', block):
      return re.split(r'^# ', block.strip())[1]
  return "No title found"
  
def generate_page(from_path, template_path, dest_path):
  print("Generating page from " + from_path + " to " + dest_path + " using "+ template_path)

  markdown_file = open(from_path, 'r')
  markdown = markdown_file.read()
  markdown_file.close()

  template_file = open(template_path, 'r')
  template = template_file.read()
  template_file.close

  content = markdown_to_html_node(markdown).to_html()
  title = extract_title(markdown)
  print(title)
  template = template.replace("{{ Title }}", title)
  template = template.replace("{{ Content }}", content)

  if not os.path.exists(dest_path):
    os.makedirs(dest_path)

  file = open(dest_path + "\index.html", 'w')
  file.write(template)



