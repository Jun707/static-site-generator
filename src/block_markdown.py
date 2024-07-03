from htmlnode import ParentNode, LeafNode
from textnode import text_node_to_html_node
from extract_markdown import text_to_textnodes

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown: str):
    sub_string = markdown.split("\n\n")
    res = []
    for s in sub_string:
        temp = s.strip()
        if temp:
            res.append(temp)
    print(res)
    return res

def block_to_block_type(block: str):
    lines = block.split("\n")
    if lines[0].startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return block_type_heading
    if lines[0].startswith("```") and lines[-1].endswith("```"):
        return block_type_code
    if all(line.startswith(">") for line in lines):
        return block_type_quote
    if all(line.startswith(("* ", "- ")) for line in lines):
            return block_type_unordered_list
    for i in range(len(lines)):
        if not lines[i].startswith(f"{i+1}. "):
            return block_type_paragraph
    return block_type_ordered_list

def markdown_to_html_node(markdown: str):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)

def block_to_html_node(block: str):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return paragraph_block_type(block)
    if block_type == block_type_heading:
        return heading_block_type(block)


def text_to_children(text: str):
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)
    return children


def paragraph_block_type(block: str):
    lines = block.split("\n")
    paragraph = (" ").join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_block_type(block: str):
    level = 0
    for char in block:
        if char == "#":
            level +=1
        else:
            break
    text = block[level+1:]
    children = text_to_children(text)
    
    return ParentNode(f"h{level}", children)

def code_block_type(block: str):
    text = block[4: -3]
    children = text_to_children(text)
    code_block = ParentNode("code", children)
    return ParentNode("pre", code_block)


