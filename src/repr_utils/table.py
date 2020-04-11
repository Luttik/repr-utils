from dataclasses import dataclass
from typing import List

from tabulate import tabulate

from repr_utils._base import ReprBase
from repr_utils._jinja import get_template


@dataclass
class Table(ReprBase):
    columns: List[str]
    values: List[List[str]]
    has_index: bool = False

    def __repr__(self):
        return self.__tabulate()

    def __tabulate(self, fmt="pretty") -> str:
        return tabulate(
            self.values,
            colalign=[(0, "r")] if self.has_index else None,
            headers=self.columns,
            tablefmt=fmt,
        )

    def _repr_markdown_(self):
        return self.__tabulate()

    def _repr_latex_(self):
        return self.__tabulate(fmt="latex")

    def _repr_html_(self) -> str:
        template = get_template("table_html.jinja")
        return template.render(table=self)
