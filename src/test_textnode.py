import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)

        self.assertEqual(node, node2)

    def test_different_text(self):
        node = TextNode("Hello", TextType.TEXT)
        node2 = TextNode("Goodbye", TextType.TEXT)

        self.assertNotEqual(node, node2)

    def test_different_text_type(self):
        node = TextNode("Hello", TextType.TEXT)
        node2 = TextNode("Hello", TextType.BOLD)

        self.assertNotEqual(node, node2)

    def test_different_url(self):
        node = TextNode("Boot.dev", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("Boot.dev", TextType.LINK, "https://example.com")

        self.assertNotEqual(node, node2)

    def test_none_url(self):
        node = TextNode("Hello", TextType.TEXT)
        node2 = TextNode("Hello", TextType.TEXT)

        self.assertEqual(node.url, None)
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()