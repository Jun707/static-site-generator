from content_copy import content_duplicate, generate_pages_recursive

destination = "./public"
path = "./static"
template = "./template.html"
def main():

    content_duplicate(path, destination)
    generate_pages_recursive(path, template, destination)
                
main()