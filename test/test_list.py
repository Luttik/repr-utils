from repr_utils import List
from .fixtures import Locker


def test_list(locker: Locker):
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
    locker.lock(str(_list), 'as_string')
    locker.lock(_list._repr_html_(), 'as_html', 'html')
    locker.lock(_list._repr_markdown_(), 'as_markdown', 'md')
    locker.lock(_list._repr_latex_(), 'as_latex', 'latex')


def test_list_enumeration():
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
    assert str(_list) is not None
    assert _list._repr_html_() is not None
    assert _list._repr_markdown_() is not None
    assert _list._repr_latex_() is not None


def test_list_mixed():
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
    assert str(_list) is not None
    assert _list._repr_html_() is not None
    assert _list._repr_markdown_() is not None
    assert _list._repr_latex_() is not None
