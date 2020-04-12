from dataclasses import dataclass
from typing import Any, List

from tabulate import tabulate

from repr_utils._base import ReprBase
from repr_utils._jinja import get_template


@dataclass
class Table(ReprBase):
    columns: List[str]
    values: List[List[str]]
    has_index: bool = False

    def __repr__(self) -> str:
        return self.__tabulate()

    def __tabulate(self, fmt: str = "github", values: List[List[Any]] = None) -> str:
        values = values or self.values
        return tabulate(values, headers=self.columns, tablefmt=fmt,)

    def _repr_markdown_(self) -> str:
        values = [[f"**{row[0]}**"] + row[1:] for row in self.values]
        return self.__tabulate(values=values)

    def _repr_latex_(self) -> str:
        return self.__tabulate(fmt="latex")

    def _repr_html_(self) -> str:
        template = get_template("table_html.jinja")
        return template.render(table=self)
