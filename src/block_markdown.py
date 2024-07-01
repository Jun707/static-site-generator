def markdown_to_blocks(markdown):
    sub_string = markdown.split("\n\n")
    res =[]
    for s in sub_string:
        temp = s.strip()
        if temp:
            res.append(temp)
    return res