from test.fixtures import ReprLocker

from repr_utils import Link


def test_header(repr_locker: ReprLocker):
    link = Link("https://www.google.com/", "google")
    repr_locker.lock(link)
