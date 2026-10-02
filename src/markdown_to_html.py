from block_markdown import markdown_to_blocks, block_to_block_type, BlockType
from htmlnode import ParentNode
from textnode import text_node_to_html_node, TextNode, TextType
from inline_markdown import text_to_textnodes


def text_to_children(text):
    text_nodes = text_to_textnodes(text)

    children = []

    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))

    return children


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)

    block_nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            text = " ".join(block.split("\n"))
            children = text_to_children(text)

            block_nodes.append(ParentNode("p", children))
        
        elif block_type == BlockType.HEADING:
            first_line = block.split("\n")[0]

            count = 0

            for char in first_line:
                if char == "#":
                    count += 1
                else:
                    break

            text = first_line[count + 1:]

            children = text_to_children(text)

            block_nodes.append(ParentNode(f"h{count}", children))

        elif block_type == BlockType.QUOTE:
            lines = block.split("\n")

            text_lines = []

            for line in lines:
                text_lines.append(line[1:].lstrip())

            text = " ".join(text_lines)

            children = text_to_children(text)

            block_nodes.append(ParentNode("blockquote", children))

        elif block_type == BlockType.UNORDERED_LIST:
            lines = block.split("\n")

            list_items = []

            for line in lines:
                text = line[2:]
                children = text_to_children(text)

                list_items.append(
                    ParentNode("li", children)
                )

            block_nodes.append(ParentNode("ul", list_items))

        elif block_type == BlockType.ORDERED_LIST:
            lines = block.split("\n")

            list_items = []

            for line in lines:
                text = line.split(". ", 1)[1]
                children = text_to_children(text)

                list_items.append(
                    ParentNode("li", children)
                )

            block_nodes.append(ParentNode("ol", list_items))

        elif block_type == BlockType.CODE:
            text = block[4:-3]

            text_node = TextNode(text, TextType.TEXT)
            code_node = text_node_to_html_node(text_node)

            code_parent = ParentNode("code", [code_node])
            pre_parent = ParentNode("pre", [code_parent])

            block_nodes.append(pre_parent)

    return ParentNode("div", block_nodes)