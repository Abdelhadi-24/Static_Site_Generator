import unittest

from block_markdown import markdown_to_blocks, BlockType, block_to_block_type


class TestMarkdownToBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""

        blocks = markdown_to_blocks(md)

        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_multiple_blocks(self):
        md = """# Heading

First paragraph

Second paragraph

- Item 1
- Item 2
"""

        blocks = markdown_to_blocks(md)

        self.assertEqual(
            blocks,
            [
                "# Heading",
                "First paragraph",
                "Second paragraph",
                "- Item 1\n- Item 2",
            ],
        )

    def test_empty_blocks_are_removed(self):
        md = """
First paragraph


Second paragraph



Third paragraph
"""

        blocks = markdown_to_blocks(md)

        self.assertEqual(
            blocks,
            [
                "First paragraph",
                "Second paragraph",
                "Third paragraph",
            ],
        )

    def test_whitespace_is_stripped(self):
        md = """
   First paragraph   

   Second paragraph   
"""

        blocks = markdown_to_blocks(md)

        self.assertEqual(
            blocks,
            [
                "First paragraph",
                "Second paragraph",
            ],
        )

    def test_paragraph(self):
        block = "This is a normal paragraph."

        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH,
        )

    def test_heading(self):
        self.assertEqual(
            block_to_block_type("# Heading"),
            BlockType.HEADING,
        )

        self.assertEqual(
            block_to_block_type("###### Heading"),
            BlockType.HEADING,
        )

    def test_invalid_heading(self):
        self.assertEqual(
            block_to_block_type("####### Heading"),
            BlockType.PARAGRAPH,
        )

        self.assertEqual(
            block_to_block_type("#Heading"),
            BlockType.PARAGRAPH,
        )

    def test_code(self):
        block = "```\nprint('hello')\n```"

        self.assertEqual(
            block_to_block_type(block),
            BlockType.CODE,
        )

    def test_quote(self):
        block = "> This is a quote\n> This is another line"

        self.assertEqual(
            block_to_block_type(block),
            BlockType.QUOTE,
        )

    def test_invalid_quote(self):
        block = "> This is a quote\nThis is not"

        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH,
        )

    def test_unordered_list(self):
        block = "- First\n- Second\n- Third"

        self.assertEqual(
            block_to_block_type(block),
            BlockType.UNORDERED_LIST,
        )

    def test_invalid_unordered_list(self):
        block = "- First\nSecond\n- Third"

        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH,
        )

    def test_ordered_list(self):
        block = "1. First\n2. Second\n3. Third"

        self.assertEqual(
            block_to_block_type(block),
            BlockType.ORDERED_LIST,
        )

    def test_invalid_ordered_list(self):
        block = "1. First\n3. Second\n4. Third"

        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH,
        )

    def test_ordered_list_must_start_at_one(self):
        block = "2. First\n3. Second"

        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH,
        )