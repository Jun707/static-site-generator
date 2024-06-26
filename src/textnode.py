from htmlnode import LeafNode
text_node_dict = {
    "text_type_text": "text",
    "text_type_bold": "bold",
    "text_type_italic": "italic",
    "text_type_code": "code",
    "text_type_link": "link",
    "text_type_image": "image"
}
def text_node_to_html_node(text_node):
    if text_node.text_type not in text_node_dict:
        raise Exception(f"Unknow text node type")
    res = ""
    if text_node.text_tpye == 'text':
        res = LeafNode(None, text_node.text)
    elif text_node.text_type == "bold":
        res = LeafNode("b", text_node.text)
    elif text_node.text_type == "italic":
        res = LeafNode("i", text_node.text)
    elif text_node.text_type == "code":
        res = LeafNode("code", text_node.text)
    elif text_node.text_type == "link":
        res = LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == "image":
        res = LeafNode("img", None, {"src": text_node.url, "alt": text_node.text})
        
    return res

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, val: object) -> bool:
        return val.text == self.text and val.text_type == self.text_type and val.url == self.url
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"      