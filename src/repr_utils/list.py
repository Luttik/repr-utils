from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from functools import partial
from typing import List as TypingList
from typing import Union

from repr_utils._base import ReprBase
from repr_utils._util import indent_each_line


@dataclass
class List(ReprBase):
    values: Union[TypingList, Mapping]
    numbered: bool = False

    def __repr__(self) -> str:
        # todo prettify
        return str(self.values)

    def get_value_repr(self, item) -> ReprBase:
        if isinstance(item, ReprBase):
            return item

        return List(item, self.numbered)

    def _repr_html_(self) -> str:
        if isinstance(self.values, Mapping):
            values_string = "\n".join(
                [
                    f"<li>{key}: {value}</li>"
                    if not self.instance_of_any(value, [Mapping, Sequence, ReprBase])
                    else f"<li>{key}</li> {self.get_value_repr(value)._repr_html_()}"
                    for key, value in self.values.items()
                ]
            )
        else:
            values_string = "\n".join(
                [
                    f"<li>{item}</li>"
                    if not self.instance_of_any(item, [Mapping, TypingList, ReprBase])
                    else self.get_value_repr(item)._repr_html_()
                    for item in self.values
                ]
            )

        return "<{type}>\n{values}\n</{type}>".format(
            type="ol" if self.numbered else "ul", values=values_string
        )

    def __handle_nested_markdown(self, value):
        return indent_each_line(self.get_value_repr(value)._repr_markdown_())

    def _repr_markdown_(self) -> str:

        if isinstance(self.values, Mapping):
            return "\n".join(
                [
                    f" - {key}: {value}"
                    if not self.instance_of_any(value, [Mapping, Sequence, ReprBase])
                    else f" - {key}\n{self.__handle_nested_markdown(value)}"
                    for key, value in self.values.items()
                ]
            )
        return "\n".join(
            [
                f" - {item}"
                if not self.instance_of_any(item, [Mapping, TypingList, ReprBase])
                else self.__handle_nested_markdown(item)
                for item in self.values
            ]
        )

    def _repr_latex_(self) -> str:
        if isinstance(self.values, Mapping):
            values_string = "\n".join(
                [
                    f"\\item {key}: {value}"
                    if not self.instance_of_any(value, [Mapping, Sequence, ReprBase])
                    else f"\\item {key}\n{self.get_value_repr(value)._repr_latex_()}"
                    for key, value in self.values.items()
                ]
            )
        else:
            values_string = "\n".join(
                [
                    f"\\item {item}"
                    if not self.instance_of_any(item, [Mapping, TypingList, ReprBase])
                    else self.get_value_repr(item)._repr_latex_()
                    for item in self.values
                ]
            )

        return "\\begin{{{type}}}\n{values}\n\\end{{{type}}}".format(
            type="itemize" if self.numbered else "enumerate", values=values_string
        )

    @classmethod
    def instance_of_any(cls, obj, types: TypingList[type], false_on_string=True):
        if isinstance(obj, str) and false_on_string:
            return False
        type_matcher = partial(isinstance, obj)
        return any(map(type_matcher, types))
