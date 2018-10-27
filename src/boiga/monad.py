import typing as T
from typing_extensions import Protocol
from boiga.functor import Functor

_Tco = T.TypeVar('_Tco', covariant=True)
_M = T.TypeVar('_M', bound='Monad')


class Monad(Functor[_Tco], Protocol, T.Generic[_M, _Tco]):
    def bind(self, f: T.Callable[[_Tco], _M]) -> _M: ...

    def __rshift__(self, f: T.Callable[[_Tco], _M]) -> _M: ...
