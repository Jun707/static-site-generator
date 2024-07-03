import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_parentNode_to_html_leafNode_case(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')
    
    def test_parentNode_to_html_leafNode_with_props(self):
        props = {"href": "https://www.google.com"}
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                LeafNode("a", "Google.com", props)
            ],
        )
        self.assertEqual(node.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<a href="https://www.google.com">Google.com</a></p>')
        
    
    def test_parentNode_to_html_parentNode_nesting(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ]
                ),
                LeafNode("div", "end of text")
            ],
        )
        self.assertEqual(node.to_html(), '<div><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><div>end of text</div></div>')


if __name__ == "__main__":
    unittest.main()

