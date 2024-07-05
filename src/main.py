from textnode import TextNode 
import os, shutil

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

def main():
    # node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    # print(node)
    destination = "./public"
    path = "./static"
    content_duplicate(path, destination)
                
main()