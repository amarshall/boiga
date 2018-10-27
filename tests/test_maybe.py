from boiga.maybe import Maybe, Just, Nothing
import pytest


def test_unit_with_non_none() -> None:
    assert Maybe.unit(42) == Just(42)


def test_unit_with_none() -> None:
    assert Maybe.unit(None) == Nothing()


def test_nothing_is_singleton() -> None:
    assert id(Nothing()) == id(Nothing())


def test_maybe_with_none() -> None:
    with pytest.raises(TypeError, message='use Nothing() instead of Just(None)'):
        Just(None)


class TestMaybeBind():
    def test_just_bind_calls_with_value(self) -> None:
        def inc(x: int) -> Maybe[int]: return Just(x + 1)
        maybe: Maybe[int] = Just(42)
        assert maybe.bind(inc) == Just(43)
        assert (maybe >> inc) == Just(43)

    def test_just_bind_calls_with_value_other_type(self) -> None:
        def inc(x: int) -> Maybe[str]: return Just('yay')
        maybe: Maybe[int] = Just(42)
        assert maybe.bind(inc) == Just('yay')
        assert (maybe >> inc) == Just('yay')

    def test_nothing_bind_is_no_op(self) -> None:
        def oops(x: int) -> Maybe[int]: raise
        maybe: Maybe[int] = Nothing()
        assert maybe.bind(oops) == Nothing()
        assert (maybe >> oops) == Nothing()


class TestMaybeFmap():
    def test_just_fmap_calls_with_value(self) -> None:
        def inc(x: int) -> int: return x + 1
        maybe: Maybe[int] = Just(42)
        assert maybe.fmap(inc) == Just(43)
        assert (maybe * inc) == Just(43)

    def test_just_fmap_calls_with_value_other_type(self) -> None:
        def f(x: int) -> str: return 'yay'
        maybe: Maybe[int] = Just(42)
        assert maybe.fmap(f) == Just('yay')
        assert (maybe * f) == Just('yay')

    def test_nothing_fmap_is_no_op(self) -> None:
        def oops(x: int) -> int: raise
        maybe: Maybe[int] = Nothing()
        assert maybe.fmap(oops) == Nothing()
        assert (maybe * oops) == Nothing()


class TestMaybeEq():
    def test_just_when_eq(self) -> None:
        obj = object()
        assert Just(obj) == Just(obj)

    def test_just_when_not_eq(self) -> None:
        assert Just(object()) != Just(object())

    def test_just_and_nothing(self) -> None:
        assert Just(object()) != Nothing()

    def test_nothing_and_nothing(self) -> None:
        assert Nothing() == Nothing()


class TestMaybeRepr():
    def test_just(self) -> None:
        assert Just(42).__repr__() == 'Just(42)'

    def test_nothing(self) -> None:
        assert Nothing().__repr__() == 'Nothing()'
