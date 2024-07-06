from textnode import TextNode 
from content_copy import content_duplicate, extract_title, generate_page

def main():
    # node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    # print(node)
    # destination = "./public"
    # path = "./static"
    # content_duplicate(path, destination)
#     markdown = """
# """
#     res = extract_title(markdown)
#     print(res)
      generate_page("./static/index.md", "./template.html", "./public")
                
main()