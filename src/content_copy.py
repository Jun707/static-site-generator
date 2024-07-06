import os, shutil
from block_markdown import markdown_to_html_node
from htmlnode import HTMLNode

def content_duplicate(path, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)

    folder = os.listdir(path)

    for file in folder:
        new_path = os.path.join(path, file)
        new_des = os.path.join(destination, file)
        if os.path.isfile(new_path):
            shutil.copy(new_path, new_des)
        else:
            content_duplicate(new_path, new_des)

def extract_title(markdown: str):
    blocks = markdown.split("\n\n")
    header_block = blocks[0].strip()
    header = header_block[:2]
    if not header.startswith("#"):
        raise Exception("All pages need a single h1 header")
    for char in header:
        header_char = 0
        if char == "#":
            header_char +=1
        if header_char > 1:
            raise Exception("All pages need a single h1 header")
    header_str = header_block[2:]
    return f"<h1>{header_str}</h1>"

def generate_page(from_path, template_path, des_path):
    print(f"Generate page from {from_path} to {des_path} using {template_path}")
    f = open(from_path, "r")
    from_path_content= f.read()
    f.close()
    header = extract_title(from_path_content)
    # parse md to html node
    html_node = markdown_to_html_node(from_path_content)
    print(html_node)
    # parse html node to html code
    html_content = html_node.to_html()
    t = open(template_path, "r")
    template_path_content = t.read()
    t.close()
    print(header)
    print(html_content)
    template_path_content = template_path_content.replace("{{ Title }}", header)
    print(template_path_content)
    

