from block_markdown import markdown_to_blocks, block_to_block_type, block_type_code, block_type_heading, block_type_ordered_list, block_type_paragraph, block_type_quote, block_type_unordered_list
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
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

if __name__ == "__main__":
    unittest.main()