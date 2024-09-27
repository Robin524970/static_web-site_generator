from block_markdown import *
from htmlnode import *
from textnode import *
from funcs import *

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)

        match block_type:
            case "heading":
                nodes.append(header_type_value(block))
            case "code":
                code = block.strip("`\n")
                text_nodes = text_to_children(code)
                pre_tag = ParentNode("pre", [ParentNode("code", text_nodes)])
                nodes.append(pre_tag)
            case "quote":
                quote = strip_md_prefix(block, "> ")
                text_nodes = text_to_children(quote)
                nodes.append(ParentNode("blockquote", text_nodes))
            case "ordered_list":
                items_list = create_ordered_list_nodes(block)
                nodes.append(ParentNode("ol", items_list))
            case "unordered_list":
                items_list = create_unordered_list_nodes(block)
                nodes.append(ParentNode("ul", items_list))
            case "paragraph":
                text_nodes = text_to_children(block)
                nodes.append(ParentNode("p", text_nodes))
            case _:
                raise Exception("Invalid block type")
    return ParentNode("div", nodes)

def header_type_value(markdown):
    header = tuple()
    if markdown.startswith("# "):
        header = "h1", markdown.lstrip("# ")
    if markdown.startswith("## "):
        header = "h2", markdown.lstrip("# ")
    if markdown.startswith("### "):
        header = "h3", markdown.lstrip("# ")
    if markdown.startswith("#### "):
        header = "h4", markdown.lstrip("# ")
    if markdown.startswith("##### "):
        header = "h5", markdown.lstrip("# ")
    if markdown.startswith("###### "):
        header = "h6", markdown.lstrip("# ")
    text_nodes = text_to_children(header[1])
    return ParentNode(header[0], text_nodes)

def strip_md_prefix(markdown, prefix):
    lines = markdown.split("\n")
    text = []
    for line in lines:
        text.append(line.lstrip(prefix))
    return "\n".join(text)

def create_ordered_list_nodes(markdown):
    lines = markdown.split("\n")
    list_items = []
    for line in lines:
        line = line.split(". ", 1)[1]
        text_nodes = text_to_children(line)
        list_item = ParentNode("li", text_nodes)
        list_items.append(list_item)
    return list_items

def create_unordered_list_nodes(markdown):
    cleaned = ""
    if markdown.startswith("*"):
        cleaned = strip_md_prefix(markdown, "* ")
    if markdown.startswith("-"):
        cleaned = strip_md_prefix(markdown, "- ")

    lines = cleaned.split("\n")
    list_items = []
    for line in lines:
        text_nodes = text_to_children(line)
        list_item = ParentNode("li", text_nodes)
        list_items.append(list_item)
    return list_items

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        html_nodes.append(html_node)
    return html_nodes
