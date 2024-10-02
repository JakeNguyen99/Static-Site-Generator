import unittest

from page import(
  extract_title
)

class TestPage(unittest.TestCase):
  def test_extract_title(self):
    markdown = """# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"""
    title = extract_title(markdown)
    self.assertEqual("This is a heading", title)

  def test_extract_title_missing_heading(self):
    markdown = """\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"""
    title = extract_title(markdown)
    self.assertEqual("No title found", title)

if __name__ == "__main__":
  unittest.main()