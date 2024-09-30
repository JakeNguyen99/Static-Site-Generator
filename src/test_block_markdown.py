import unittest

from block_markdown import(
  markdown_to_blocks
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

if __name__ == "__main__":
    unittest.main()