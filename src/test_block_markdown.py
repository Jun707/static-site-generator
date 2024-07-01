from block_markdown import markdown_to_blocks
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

        