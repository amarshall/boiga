from typing import Callable, TypeVar, Union, cast, overload

R = TypeVar('R')
T = TypeVar('T')
U = TypeVar('U')
V = TypeVar('V')
W = TypeVar('W')
X = TypeVar('X')
Y = TypeVar('Y')
Z = TypeVar('Z')


class _Absent:
    pass


_absent = _Absent()


@overload
def partial2(f: Callable[[T, U], R]) -> Callable[[T, U], R]: ...
@overload  # noqa: E302,F811
def partial2(f: Callable[[T, U], R], a: T) -> Callable[[U], R]: ...

def partial2(  # noqa: E302,F811
        f: Callable[[T, U], R],
        a: Union[T, _Absent] = _absent,
        ) -> Union[
            Callable[[T, U], R],
            Callable[[U], R],
            ]:
    if isinstance(a, _Absent):
        return f
    else:
        def g(b: U) -> R:
            a2 = cast(T, a)
            return f(a2, b)
    return g


@overload
def partial3(f: Callable[[T, U, V], R]) -> Callable[[T, U, V], R]: ...
@overload  # noqa: E302,F811
def partial3(f: Callable[[T, U, V], R], a: T) -> Callable[[U, V], R]: ...
@overload  # noqa: E302,F811
def partial3(f: Callable[[T, U, V], R], a: T, b: U) -> Callable[[V], R]: ...

def partial3(  # noqa: E302,F811
        f: Callable[[T, U, V], R],
        a: Union[T, _Absent] = _absent,
        b: Union[U, _Absent] = _absent,
        ) -> Union[
            Callable[[T, U, V], R],
            Callable[[U, V], R],
            Callable[[V], R],
            ]:
    if isinstance(a, _Absent):
        return f
    if isinstance(b, _Absent):
        def g2(b: U, c: V) -> R:
            a2 = cast(T, a)
            return f(a2, b, c)
        return g2
    else:
        def g1(c2: V) -> R:
            a2 = cast(T, a)
            b2 = cast(U, b)
            return f(a2, b2, c2)
        return g1


@overload
def partial4(f: Callable[[T, U, V, W], R]) -> Callable[[T, U, V, W], R]: ...
@overload  # noqa: E302,F811
def partial4(f: Callable[[T, U, V, W], R], a: T) -> Callable[[U, V, W], R]: ...
@overload  # noqa: E302,F811
def partial4(f: Callable[[T, U, V, W], R], a: T, b: U) -> Callable[[V, W], R]: ...
@overload  # noqa: E302,F811
def partial4(f: Callable[[T, U, V, W], R], a: T, b: U, c: V) -> Callable[[W], R]: ...

def partial4(  # noqa: E302,F811
        f: Callable[[T, U, V, W], R],
        a: Union[T, _Absent] = _absent,
        b: Union[U, _Absent] = _absent,
        c: Union[V, _Absent] = _absent,
        ) -> Union[
            Callable[[T, U, V, W], R],
            Callable[[U, V, W], R],
            Callable[[V, W], R],
            Callable[[W], R],
            ]:
    if isinstance(a, _Absent):
        return f
    elif isinstance(b, _Absent):
        def g3(b: U, c: V, d: W) -> R:
            a2 = cast(T, a)
            return f(a2, b, c, d)
        return g3
    elif isinstance(c, _Absent):
        def g2(c: V, d: W) -> R:
            a2 = cast(T, a)
            b2 = cast(U, b)
            return f(a2, b2, c, d)
        return g2
    else:
        def g1(d: W) -> R:
            a2 = cast(T, a)
            b2 = cast(U, b)
            c2 = cast(V, c)
            return f(a2, b2, c2, d)
        return g1
