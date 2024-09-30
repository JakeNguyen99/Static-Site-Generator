import unittest

from block_markdown import(
  markdown_to_blocks,
  block_to_block_type
)

class TestBlockMardown(unittest.TestCase):
   def test_markdown_to_blocks(self):
     markdown = """# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"""
     blocks = markdown_to_blocks(markdown)
     self.assertListEqual(
        [
           "# This is a heading",
           "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
           """* This is the first list item in a list block\n* This is a list item\n* This is another list item""",
        ],
        blocks,
     )

   def test_heading(self):
     self.assertEqual(block_to_block_type("# This is a heading"), "heading")
   
   def test_code(self):
      self.assertEqual(block_to_block_type("```code```"), "code")

   def test_quote(self):
      self.assertEqual(block_to_block_type("> quote"), "quote")

   def test_unordered_list_1(self):
      self.assertEqual(block_to_block_type("* unorder list 1"), "unordered_list")

   def test_unordered_list_2(self):
      self.assertEqual(block_to_block_type("- unordered list 2"), "unordered_list")

   def test_ordered_list_2(self):
      self.assertEqual(block_to_block_type("1. ordered list"), "ordered_list")

   def test_paragraph(self):
      self.assertEqual(block_to_block_type("This is a paragraph of text. It has some **bold** and *italic* words inside of it."), "paragraph")

if __name__ == "__main__":
    unittest.main()