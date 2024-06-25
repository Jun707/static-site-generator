import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        props = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode("h1", "test", None, props)
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_leafNode_to_html(self):
        node = LeafNode("h1", "hello world")
        self.assertEqual(node.to_html(), "<h1>hello world</h1>")

    def test_leafNode_to_html_no_tag(self):
        node = LeafNode(None, "hello world")
        self.assertEqual(node.to_html(), "hello world")
    
    def test_leafNode_to_html_with_props(self):
        props = {"href": "https://www.google.com"}
        node = LeafNode("a", "Google.com", props)
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Google.com</a>')

if __name__ == "__main__":
    unittest.main()

