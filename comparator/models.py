"""
Data models using dataclasses.
https://docs.python.org/3/library/dataclasses.html
"""

from dataclasses import dataclass


@dataclass(kw_only=True)
class ERC20Contract:
    """
    This model represents an ERC-20 contract on a specified chain.
    """

    blockchain: str
    address: str
    rpc_url: str
    decimals: int
