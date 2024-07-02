block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown: str):
    sub_string = markdown.split("\n\n")
    res =[]
    for s in sub_string:
        temp = s.strip()
        if temp:
            res.append(temp)
    return res

def block_to_block_type(markdown: str):
    lines = markdown.split("\n")
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