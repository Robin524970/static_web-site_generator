from md_to_html import *
import os
import pathlib

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as markdown_file:
        markdown = markdown_file.read()

    with open(template_path) as template_file:
        html_template = template_file.read()

    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    html_template = html_template.replace("{{ Title }}", title)
    html_template = html_template.replace("{{ Content }}", html)
    
    if not os.path.exists(os.path.dirname(dest_path)):
        os.mkdir(os.path.dirname(dest_path))
    
    with open(dest_path, "x") as f:
        f.write(html_template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    dir_list = os.listdir(dir_path_content)
    for item in dir_list:
        path_to_current_item = os.path.join(dir_path_content, item)
        path_to_dest_item = os.path.join(dest_dir_path,item)
        if os.path.isfile(path_to_current_item):
            
            generate_page(path_to_current_item, template_path, f"{path_to_dest_item[:-3]}.html")
        else:
            generate_pages_recursive(path_to_current_item, template_path, path_to_dest_item)
