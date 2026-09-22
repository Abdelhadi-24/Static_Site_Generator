import unittest

from htmlnode import HTMLNode, ParentNode, LeafNode


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

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])

        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child</span></div>",
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])

        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_multiple_children(self):
        parent_node = ParentNode(
            "div",
            [
                LeafNode("p", "Hello"),
                LeafNode("p", "World"),
            ],
        )

        self.assertEqual(
            parent_node.to_html(),
            "<div><p>Hello</p><p>World</p></div>",
        )

    def test_text_children(self):
        parent_node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold"),
                LeafNode(None, " normal text"),
                LeafNode("i", " italic"),
            ],
        )

        self.assertEqual(
            parent_node.to_html(),
            "<p><b>Bold</b> normal text<i> italic</i></p>",
        )

    def test_no_children(self):
        parent_node = ParentNode("div", [])

        self.assertEqual(
            parent_node.to_html(),
            "<div></div>",
        )

    def test_no_tag(self):
        parent_node = ParentNode(None, [])

        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_no_children_attribute(self):
        parent_node = ParentNode("div", None)

        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_props(self):
        parent_node = ParentNode(
            "div",
            [LeafNode("p", "Hello")],
            {"class": "container"},
        )

        self.assertEqual(
            parent_node.to_html(),
            '<div class="container"><p>Hello</p></div>',
        )



if __name__ == "__main__":
    unittest.main()