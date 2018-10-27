# Boiga: type-safe functional Python

[![PyPI package](https://img.shields.io/pypi/v/boiga.svg)](https://pypi.org/project/boiga/)
[![Build Status](https://secure.travis-ci.org/amarshall/boiga.svg?branch=master)](https://travis-ci.org/amarshall/boiga)

Unlike most functional programming and monad libraries for Python, this is well-typed thanks to [PEP 484](https://www.python.org/dev/peps/pep-0484/) and [mypy](http://www.mypy-lang.org/).

## Type-safety

Boiga is only as type-safe as mypy permits. However, Boiga makes every attempt to ensure maximal type-safety. This includes:

- Enabling various mypy flags to increase strictness
- Type-checking all test code
- Having tests which programatically run mypy and ensure that expected type-check failures do indeed fail to type-check

## Why “Boiga”?

Boiga is a genus of snake, often nicknamed “cat snakes”. The level of functional *cat*egory theory in this library is perhaps “un-Pythonic”. But it’s still a snake, just not a Python—a cat-eyed snake, perhaps. Also, most of the obvious package names were already taken.

## Mypy bugs found

- [Lambda as RHS for operator always gets inferred as Any](https://github.com/python/mypy/issues/5843)
