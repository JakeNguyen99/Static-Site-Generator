import os
import shutil
from copy_static import copy_static
from page import generate_page, generate_pages_recursive

def main():
  src = os.path.join(os.curdir, "static")
  dst = os.path.join(os.curdir, "public")
  template_path = os.path.join(os.curdir, "template.html")
  content_path = os.path.join(os.curdir, "content")

  if os.path.exists(dst):
    shutil.rmtree(dst)
    os.makedirs(dst)

  copy_static(src, dst)
  generate_pages_recursive(content_path, template_path,dst)


main()