from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")

    new_blocks = []

    for block in blocks:
        block = block.strip()

        if block != "":
            new_blocks.append(block)

    return new_blocks


def block_to_block_type(block):
    lines = block.split("\n")

    # Heading
    if lines[0].startswith("#"):
        count = 0

        for char in lines[0]:
            if char == "#":
                count += 1
            else:
                break

        if 1 <= count <= 6 and len(lines[0]) > count and lines[0][count] == " ":
            return BlockType.HEADING

    # Code
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE

    # Quote
    is_quote = True

    for line in lines:
        if not line.startswith(">"):
            is_quote = False
            break

    if is_quote:
        return BlockType.QUOTE

    # Unordered list
    is_unordered_list = True

    for line in lines:
        if not line.startswith("- "):
            is_unordered_list = False
            break

    if is_unordered_list:
        return BlockType.UNORDERED_LIST

    # Ordered list
    is_ordered_list = True
    expected_number = 1

    for line in lines:
        prefix = f"{expected_number}. "

        if not line.startswith(prefix):
            is_ordered_list = False
            break

        expected_number += 1

    if is_ordered_list:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH