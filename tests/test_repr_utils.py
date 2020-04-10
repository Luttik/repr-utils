from repr_utils import __version__, Header, Table
from unittest import TestCase


def test_version():
    assert __version__ == "0.1.0"


class HeaderTester(TestCase):
    def test_header(self):
        name = "example"
        header = Header(name, 2)
        self.assertEqual(str(header), name)
        self.assertEqual(f"<h2>{name}</h2>", header._repr_html_())
        self.assertEqual(
            f"## {name}", header._repr_markdown_(),
        )
        self.assertEqual(f"\\subheader{{{name}}}", header._repr_latex_())


class TableTester(TestCase):
    # todo define better tests (by locking variables)
    def test_table(self):
        table = Table(
            ["a", "bla", "code & stuff"],
            [["a", 2, 3], ["oh man", 2, 3, 4], ["last row", 4, 5, 6]],
            has_index=True,
        )
        print(table._repr_html_())
        self.assertIsNotNone(str(table))
        self.assertIsNotNone(table._repr_html_())
        self.assertIsNotNone(table._repr_markdown_())
        self.assertIsNotNone(table._repr_latex_())
