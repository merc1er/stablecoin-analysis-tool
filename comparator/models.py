"""
Data models using dataclasses.
https://docs.python.org/3/library/dataclasses.html
"""

from math import floor
from decimal import Decimal
from dataclasses import dataclass
from functools import cached_property


@dataclass(kw_only=True)
class ERC20Contract:
    """
    This model represents an ERC-20 contract on a specified chain.
    """

    blockchain: str
    address: str
    rpc_url: str
    decimals: int


@dataclass(kw_only=True)
class TotalSupply:
    """
    This model represents the total supply of a given ERC-20 token on a given
    blockchain.
    """

    value: Decimal
    blockchain: str

    @cached_property
    def floored_value(self) -> int:
        return floor(self.value)
