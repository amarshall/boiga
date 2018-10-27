import typing as T
from typing_extensions import Protocol
from boiga.monad import Monad
from boiga.util import _Container

_T = T.TypeVar('_T')
_U = T.TypeVar('_U')
_V = T.TypeVar('_V')
_L = T.TypeVar('_L')
_M = T.TypeVar('_M', bound='Monad')


class Either(
        Monad['Either', _T],
        Protocol,
        T.Generic[_L, _T],
        ):
    def __init__(self, *_: T.Any, **__: T.Any) -> None: ...

    def bind(
            self, f: T.Callable[[_T], 'Either[_L, _U]']
            ) -> 'Either[_L, _U]': ...

    def __rshift__(
            self, f: T.Callable[[_T], 'Either[_L, _U]']
            ) -> 'Either[_L, _U]': ...

    def fmap(self, f: T.Callable[[_T], _U]) -> 'Either[_L, _U]': ...

    def __mul__(self, f: T.Callable[[_T], _U]) -> 'Either[_L, _U]': ...


class Left(Either[_L, _T], _Container[_L]):
    _value: _L

    def __init__(self, value: _L) -> None:
        self._value = value

    def bind(self, f: T.Callable[[_T], Either[_L, _U]]) -> Either[_L, _U]:
        return Left(self._value)
    __rshift__ = bind

    def fmap(self, f: T.Callable[[_T], _U]) -> Either[_L, _U]:
        return Left(self._value)
    __mul__ = fmap

    def __repr__(self) -> str:
        return 'Left({})'.format(self._value)


class Right(Either[_L, _T], _Container[_T]):
    _value: _T

    def __init__(self, value: _T) -> None:
        self._value = value

    def bind(self, f: T.Callable[[_T], Either[_L, _U]]) -> Either[_L, _U]:
        return f(self._value)
    __rshift__ = bind

    def fmap(self, f: T.Callable[[_T], _U]) -> Either[_L, _U]:
        return Right(f(self._value))
    __mul__ = fmap

    def __repr__(self) -> str:
        return 'Right({})'.format(self._value)
