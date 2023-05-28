<div align="center">
  <h1>Stablecoin analysis tool</h1>
  <p><b>This tool is made as part of the <a href="https://www.skillshare.com/en/classes/Next-Level-Python-Become-a-Python-Expert/1997963259?via=search-layout-grid">"Next-Level Python: Become a Python Expert"</a> Skillshare course assignment.</b></p>
</div>


## Overview

**Stablecoin market capitalization comparator.**


### Description

This Python program fetches the supply of the [USDT](https://coinmarketcap.com/currencies/tether/)
stablecoin on different blockchains (Ethereum, Polygon, etc), and compares the data.

It uses the following concepts taught in the course:

- [X] concurrency
- [X] type hints/annotation
- [ ] iterators and generators
- [X] context managers
- [ ] lambda (anonymous) functions


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
