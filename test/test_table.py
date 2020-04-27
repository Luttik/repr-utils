from repr_utils import Table
from test.fixtures import ReprLocker


def test_table(repr_locker: ReprLocker):
    table = Table(
        ["a", "bla", "code & stuff"],
        [["a", 2, 3], ["oh man", 2, 3, 4], ["last row", 4, 5, 6]],
        has_index=True,
    )
    repr_locker.lock(table)
