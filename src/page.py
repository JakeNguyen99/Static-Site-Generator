import re
import os
from block_markdown import block_to_block_type, markdown_to_blocks, markdown_to_html_node
from copy_static import copy_static

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
  template = template.replace("{{ Title }}", title)
  template = template.replace("{{ Content }}", content)

  if not os.path.exists(dest_path):
    os.makedirs(dest_path)
  file = open(dest_path + "\index.html", 'w')
  file.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
  for item in os.listdir(dir_path_content):
    content_item = os.path.join(dir_path_content, item)
    if os.path.isfile(content_item):
      generate_page(content_item, template_path, dest_dir_path)
    else:
      generate_pages_recursive(content_item, template_path, os.path.join(dest_dir_path, item))



