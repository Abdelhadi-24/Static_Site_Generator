import unittest

from main import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_extract_title_with_whitespace(self):
        self.assertEqual(
            extract_title("#   Tolkien Fan Club   "),
            "Tolkien Fan Club",
        )

    def test_extract_title_with_multiple_headings(self):
        markdown = "# Main Title\n\n## Subtitle"
        self.assertEqual(extract_title(markdown), "Main Title")

    def test_extract_title_missing(self):
        with self.assertRaises(Exception):
            extract_title("## Not an h1 heading")
