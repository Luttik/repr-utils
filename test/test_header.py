from repr_utils import Header


def test_header():
    name = "example"
    header = Header(name, 2)
    assert str(header) == name
    assert f"<h2>{name}</h2>" == header._repr_html_()
    assert f"## {name}" == header._repr_markdown_()
    assert f"\\subsection{{{name}}}" == header._repr_latex_()
