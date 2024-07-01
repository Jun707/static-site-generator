import unittest
from extract_markdown import extract_markdown_images, extract_markdown_link, split_nodes_image, split_nodes_link, split_nodes_delimiter, text_to_textnodes
from textnode import TextNode, text_type_link, text_type_image, text_type_text, text_type_italic, text_type_bold, text_type_code

class test_extract_markdown(unittest.TestCase):
    def test_extract_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"

        self.assertEqual(extract_markdown_images(text), [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")])

    def test_extract_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"

        self.assertEqual(extract_markdown_link(text), [("link", "https://www.example.com"), ("another", "https://www.example.com/another")])

    def test_split_nodes_delimiter(self):
        test_node = TextNode("This is text with a `code block` word", text_type_text)
        new_node = split_nodes_delimiter([test_node], "`", text_type_code)
        self.assertEqual(new_node, 
            [
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" word", text_type_text),
            ]
        )

    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png) last ![last image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, 
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and another ", text_type_text),
                TextNode(
                    "second image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
                ),
                TextNode(" last ", text_type_text),
                TextNode(
                    "last image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
                ),
            ]
        )

    def test_split_nodes_link(self):
        node = TextNode("This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)", text_type_text)
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes, 
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("link", text_type_link, "https://www.example.com"),
                TextNode(" and ", text_type_text),
                TextNode(
                    "another", text_type_link, "https://www.example.com/another"
                ),
            ]
        )
    def test_text_to_textnodes(self):
        nodes = text_to_textnodes(
            "This is `text` with an *italic*"
        )
        self.assertListEqual(
            [
                TextNode("This is ", text_type_text),
                TextNode("text", text_type_code),
                TextNode(" with an ", text_type_text),
                TextNode("italic", text_type_italic),
            ],
            nodes,
        )


