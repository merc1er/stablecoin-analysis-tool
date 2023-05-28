<div align="center">
  <h1>Stablecoin analysis tool</h1>
  <p>This tool is made as part of the "Next-Level Python: Become a Python Expert" course assignment.</p>
</div>


## Overview

**Stablecoin market capitalization comparator.**


### Description

This Python program fetches the supply of the USDT and USDC stablecoins on different
blockchains (Ethereum, Polygon), and compares the data.

It uses the following concepts taught in the course:

- concurrency
- type hints/annotation
- iterators and generators
- context managers
- lambda (anonymous) functions


### Workflow diagram

![Workflow diagram](diagram.svg)


## Lesson notes

Dataclasses:
- @dataclass
- default_factory, init=False
- setter


Functools:
- @cached_property
- @singledispatch


Concurrent programming:
- asyncio.gather()


Iterators:
- generators (lazy)
- yield
