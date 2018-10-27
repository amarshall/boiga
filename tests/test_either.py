from boiga.either import Either, Left, Right
from tests.typecheck_helper import typecheck
import typing as T

_T = T.TypeVar('_T')
_U = T.TypeVar('_U')


class TestEitherBind():
    def test_left_bind_is_no_op(self) -> None:
        def oops(x: int) -> Either[str, int]: raise
        either: Either[str, int] = Left('err')
        assert either.bind(oops) == Left('err')

    def test_right_bind_calls_with_value(self) -> None:
        def inc(x: int) -> Either[_T, int]: return Right(x + 1)
        assert Right(1).bind(inc) == Right(2)
        assert (Right(1) >> inc) == Right(2)

    def test_right_bind_calls_with_value_other_type(self) -> None:
        def f(x: _T) -> Either[_U, str]: return Right('yay')
        assert Right(1).bind(f) == Right('yay')
        assert (Right(1) >> f) == Right('yay')

    def _test_bind_typecheck(
            self, val: str, fn_def: str, sig: str,
            expected: str = 'Callable[[int], Either[str, int]]',
            ) -> None:
        result = typecheck([
            "from boiga.either import Either, Left, Right",
            "either: Either[str, int] = Left('err')",
            fn_def,
            "either.bind(fn)",
            ])
        assert not result.ok
        assert result.errors == [
            '<string>:4: error: Argument 1 to "bind" of "Either" has incompatible type '
            f'"{sig}"; '
            f'expected "{expected}"'
            ]

    def test_left_bind_with_invalid_fn_param(self) -> None:
        self._test_bind_typecheck(
            val='Left("err")',
            fn_def='def fn(x: str) -> Either[str, int]: ...',
            sig='Callable[[str], Either[str, int]]',
            )

    def test_right_bind_with_invalid_fn_param(self) -> None:
        self._test_bind_typecheck(
            val='Right(42)',
            fn_def='def fn(x: str) -> Either[str, int]: ...',
            sig='Callable[[str], Either[str, int]]',
            )

    def test_left_bind_with_invalid_fn_return_left_type(self) -> None:
        self._test_bind_typecheck(
            val='Left("err")',
            fn_def='def fn(x: int) -> Either[int, int]: ...',
            sig='Callable[[int], Either[int, int]]',
            )

    def test_right_bind_with_invalid_fn_return_right_type(self) -> None:
        self._test_bind_typecheck(
            val='Right(42)',
            fn_def="def fn(x: int) -> Either[int, int]: ...",
            sig='Callable[[int], Either[int, int]]',
            )

    def test_left_bind_with_invalid_fn_return_type(self) -> None:
        self._test_bind_typecheck(
            val='Left("err")',
            fn_def="def fn(x: int) -> int: ...",
            sig='Callable[[int], int]',
            expected='Callable[[int], Either[str, <nothing>]]',
            )

    def test_right_bind_with_invalid_fn_return_type(self) -> None:
        self._test_bind_typecheck(
            val='Right(42)',
            fn_def="def fn(x: int) -> int: ...",
            sig='Callable[[int], int]',
            expected='Callable[[int], Either[str, <nothing>]]',
            )


class TestEitherFmap():
    def test_left_fmap_is_no_op(self) -> None:
        def oops(x: int) -> str: raise
        either: Either[str, int] = Left('err')
        assert either.fmap(oops) == Left('err')

    def test_right_fmap_calls_with_value(self) -> None:
        assert Right(1).fmap(lambda x: x + 1) == Right(2)

    def test_right_fmap_calls_with_value_other_type(self) -> None:
        assert Right(1).fmap(lambda x: 'yay') == Right('yay')

    def _test_fmap_typecheck(
            self, val: str, fn_def: str, sig: str,
            expected: str = 'Callable[[int], int]',
            ) -> None:
        result = typecheck([
            "from boiga.either import Either, Left, Right",
            "either: Either[str, int] = Left('err')",
            fn_def,
            "either.fmap(fn)",
            ])
        assert not result.ok
        assert result.errors == [
            '<string>:4: error: Argument 1 to "fmap" of "Either" has incompatible type '
            f'"{sig}"; '
            f'expected "{expected}"'
            ]

    def test_left_fmap_with_invalid_fn_param(self) -> None:
        self._test_fmap_typecheck(
            val='Left("err")',
            fn_def='def fn(x: str) -> int: ...',
            sig='Callable[[str], int]',
            )

    def test_right_fmap_with_invalid_fn_param(self) -> None:
        self._test_fmap_typecheck(
            val='Right(42)',
            fn_def='def fn(x: str) -> int: ...',
            sig='Callable[[str], int]',
            )


class TestEitherRepr():
    def test_left(self) -> None:
        assert Left(314).__repr__() == 'Left(314)'

    def test_right(self) -> None:
        assert Right(42).__repr__() == 'Right(42)'
