import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "a",
            "Google",
            props={"href": "https://www.google.com"}
        )

        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com"',
        )

    def test_multiple_props(self):
        node = HTMLNode(
            "a",
            "Google",
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            }
        )

        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"',
        )

    def test_no_props(self):
        node = HTMLNode("p", "Hello")

        self.assertEqual(node.props_to_html(), "")


if __name__ == "__main__":
    unittest.main()