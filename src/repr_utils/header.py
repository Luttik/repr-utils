from dataclasses import dataclass

from repr_utils._base import ReprBase


@dataclass
class Header(ReprBase):
    text: str
    header_number: int = 1

    def _repr_html_(self) -> str:
        return f"<h{self.header_number}>{self.text}</h{self.header_number}>"

    def _repr_markdown_(self) -> str:
        return f'{"#" * self.header_number} {self.text}'

    def _repr_latex_(self) -> str:
        return f'\\{"sub" * (self.header_number - 1)}header{{{self.text}}}'

    def __repr__(self) -> str:
        return self.text
