import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        props = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode("h1", "test", None, props)
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')


if __name__ == "__main__":
    unittest.main()

