from typing import Callable, TypeVar

R = TypeVar('R')
T = TypeVar('T')
U = TypeVar('U')
V = TypeVar('V')
W = TypeVar('W')
X = TypeVar('X')
Y = TypeVar('Y')
Z = TypeVar('Z')


def compose2(
        f: Callable[[T], U],
        g: Callable[[U], R],
        ) -> Callable[[T], R]:
    def composed(x: T) -> R:
        return g(f(x))
    return composed


def compose3(
        f: Callable[[T], U],
        g: Callable[[U], V],
        h: Callable[[V], R],
        ) -> Callable[[T], R]:
    def composed(x: T) -> R:
        return h(g(f(x)))
    return composed


def compose4(
        f: Callable[[T], U],
        g: Callable[[U], V],
        h: Callable[[V], W],
        i: Callable[[W], R],
        ) -> Callable[[T], R]:
    def composed(x: T) -> R:
        return i(h(g(f(x))))
    return composed


def compose5(
        f: Callable[[T], U],
        g: Callable[[U], V],
        h: Callable[[V], W],
        i: Callable[[W], X],
        j: Callable[[X], R],
        ) -> Callable[[T], R]:
    def composed(x: T) -> R:
        return j(i(h(g(f(x)))))
    return composed


def compose6(
        f: Callable[[T], U],
        g: Callable[[U], V],
        h: Callable[[V], W],
        i: Callable[[W], X],
        j: Callable[[X], Y],
        k: Callable[[Y], R],
        ) -> Callable[[T], R]:
    def composed(x: T) -> R:
        return k(j(i(h(g(f(x))))))
    return composed


def compose7(
        f: Callable[[T], U],
        g: Callable[[U], V],
        h: Callable[[V], W],
        i: Callable[[W], X],
        j: Callable[[X], Y],
        k: Callable[[Y], Z],
        l: Callable[[Z], R],
        ) -> Callable[[T], R]:
    def composed(x: T) -> R:
        return l(k(j(i(h(g(f(x)))))))
    return composed
