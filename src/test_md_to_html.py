import unittest
from md_to_html import *

class Test_md_to_html(unittest.TestCase):
    def setUp(self):
        self.h1 = "# header text"
        self.h2 = "## header text"
        self.h3 = "### header text"
        self.h4 = "#### header text"
        self.h5 = "##### header text"
        self.h6 = "###### header text"

        self.code_block ="""
```This is a multiline code block
Hear is another line
and another```"""

        self.quoteblock = """
> This is a quote block
> another line
> and another
"""
        self.ordered_list = """
1. item 1
2. item 2
3. item 3
"""

        self.unordered_list = """
* item 1
* item 2
* item 3
"""

        self.unordered_list2 = """
- item 1
- item 2
- item 3
"""
        self.markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item

This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)
"""

        self.paragraph = """This is a pragraph
This is the next line
and another.
"""
        self.test_case = [HTMLNode("li", None, [LeafNode(None, "item 1", None)], None), HTMLNode("li", None, [LeafNode(None, "item 2", None)], None), HTMLNode("li", None, [LeafNode(None, "item 3", None)], None)]


    def test_markdown_header(self):
        html_tree = markdown_to_html_node(self.h1)
        self.assertEqual(html_tree.to_html(), "<div><h1>header text</h1></div>")

    def test_code(self):
        html_tree = markdown_to_html_node(self.code_block)
        self.assertEqual(html_tree.to_html(), "<div><pre><code>This is a multiline code block\nHear is another line\nand another</code></pre></div>")

    def test_quote(self):
        html_tree = markdown_to_html_node(self.quoteblock)
        self.assertEqual(html_tree.to_html(), "<div><blockquote>This is a quote block\nanother line\nand another</blockquote></div>")

    def test_ordered_list(self):
        html_tree = markdown_to_html_node(self.ordered_list)
        self.assertEqual(html_tree.to_html(), "<div><ol><li>item 1</li><li>item 2</li><li>item 3</li></ol></div>")

    def test_unordered_list(self):
        html_tree = markdown_to_html_node(self.unordered_list)
        self.assertEqual(html_tree.to_html(), "<div><ul><li>item 1</li><li>item 2</li><li>item 3</li></ul></div>")

    def test_paragraph(self):
        html_tree = markdown_to_html_node(self.paragraph)
        self.assertEqual(html_tree.to_html(), "<div><p>This is a pragraph\nThis is the next line\nand another.</p></div>")

    def test_markdown(self):
        expected = "<div>\
<h1>This is a heading</h1>\
<p>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p>\
<ul>\
<li>This is the first list item in a list block</li>\
<li>This is a list item</li>\
<li>This is another list item</li>\
</ul>\
<p>This is <b>text</b> with an <i>italic</i> word and a \
<code>code block</code>\
 and an <img src=\"https://i.imgur.com/fJRm4Vk.jpeg\" alt=\"obi wan image\">\
</img> and a <a href=\"https://boot.dev\">link</a></p></div>"


        html_tree = markdown_to_html_node(self.markdown)
        # print(html_tree.to_html())
        self.assertEqual(html_tree.to_html(), expected)
        # print(f"\nHTML TREE: {html_tree}")

if __name__ == "__main__":
    unittest.main()
