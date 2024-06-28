import unittest

from textnode import TextNode

# total of 6 unit tests
class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", "bold", "https://www.google.com")
        node2 = TextNode("This is a text node", "bold", "https://www.google.com")
        self.assertEqual(node, node2)

    def test_eq_false_text(self):
        node = TextNode("This is a test node", "bold")
        node2 = TextNode("This is not a test node", "bold")
        self.assertNotEqual(node, node2)

    def test_eq_false_text_type(self):
        node = TextNode("This is a test node", "bold")
        node2 = TextNode("This is a test node", "text")
        self.assertNotEqual(node, node2)
    
    def test_eq_false_url(self):
        node = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node2 = TextNode("This is a text node", "bold", "https://www.google.com")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", "bold", "https://www.google.com")
        self.assertEqual("TextNode(This is a text node, bold, https://www.google.com)", repr(node))

if __name__ == "__main__":
    unittest.main()