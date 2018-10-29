from boiga.partial import partial2, partial3, partial4
from hypothesis import given
import hypothesis.strategies as strats


class TestPartial2:
    @staticmethod
    def sum2(a: int, b: int) -> int:
        return a + b

    @given(strats.integers(), strats.integers())  # type: ignore
    def test_with_0_arg(self, a: int, b: int) -> None:  # type: ignore
        assert partial2(self.sum2)(a, b) == self.sum2(a, b)

    @given(strats.integers(), strats.integers())  # type: ignore
    def test_with_1_arg(self, a: int, b: int) -> None:  # type: ignore
        assert partial2(self.sum2, a)(b) == self.sum2(a, b)


class TestPartial3:
    @staticmethod
    def sum3(a: int, b: int, c: int) -> int:
        return a + b + c

    @given(strats.integers(), strats.integers(), strats.integers())  # type: ignore
    def test_with_0_arg(self, a: int, b: int, c: int) -> None:  # type: ignore
        assert partial3(self.sum3)(a, b, c) == self.sum3(a, b, c)

    @given(strats.integers(), strats.integers(), strats.integers())  # type: ignore
    def test_with_1_arg(self, a: int, b: int, c: int) -> None:  # type: ignore
        assert partial3(self.sum3, a)(b, c) == self.sum3(a, b, c)

    @given(strats.integers(), strats.integers(), strats.integers())  # type: ignore
    def test_with_2_arg(self, a: int, b: int, c: int) -> None:  # type: ignore
        assert partial3(self.sum3, a, b)(c) == self.sum3(a, b, c)


class TestPartial4:
    @staticmethod
    def sum4(a: int, b: int, c: int, d: int) -> int:
        return a + b + c + d

    @given(  # type: ignore
        strats.integers(), strats.integers(),  # type: ignore
        strats.integers(), strats.integers(),
        )
    def test_with_0_arg(self, a: int, b: int, c: int, d: int) -> None:
        assert partial4(self.sum4)(a, b, c, d) == self.sum4(a, b, c, d)

    @given(  # type: ignore
        strats.integers(), strats.integers(),  # type: ignore
        strats.integers(), strats.integers(),
        )
    def test_with_1_arg(self, a: int, b: int, c: int, d: int) -> None:
        assert partial4(self.sum4, a)(b, c, d) == self.sum4(a, b, c, d)

    @given(  # type: ignore
        strats.integers(), strats.integers(),  # type: ignore
        strats.integers(), strats.integers(),
        )
    def test_with_2_arg(self, a: int, b: int, c: int, d: int) -> None:
        assert partial4(self.sum4, a, b)(c, d) == self.sum4(a, b, c, d)

    @given(  # type: ignore
        strats.integers(), strats.integers(),  # type: ignore
        strats.integers(), strats.integers(),
        )
    def test_with_3_arg(self, a: int, b: int, c: int, d: int) -> None:
        assert partial4(self.sum4, a, b, c)(d) == self.sum4(a, b, c, d)
