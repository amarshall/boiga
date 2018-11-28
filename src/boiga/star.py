from typing import Callable, Tuple, TypeVar

R = TypeVar('R')
T = TypeVar('T')
U = TypeVar('U')
V = TypeVar('V')
W = TypeVar('W')
X = TypeVar('X')
Y = TypeVar('Y')
Z = TypeVar('Z')


def star2(fn: Callable[[T, U], R]) -> Callable[[Tuple[T, U]], R]:
    def fn2(tup: Tuple[T, U]) -> R:
        (t, u) = tup
        return fn(t, u)
    return fn2


def star3(fn: Callable[[T, U, V], R]) -> Callable[[Tuple[T, U, V]], R]:
    def fn2(tup: Tuple[T, U, V]) -> R:
        (t, u, v) = tup
        return fn(t, u, v)
    return fn2


def star4(fn: Callable[[T, U, V, W], R]) -> Callable[[Tuple[T, U, V, W]], R]:
    def fn2(tup: Tuple[T, U, V, W]) -> R:
        (t, u, v, w) = tup
        return fn(t, u, v, w)
    return fn2


def star5(fn: Callable[[T, U, V, W, X], R]) -> Callable[[Tuple[T, U, V, W, X]], R]:
    def fn2(tup: Tuple[T, U, V, W, X]) -> R:
        (t, u, v, w, x) = tup
        return fn(t, u, v, w, x)
    return fn2
