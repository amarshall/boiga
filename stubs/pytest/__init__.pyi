from contextlib import contextmanager
from typing import Iterator, Type


@contextmanager
def raises(
        exc_cls: Type[BaseException],
        message: str = None,
        ) -> Iterator[None]: ...
