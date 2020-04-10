from abc import abstractmethod, ABC


class ReprBase(ABC):
    @abstractmethod
    def __repr__(self) -> str:
        ...

    @abstractmethod
    def _repr_html_(self) -> str:
        ...

    @abstractmethod
    def _repr_markdown_(self) -> str:
        ...

    @abstractmethod
    def _repr_latex_(self) -> str:
        ...
