import typing as T

_T = T.TypeVar('_T')


class _Container(T.Generic[_T]):
    _value: _T

    def __eq__(self, other: object) -> bool:
        if isinstance(other, self.__class__):
            return self._value == other._value
        else:
            return False
