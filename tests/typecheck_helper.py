from mypy.api import run
from typing import List, NamedTuple, Sequence, Union


class TypecheckResult(NamedTuple):
    ok: bool
    errors: List[str]


def typecheck(program: Union[str, Sequence[str]]) -> TypecheckResult:
    if program.__getitem__:
        prog = '\n'.join(program)
    else:
        prog = program
    stdout, stderr, exit_code = run(['--command', prog])
    if exit_code > 1:
        raise RuntimeError('mypy exited unexpectedly')
    return TypecheckResult(exit_code == 0, list(filter(None, stdout.split("\n"))))
