from repr_utils import List
from .fixtures import ReprLocker


def test_unordered(repr_locker: ReprLocker):
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
    repr_locker.lock(_list)


def test_list_enumeration(repr_locker: ReprLocker):
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
    repr_locker.lock(_list)


def test_list_mixed(repr_locker: ReprLocker):
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
    repr_locker.lock(_list)
