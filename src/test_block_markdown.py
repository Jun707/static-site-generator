from block_markdown import markdown_to_blocks, block_to_block_type, markdown_to_html_node, block_type_code, block_type_heading, block_type_ordered_list, block_type_paragraph, block_type_quote, block_type_unordered_list
import unittest

class test_block_markdown(unittest.TestCase):

    def test_markdown_to_blocks(self):
        test_text = """This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        res = markdown_to_blocks(test_text)
        self.assertEqual(res, 
            [
             "This is **bolded** paragraph",
             "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line", 
             "* This is a list\n* with items"
            ]
        )

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = """```This is a code block```"""
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_paragraph_block_to_html_node(self):
        md = """This is **bolded** paragraph"""
        html_content = "<div><p>This is <b>bolded</b> paragraph</p></div>"
        paragraph_block = markdown_to_html_node(md)
        res = paragraph_block.to_html()
        self.assertEqual(res, html_content)
    
    def test_code_block_to_html_node(self):
        md = """```This is a code block```"""
        html_content = "<div><pre><code>This is a code block</code></pre></div>"
        code_block = markdown_to_html_node(md)
        res = code_block.to_html()
        self.assertEqual(res, html_content)
    
    def test_code_block_with_bolded_paragraph_to_html_node(self):
        md = """
```This is a code block```

this is a **bolded** text
"""
        html_content = "<div><pre><code>This is a code block</code></pre><p>this is a <b>bolded</b> text</p></div>"
        code_block = markdown_to_html_node(md)
        res = code_block.to_html()
        self.assertEqual(res, html_content)
    
    def test_heading_block_to_html_node(self):
        md = """### Heading"""
        html_content = "<div><h3>Heading</h3></div>"
        heading_block = markdown_to_html_node(md)
        res = heading_block.to_html()
        self.assertEqual(res, html_content)
    
    def test_ordered_list_block_to_html_code(self):
        md = """
1. item 1
2. item 2
3. item 3
"""
        html_content = "<div><ol><li>item 1</li><li>item 2</li><li>item 3</li></ol></div>"
        ordered_list_block = markdown_to_html_node(md)
        res = ordered_list_block.to_html()
        self.assertEqual(res, html_content)
    
    def test_heading_block_with_ordered_list_to_html_node(self):
        md = """
# Ordered List

1. test 1
2. test 2
3. test 3
"""
        html_content = "<div><h1>Ordered List</h1><ol><li>test 1</li><li>test 2</li><li>test 3</li></ol></div>"
        block = markdown_to_html_node(md)
        res = block.to_html()
        self.assertEqual(res, html_content)

    def test_unordered_list_block_to_html_node(self):
        md = """
* order 1
* order 2
* order 3
"""
        html_content = "<div><ul><li>order 1</li><li>order 2</li><li>order 3</li></ul></div>"
        unordered_list_block = markdown_to_html_node(md)
        res = unordered_list_block.to_html()
        self.assertEqual(res, html_content)

    def test_quote_block_to_html_node(self):
        md = """
> quote 1
> quote 2
> quote 3
"""

    html_content = "<div><blockquote>quote 1</blockquote><blockquote>quote 2</blockquote><blockquote>quote 3</blockquote></div>"

if __name__ == "__main__":
    unittest.main()