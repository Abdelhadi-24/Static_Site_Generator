import unittest

from inline_markdown import (
    split_nodes_delimiter, extract_markdown_images, extract_markdown_links
)
from textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    # imgs + links

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )

        self.assertListEqual(
            [
                ("image", "https://i.imgur.com/zjjcJKZ.png")
            ],
            matches,
        )

    def test_extract_multiple_images(self):
        matches = extract_markdown_images(
            "![cat](cat.png) and ![dog](dog.png)"
        )

        self.assertListEqual(
            [
                ("cat", "cat.png"),
                ("dog", "dog.png"),
            ],
            matches,
        )

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is [Boot.dev](https://www.boot.dev)"
        )

        self.assertListEqual(
            [
                ("Boot.dev", "https://www.boot.dev")
            ],
            matches,
        )

    def test_extract_multiple_links(self):
        matches = extract_markdown_links(
            "[Boot.dev](https://www.boot.dev) and [YouTube](https://youtube.com)"
        )

        self.assertListEqual(
            [
                ("Boot.dev", "https://www.boot.dev"),
                ("YouTube", "https://youtube.com"),
            ],
            matches,
        )

    def test_link_does_not_match_image(self):
        matches = extract_markdown_links(
            "![image](image.png)"
        )

        self.assertListEqual([], matches)

    def test_no_images(self):
        matches = extract_markdown_images(
            "There are no images here."
        )

        self.assertListEqual([], matches)

    def test_no_links(self):
        matches = extract_markdown_links(
            "There are no links here."
        )

        self.assertListEqual([], matches)



if __name__ == "__main__":
    unittest.main()
