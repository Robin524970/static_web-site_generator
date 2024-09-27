import unittest
from block_markdown import *

class Test_markdown_to_blocks(unittest.TestCase):
    

    def test_markdown(self):
        markdown = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""
        blocks = markdown_to_blocks(markdown)
        self.assertListEqual(
            blocks, [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
            ]
        )

    def test_block_type(self):
        markdown = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item

- This is the first list item in a list block
- This is a list item
- This is another list item

```This is a code block```

1. list 1
2. list 2
3. list 3
"""
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            block_to_block_type(blocks[0]),
            block_type_heading
        )

        self.assertEqual(
            block_to_block_type(blocks[1]),
            block_type_paragraph
        )

        self.assertEqual(
            block_to_block_type(blocks[2]),
            block_type_unordered_list
        )

        self.assertEqual(
            block_to_block_type(blocks[3]),
            block_type_unordered_list
        )

        self.assertEqual(
            block_to_block_type(blocks[4]),
            block_type_code
        )

        self.assertEqual(
            block_to_block_type(blocks[5]),
            block_type_ordered_list
        )
    def test_multiline_codeblock(self):
        markdown = """
```
This is a code block
this is another line of code
and another
```
"""
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            block_to_block_type(blocks[0]),
            block_type_code
        )

    def test_extract_title(self):
        markdown = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item

- This is the first list item in a list block
- This is a list item
- This is another list item

```This is a code block```

1. list 1
2. list 2
3. list 3
"""
        self.assertEqual(extract_title(markdown), "This is a heading")
        
if __name__ == "__main__":
    unittest.main()
