import os, shutil
from block_markdown import markdown_to_html_node

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
    return f"{header_str}"

def generate_page(from_path, template_path, des_path):
    print(f"Generate page from {from_path} to {des_path} using {template_path}")
    f = open(from_path, "r")
    from_path_content= f.read()
    f.close()

    header = extract_title(from_path_content)
    html_node = markdown_to_html_node(from_path_content)
    body_content = html_node.to_html()

    t = open(template_path, "r")
    template_path_content = t.read()
    t.close()

    template_path_content = template_path_content.replace("{{ Title }}", header)
    template_path_content = template_path_content.replace("{{ Content }}", body_content)

    dir_list = des_path.split("/")
    dir = "/".join(dir_list[:-1])
    if not os.path.exists(dir):
        os.makedirs(dir)
    with open(des_path, "w") as f:
        f.write(template_path_content)

def generate_pages_recursive(dir_path_content, template_path, des_path):
    dir_list = os.listdir(dir_path_content)
    for dir in dir_list:
        isFile = os.path.isfile((os.path.join(dir_path_content,dir)))
        if not isFile:
            from_dir = os.path.join(dir_path_content, dir)
            des_dir = os.path.join(des_path, dir)
            if not des_dir:
                os.makedirs(des_dir)
            generate_pages_recursive(from_dir, template_path, des_dir)
        else:
            from_file = os.path.join(dir_path_content, dir)
            if from_file.endswith(".md"):
                file_html_suffix = dir[:-2] + "html"
                des_file = os.path.join(des_path, file_html_suffix)
                generate_page(from_file, template_path, des_file)