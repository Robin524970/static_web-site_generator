import re
block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    
    result = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        result.append(block)
    return result
    
def block_to_block_type(block):
    lines = block.split("\n")

    if (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
    ):
        return block_type_heading
    
    if block.startswith("```") and block.endswith("```"):
        return block_type_code

    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
               return block_type_paragraph
        return block_type_quote

    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
               return block_type_paragraph
        return block_type_unordered_list

    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
               return block_type_paragraph
        return block_type_unordered_list
    
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
               return block_type_paragraph
            i += 1
        return block_type_ordered_list
    return block_type_paragraph

def extract_title(markdown):

    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block_to_block_type(block) == block_type_heading:
            if block.startswith("# "):
                return block.strip("# ")
    raise Exception("No h1 found")