from dataclasses import dataclass
from functools import partial
from typing import Union, List as TypingList
from collections import Mapping, Sequence

from IPython.core.display import display, HTML

from repr_utils._base import ReprBase


@dataclass
class List(ReprBase):
    values: Union[TypingList, Mapping]
    numbered: bool = False

    def __repr__(self) -> str:
        # todo improve (handle nested items)
        if isinstance(self.values, Mapping):
            return str(dict(**self.values))
        return str(list(*self.values))

    def get_value_repr(self, item) -> ReprBase:
        if isinstance(item, ReprBase):
            return item

        return List(item, self.numbered)

    def _repr_html_(self) -> str:
        values_string = None

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

    def _repr_markdown_(self) -> str:
        # Todo implement
        raise NotImplementedError()

    def _repr_latex_(self) -> str:
        # Todo implement
        raise NotImplementedError()

    def instance_of_any(self, obj, types: TypingList[type], false_on_string=True):
        if isinstance(obj, str):
            return False
        type_matcher = partial(isinstance, obj)
        return any(map(type_matcher, types))

    def _ipython_display_(self):
        # Todo remove if _repr_markdown_ and _repr_latex_ are implemented
        return display(HTML(self._repr_html_()))
