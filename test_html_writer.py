#!/usr/bin/env python3

import unittest
from html_writer import read_html, read_csv, csv_to_html, combine_template_with_data

class TestHTMLWriter(unittest.TestCase):

    def setUp(self):
        self.csvdata = [["First", "Last", "E-Mail"]]
        self.htmldata = "<tr><td>A</td><td>B</td><td>C</td></tr>"
        self.template = read_html()

    def test_read_csv_type(self):
        result = read_csv("test.csv")
        self.assertIsInstance(result, list)

    def test_read_csv_data(self):
        result = read_csv("test.csv")
        first = result[0][0]
        self.assertEqual(first, "Andreas")

    def test_csv_to_html_type(self):
        htmlstring = csv_to_html(self.csvdata)
        self.assertIsInstance(htmlstring, str)

    def test_csv_to_html_is_table_row(self):
        htmlstring = csv_to_html(self.csvdata)
        self.assertIn("<tr>", htmlstring)
        self.assertIn("</tr>", htmlstring)

    def test_csv_to_html_has_table_data(self):
        htmlstring = csv_to_html(self.csvdata)
        self.assertIn("<td>", htmlstring)
        self.assertIn("</td>", htmlstring)

    def test_csv_to_html_replaced_brackets(self):
        htmlstring = csv_to_html(self.csvdata)
        self.assertNotIn("{}", htmlstring)

    def test_combine_template_with_data_type(self):
        content = combine_template_with_data(self.template, "")
        self.assertIsInstance(content, str)

    def test_combine_template_with_data_replace(self):
        content = combine_template_with_data(self.template, self.htmldata)
        self.assertTrue(content.startswith("<!DOCTYPE html>"))
        self.assertTrue(content.endswith("</html>\n"))
        self.assertNotIn("{}", content)

if __name__ == "__main__":
    unittest.main()
