import re
from textnode import TextNode, text_type_image, text_type_text, text_type_link, text_type_bold, text_type_code, text_type_italic

def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern,text) 
    return matches

def extract_markdown_link(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text) 
    return matches

def split_nodes_delimiter(old_nodes, delimiter, text_node):
    res = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            res.append(node)
            continue
        sub_string = []
        delimiter_section = node.text.split(delimiter)
        if len(delimiter_section) == 0:
            raise Exception("Missing closing delimiter")
        for i in range(len(delimiter_section)):
            if delimiter_section[i] == "":
                continue
            if i % 2 == 0:
                sub_string.append(TextNode(delimiter_section[i], text_type_text))
            else:
                sub_string.append(TextNode(delimiter_section[i], text_node))
        res.extend(sub_string)

    return res

def split_nodes_image(old_nodes):
    res = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            res.append(node)
            continue
            
        text = node.text
        matches = extract_markdown_images(text)
        if not len(matches):
            res.append(node)
            continue
        
        for i in matches:
            sub_string = text.split(f"![{i[0]}]({i[1]})", 1)
            if len(sub_string) != 2:
                raise ValueError("Invalid markdown format, image tag is not closed")
            if sub_string[0]:
                res.append(TextNode(sub_string[0], text_type_text))
            res.append(TextNode(i[0], text_type_image, i[1]))
            text = sub_string[1]               
        if text:
            res.append(TextNode(text, text_type_text))
    return res

def split_nodes_link(old_nodes):
    res = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            res.append(node)
            continue
        text = node.text
        matches = extract_markdown_link(text)
        if not len(matches):
            res.append(node)
            continue
        
        for i in matches:
            sub_string = text.split(f"[{i[0]}]({i[1]})", 1)
            if len(sub_string) != 2:
                raise ValueError("Invalid markdown format, link tag is not closed")
            if sub_string[0]:
                res.append(TextNode(sub_string[0], text_type_text))
            res.append(TextNode(i[0], text_type_link, i[1]))
            text = sub_string[1]               
        if text:
            res.append(TextNode(text, text_type_text))
    return res

def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes