from repr_utils import Table


def test_table():
    table = Table(
        ["a", "bla", "code & stuff"],
        [["a", 2, 3], ["oh man", 2, 3, 4], ["last row", 4, 5, 6]],
        has_index=True,
    )
    print(table._repr_html_())
    assert str(table) is not None
    assert table._repr_html_() is not None
    assert table._repr_markdown_() is not None
    assert table._repr_latex_() is not None
