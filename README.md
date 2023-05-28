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

- concurrency *(see main.py)*
- type hints/annotation *(used throughout the codebase)*
- iterators and generators *(see main.py, commented in the main function)*
- context managers *(see main.py - main function)*
- lambda (anonymous) functions *(see main.py, commented in the main function)*


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
