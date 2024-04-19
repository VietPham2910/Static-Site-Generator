import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_text_to_html(self):
        node = HTMLNode("p", "paragraph",props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')


if __name__ == "__main__":
    unittest.main()
