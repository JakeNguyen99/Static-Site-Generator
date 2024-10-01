import unittest

from htmlnode import ParentNode, LeafNode

from block_markdown import(
  markdown_to_blocks,
  block_to_block_type,
  markdown_to_html_node
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
     self.assertEqual(block_to_block_type("#### This is a heading"), "heading")
   
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

   def test_markdown_to_html_node(self):
      markdown = """
# Heading 1

## Heading 2

### Heading 3

#### Heading 4

##### Heading 5

###### Heading 6

```
print("Hello world")
```

> We are the hollow men
> We are the stuffed men
> Leaning together
> Headpiece filled with straw. Alas!

* bullet
* points

* more
- bullet
- points

1. a
2. list
3. in
4. order

a paragraph of normal text
        """
      html_node = ParentNode(
            "div",
            [
                ParentNode("h1", [LeafNode(None, "Heading 1")]),
                ParentNode("h2", [LeafNode(None, "Heading 2")]),
                ParentNode("h3", [LeafNode(None, "Heading 3")]),
                ParentNode("h4", [LeafNode(None, "Heading 4")]),
                ParentNode("h5", [LeafNode(None, "Heading 5")]),
                ParentNode("h6", [LeafNode(None, "Heading 6")]),
                ParentNode(
                    "pre",
                    [ParentNode("code", [LeafNode(None, 'print("Hello world")')])],
                ),
                ParentNode(
                    "blockquote",
                    [
                        LeafNode(
                            None,
                            "We are the hollow men\nWe are the stuffed men\nLeaning together\nHeadpiece filled with straw. Alas!",
                        )
                    ],
                ),
                ParentNode(
                    "ul",
                    [
                        ParentNode("li", [LeafNode(None, "bullet")]),
                        ParentNode("li", [LeafNode(None, "points")]),
                    ],
                ),
                ParentNode(
                    "ul",
                    [
                        ParentNode("li", [LeafNode(None, "more")]),
                        ParentNode("li", [LeafNode(None, "bullet")]),
                        ParentNode("li", [LeafNode(None, "points")]),
                    ],
                ),
                ParentNode(
                    "ol",
                    [
                        ParentNode("li", [LeafNode(None, "a")]),
                        ParentNode("li", [LeafNode(None, "list")]),
                        ParentNode("li", [LeafNode(None, "in")]),
                        ParentNode("li", [LeafNode(None, "order")]),
                    ],
                ),
                ParentNode("p", [LeafNode(None, "a paragraph of normal text")]),
            ],
        )
      self.assertEqual(markdown_to_html_node(markdown).to_html(), html_node.to_html())

if __name__ == "__main__":
    unittest.main()