from repr_utils import Header
from test.fixtures import ReprLocker


def test_header(repr_locker: ReprLocker):
    name = "example"
    header = Header(name, 2)
    repr_locker.lock(header)
