from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from functools import partial
from typing import List as TypingList

from repr_utils._base import ReprBase
from repr_utils._util import indent_each_line


@dataclass
class Link(ReprBase):
    url: str
    text: str

    def __repr__(self) -> str:
        return f"{self.text}: {self.url}"

    def _repr_html_(self) -> str:
        return f'<a href="{self.url}">\n{self.text}\n</a>'

    def _repr_markdown_(self) -> str:
        return f"[{self.text}]({self.url})"

    def _repr_latex_(self) -> str:
        return f"\\href{{{self.url}}}{{{self.text}}}"
