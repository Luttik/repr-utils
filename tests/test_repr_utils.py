from unittest import TestCase

from repr_utils import Header, List, Table


class HeaderTester(TestCase):
    def test_header(self):
        name = "example"
        header = Header(name, 2)
        self.assertEqual(str(header), name)
        self.assertEqual(f"<h2>{name}</h2>", header._repr_html_())
        self.assertEqual(
            f"## {name}", header._repr_markdown_(),
        )
        self.assertEqual(f"\\subsection{{{name}}}", header._repr_latex_())


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


class ListTester(TestCase):
    def test_list(self):
        _list = List(
            {
                "foo": "bar",
                "nested list": [
                    "Item 1",
                    "Item 2",
                    "two items coming up",
                    [1, 2],
                    dict(a=1, b=2),
                ],
                "nested dictionary": {"More nesting": [1, 2, 3]},
            }
        )
        _list._repr_html_()
        self.assertIsNotNone(str(_list))
        self.assertIsNotNone(_list._repr_html_())
        self.assertIsNotNone(_list._repr_markdown_())
        self.assertIsNotNone(_list._repr_latex_())

    def test_list_enumeration(self):
        _list = List(
            {
                "foo": "bar",
                "nested list": [
                    "Item 1",
                    "Item 2",
                    "two items coming up",
                    [1, 2],
                    dict(a=1, b=2),
                ],
                "nested dictionary": {"More nesting": [1, 2, 3]},
            },
            numbered=True,
        )
        self.assertIsNotNone(str(_list))
        self.assertIsNotNone(_list._repr_html_())
        self.assertIsNotNone(_list._repr_markdown_())
        self.assertIsNotNone(_list._repr_latex_())

    def test_list_mixed(self):
        _list = List(
            {
                "foo": "bar",
                "nested list": List([
                    "Item 1",
                    "Item 2",
                    "two items coming up",
                    [1, 2],
                    dict(a=1, b=2),
                ]),
                "nested dictionary": {"More nesting": [1, 2, 3]},
            },
            numbered=True,
        )
        self.assertIsNotNone(str(_list))
        self.assertIsNotNone(_list._repr_html_())
        self.assertIsNotNone(_list._repr_markdown_())
        self.assertIsNotNone(_list._repr_latex_())
