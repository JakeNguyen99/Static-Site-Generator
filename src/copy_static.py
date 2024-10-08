import os
import shutil

def copy_static(src, dst):
  if not os.path.exists(dst):
    os.makedirs(dst)
  for item in os.listdir(src):
    src_item = os.path.join(src, item)
    dst_item = os.path.join(dst, item)
    if os.path.isdir(src_item):
      copy_static(src_item, dst_item)
    else:
      shutil.copy2(src_item, dst_item)