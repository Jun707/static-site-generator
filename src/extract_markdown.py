import re
from textnode import TextNode, text_type_image, text_type_text, text_type_link

def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern,text) 
    return matches

def extract_markdown_link(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text) 
    return matches

def split_nodes_image(old_nodes):
    res = []
    for node in old_nodes:
        sub_string = []

        matches = extract_markdown_images(node.text)
        sub_text = node.text
        if not matches:
            sub_string.append(TextNode(node.text, text_type_text))
        else:
            for i in matches:
                sub_text = sub_text.split(f"![{i[0]}]({i[1]})", 1)
                sub_string.append(TextNode(sub_text[0], text_type_text))
                sub_string.append(TextNode(i[0], text_type_image, i[1]))
                if len(sub_text) >= 1:
                    sub_text = sub_text[1]
        res.extend(sub_string)
    return res

def split_nodes_link(old_nodes):
    res = []
    for node in old_nodes:
        sub_string = []

        matches = extract_markdown_link(node.text)
        sub_text = node.text
        if not matches:
            sub_string.append(TextNode(node.text, text_type_text))
        else:
            for i in matches:
                sub_text = sub_text.split(f"[{i[0]}]({i[1]})", 1)
                sub_string.append(TextNode(sub_text[0], text_type_text))
                sub_string.append(TextNode(i[0], text_type_link, i[1]))
                if len(sub_text) >= 1:
                    sub_text = sub_text[1]
        res.extend(sub_string)
    return res