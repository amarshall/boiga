import typing as T
from typing_extensions import Protocol

_Tco = T.TypeVar('_Tco', covariant=True)
_U = T.TypeVar('_U')


class Functor(Protocol, T.Generic[_Tco]):
    def __init__(self) -> None: ...

    def fmap(self, f: T.Callable[[_Tco], _U]) -> 'Functor[_U]': ...

    def __mul__(self, f: T.Callable[[_Tco], _U]) -> 'Functor[_U]': ...
