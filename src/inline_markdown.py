import re
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)


def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text
        images = extract_markdown_images(original_text)

        if not images:
            new_nodes.append(old_node)
            continue

        remaining_text = original_text

        for image_alt, image_url in images:
            image_markdown = f"![{image_alt}]({image_url})"

            sections = remaining_text.split(image_markdown, 1)

            before = sections[0]

            if before != "":
                new_nodes.append(
                    TextNode(before, TextType.TEXT)
                )

            new_nodes.append(
                TextNode(
                    image_alt,
                    TextType.IMAGE,
                    image_url,
                )
            )

            remaining_text = sections[1]

        if remaining_text != "":
            new_nodes.append(
                TextNode(remaining_text, TextType.TEXT)
            )

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text
        links = extract_markdown_links(original_text)

        if not links:
            new_nodes.append(old_node)
            continue

        remaining_text = original_text

        for link_text, link_url in links:
            link_markdown = f"[{link_text}]({link_url})"

            sections = remaining_text.split(link_markdown, 1)

            before = sections[0]

            if before != "":
                new_nodes.append(
                    TextNode(before, TextType.TEXT)
                )

            new_nodes.append(
                TextNode(
                    link_text,
                    TextType.LINK,
                    link_url,
                )
            )

            remaining_text = sections[1]

        if remaining_text != "":
            new_nodes.append(
                TextNode(remaining_text, TextType.TEXT)
            )

    return new_nodes