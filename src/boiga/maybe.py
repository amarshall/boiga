import typing as T
from typing_extensions import Protocol
from boiga.monad import Monad
from boiga.util import _Container

_T = T.TypeVar('_T')
_U = T.TypeVar('_U')
_M = T.TypeVar('_M', bound='Monad')


class Maybe(Monad['Maybe', _T], Protocol, T.Generic[_T]):
    @staticmethod
    def unit(value: T.Optional[_T]) -> 'Maybe[_T]':
        if value is None:
            return Nothing()
        else:
            return Just(value)

    def bind(self, f: T.Callable[[_T], 'Maybe[_U]']) -> 'Maybe[_U]': ...

    def __rshift__(self, f: T.Callable[[_T], 'Maybe[_U]']) -> 'Maybe[_U]': ...


class Just(Maybe[_T], _Container[T.Optional[_T]]):
    _value: _T

    def __init__(self, value: _T) -> None:
        if value is None:
            raise TypeError('use Nothing() instead of Just(None)')
        self._value = value

    def bind(self, f: T.Callable[[_T], _M]) -> _M:
        return f(self._value)
    __rshift__ = bind

    def fmap(self, f: T.Callable[[_T], _U]) -> Maybe[_U]:
        return Just(f(self._value))
    __mul__ = fmap

    def __repr__(self) -> str:
        return 'Just({})'.format(self._value)


class Nothing(Maybe[_T]):
    _instance: 'T.Optional[Nothing[object]]' = None

    def __new__(
            cls: 'T.Type[Nothing[_T]]',
            *args: T.List[object], **kwargs: T.Dict[str, object]
            ) -> 'Nothing[_T]':
        if not cls._instance:
            cls._instance = Maybe.__new__(cls)
        return cls._instance  # type: ignore

    def __init__(self) -> None:
        pass

    def bind(self, f: T.Callable[[_T], Maybe[_U]]) -> Maybe[_U]:
        return Nothing()
    __rshift__ = bind

    def fmap(self, f: T.Callable[[_T], _U]) -> Maybe[_U]:
        return Nothing()
    __mul__ = fmap

    def __repr__(self) -> str:
        return 'Nothing()'
