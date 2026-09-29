import unittest

from block_markdown import markdown_to_blocks


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