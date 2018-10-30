from boiga.compose import (
    compose2, compose3, compose4, compose5, compose6, compose7
    )
from tests.typecheck_helper import TypecheckResult, typecheck


# Ideally, these are @dataclass, but not in Python 3.6
class _Flow0:
    a: int
    def __init__(self, a: int) -> None: self.a = a  # noqa: E301
    def __eq__(self, other: object) -> bool:  # noqa: E301
        return isinstance(other, _Flow0) and (self.a == other.a)
class _Flow1:  # noqa: E302
    b: int
    def __init__(self, b: int) -> None: self.b = b  # noqa: E301
    def __eq__(self, other: object) -> bool:  # noqa: E301
        return isinstance(other, _Flow1) and (self.b == other.b)
class _Flow2:  # noqa: E302
    c: int
    def __init__(self, c: int) -> None: self.c = c  # noqa: E301
    def __eq__(self, other: object) -> bool:  # noqa: E301
        return isinstance(other, _Flow2) and (self.c == other.c)
class _Flow3:  # noqa: E302
    d: int
    def __init__(self, d: int) -> None: self.d = d  # noqa: E301
    def __eq__(self, other: object) -> bool:  # noqa: E301
        return isinstance(other, _Flow3) and (self.d == other.d)
class _Flow4:  # noqa: E302
    e: int
    def __init__(self, e: int) -> None: self.e = e  # noqa: E301
    def __eq__(self, other: object) -> bool:  # noqa: E301
        return isinstance(other, _Flow4) and (self.e == other.e)
class _Flow5:  # noqa: E302
    f: int
    def __init__(self, f: int) -> None: self.f = f  # noqa: E301
    def __eq__(self, other: object) -> bool:  # noqa: E301
        return isinstance(other, _Flow5) and (self.f == other.f)
class _Flow6:  # noqa: E302
    g: int
    def __init__(self, g: int) -> None: self.g = g  # noqa: E301
    def __eq__(self, other: object) -> bool:  # noqa: E301
        return isinstance(other, _Flow6) and (self.g == other.g)
class _Flow7:  # noqa: E302
    h: int
    def __init__(self, h: int) -> None: self.h = h  # noqa: E301
    def __eq__(self, other: object) -> bool:  # noqa: E301
        return isinstance(other, _Flow7) and (self.h == other.h)


def _flow0(x: _Flow0) -> _Flow1: return _Flow1(x.a)
def _flow1(x: _Flow1) -> _Flow2: return _Flow2(x.b)  # noqa: E302
def _flow2(x: _Flow2) -> _Flow3: return _Flow3(x.c)  # noqa: E302
def _flow3(x: _Flow3) -> _Flow4: return _Flow4(x.d)  # noqa: E302
def _flow4(x: _Flow4) -> _Flow5: return _Flow5(x.e)  # noqa: E302
def _flow5(x: _Flow5) -> _Flow6: return _Flow6(x.f)  # noqa: E302
def _flow6(x: _Flow6) -> _Flow7: return _Flow7(x.g)  # noqa: E302


imports = [
    'from boiga.compose import compose2, compose3, compose4, compose5, compose6, compose7',
    'from tests.test_compose import _flow0, _flow1, _flow2, _flow3, _flow4, _flow5, _flow6',
    'from tests.test_compose import _Flow0, _Flow1, _Flow2, _Flow3, _Flow4, _Flow5, _Flow6, _Flow7',
    ]


def typecheck_flow(code: str) -> TypecheckResult:
    return typecheck([*imports, code])


class TestCompose2:
    def test_valid_flow_with_call(self) -> None:
        assert compose2(_flow0, _flow1)(_Flow0(42)) == _Flow2(42)

    def test_valid_flow_typechecks(self) -> None:
        result = typecheck_flow('compose2(_flow0, _flow1)')
        assert result.ok

    def test_invalid_flow_fns(self) -> None:
        result = typecheck_flow('compose2(_flow0, _flow0)')
        assert not result.ok
        assert result.errors == [
            '<string>:4: error: Cannot infer type argument 2 of "compose2"'
            ]

    def test_invalid_flow_call(self) -> None:
        result = typecheck_flow('compose2(_flow0, _flow1)(_Flow2(42))')
        assert not result.ok
        assert result.errors == [
            '<string>:4: error: Argument 1 has incompatible type "_Flow2"; expected "_Flow0"'
            ]

    def test_invalid_flow_result(self) -> None:
        result = typecheck_flow('compose2(_flow0, _flow1)(_Flow0(42)).foo')
        assert not result.ok
        assert result.errors == [
            '<string>:4: error: "_Flow2" has no attribute "foo"'
            ]


class TestCompose3:
    def test_valid_flow_with_call(self) -> None:
        flow = compose3(_flow0, _flow1, _flow2)
        assert flow(_Flow0(42)) == _Flow3(42)

    def test_valid_flow_typechecks(self) -> None:
        result = typecheck_flow('compose3(_flow0, _flow1, _flow2)')
        assert result.ok

    def test_invalid_flow_fns(self) -> None:
        result = typecheck_flow('compose3(_flow0, _flow1, _flow0)')
        assert not result.ok
        assert result.errors == [
            '<string>:4: error: Cannot infer type argument 3 of "compose3"'
            ]

    def test_invalid_flow_call(self) -> None:
        result = typecheck_flow('compose3(_flow0, _flow1, _flow2)(_Flow2(42))')
        assert not result.ok
        assert result.errors == [
            '<string>:4: error: Argument 1 has incompatible type "_Flow2"; expected "_Flow0"'
            ]

    def test_invalid_flow_result(self) -> None:
        result = typecheck_flow('compose3(_flow0, _flow1, _flow2)(_Flow0(42)).foo')
        assert not result.ok
        assert result.errors == [
            '<string>:4: error: "_Flow3" has no attribute "foo"'
            ]


class TestCompose4:
    def test_valid_flow_with_call(self) -> None:
        flow = compose4(_flow0, _flow1, _flow2, _flow3)
        assert flow(_Flow0(42)) == _Flow4(42)

    def test_valid_flow_typechecks(self) -> None:
        result = typecheck_flow('compose4(_flow0, _flow1, _flow2, _flow3)')
        assert result.ok

    def test_invalid_flow_fns(self) -> None:
        result = typecheck_flow('compose4(_flow0, _flow1, _flow2, _flow0)')
        assert not result.ok
        assert result.errors == [
            '<string>:4: error: Cannot infer type argument 4 of "compose4"'
            ]

    def test_invalid_flow_call(self) -> None:
        result = typecheck_flow('compose4(_flow0, _flow1, _flow2, _flow3)(_Flow2(42))')
        assert not result.ok
        assert result.errors == [
            '<string>:4: error: Argument 1 has incompatible type "_Flow2"; expected "_Flow0"'
            ]

    def test_invalid_flow_result(self) -> None:
        result = typecheck_flow('compose4(_flow0, _flow1, _flow2, _flow3)(_Flow0(42)).foo')
        assert not result.ok
        assert result.errors == [
            '<string>:4: error: "_Flow4" has no attribute "foo"'
            ]


class TestCompose5:
    def test_valid_flow_with_call(self) -> None:
        flow = compose5(_flow0, _flow1, _flow2, _flow3, _flow4)
        assert flow(_Flow0(42)) == _Flow5(42)

    def test_valid_flow_typechecks(self) -> None:
        result = typecheck_flow('compose5(_flow0, _flow1, _flow2, _flow3, _flow4)')
        assert result.ok

    def test_invalid_flow_fns(self) -> None:
        result = typecheck_flow('compose5(_flow0, _flow1, _flow2, _flow3, _flow0)')
        assert not result.ok
        assert result.errors == [
            '<string>:4: error: Cannot infer type argument 5 of "compose5"'
            ]

    def test_invalid_flow_call(self) -> None:
        result = typecheck_flow(
            'compose5(_flow0, _flow1, _flow2, _flow3, _flow4)(_Flow2(42))')
        assert not result.ok
        assert result.errors == [
            '<string>:4: error: Argument 1 has incompatible type "_Flow2"; expected "_Flow0"'
            ]

    def test_invalid_flow_result(self) -> None:
        result = typecheck_flow(
            'compose5(_flow0, _flow1, _flow2, _flow3, _flow4)(_Flow0(42)).foo')
        assert not result.ok
        assert result.errors == [
            '<string>:4: error: "_Flow5" has no attribute "foo"'
            ]


class TestCompose6:
    def test_valid_flow_with_call(self) -> None:
        flow = compose6(_flow0, _flow1, _flow2, _flow3, _flow4, _flow5)
        assert flow(_Flow0(42)) == _Flow6(42)

    def test_valid_flow_typechecks(self) -> None:
        result = typecheck_flow('compose6(_flow0, _flow1, _flow2, _flow3, _flow4, _flow5)')
        assert result.ok

    def test_invalid_flow_fns(self) -> None:
        result = typecheck_flow('compose6(_flow0, _flow1, _flow2, _flow3, _flow4, _flow0)')
        assert not result.ok
        assert result.errors == [
            '<string>:4: error: Cannot infer type argument 6 of "compose6"'
            ]

    def test_invalid_flow_call(self) -> None:
        result = typecheck_flow(
            'compose6(_flow0, _flow1, _flow2, _flow3, _flow4, _flow5)(_Flow2(42))')
        assert not result.ok
        assert result.errors == [
            '<string>:4: error: Argument 1 has incompatible type "_Flow2"; expected "_Flow0"'
            ]

    def test_invalid_flow_result(self) -> None:
        result = typecheck_flow(
            'compose6(_flow0, _flow1, _flow2, _flow3, _flow4, _flow5)(_Flow0(42)).foo')
        assert not result.ok
        assert result.errors == [
            '<string>:4: error: "_Flow6" has no attribute "foo"'
            ]


class TestCompose7:
    def test_valid_flow_with_call(self) -> None:
        flow = compose7(_flow0, _flow1, _flow2, _flow3, _flow4, _flow5, _flow6)
        assert flow(_Flow0(42)) == _Flow7(42)

    def test_valid_flow_typechecks(self) -> None:
        result = typecheck_flow('compose7(_flow0, _flow1, _flow2, _flow3, _flow4, _flow5, _flow6)')
        assert result.ok

    def test_invalid_flow_fns(self) -> None:
        result = typecheck_flow('compose7(_flow0, _flow1, _flow2, _flow3, _flow4, _flow5, _flow0)')
        assert not result.ok
        assert result.errors == [
            '<string>:4: error: Cannot infer type argument 7 of "compose7"'
            ]

    def test_invalid_flow_call(self) -> None:
        result = typecheck_flow(
            'compose7(_flow0, _flow1, _flow2, _flow3, _flow4, _flow5, _flow6)(_Flow2(42))')
        assert not result.ok
        assert result.errors == [
            '<string>:4: error: Argument 1 has incompatible type "_Flow2"; expected "_Flow0"'
            ]

    def test_invalid_flow_result(self) -> None:
        result = typecheck_flow(
            'compose7(_flow0, _flow1, _flow2, _flow3, _flow4, _flow5, _flow6)(_Flow0(42)).foo')
        assert not result.ok
        assert result.errors == [
            '<string>:4: error: "_Flow7" has no attribute "foo"'
            ]
