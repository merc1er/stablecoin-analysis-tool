"""
This module keeps track of the ERC-20 smart contracts that we want to analyze.
"""

from models import ERC20Contract


# Tether (USDT) smart contract addresses list.
# https://coinmarketcap.com/currencies/tether/
usdt_contracts = [
    ERC20Contract(
        blockchain="ethereum",
        address="0xdac17f958d2ee523a2206206994597c13d831ec7",
        rpc_url="https://rpc.ankr.com/eth",
        decimals=6,
    ),
    ERC20Contract(
        blockchain="bnb_smart_chain",
        address="0x55d398326f99059ff775485246999027b3197955",
        rpc_url="https://rpc.ankr.com/bsc",
        decimals=18,
    ),
    ERC20Contract(
        blockchain="polygon",
        address="0xc2132d05d31c914a87c6611c10748aeb04b58e8f",
        rpc_url="https://rpc.ankr.com/polygon",
        decimals=6,
    ),
    ERC20Contract(
        blockchain="avalanche",
        address="0x9702230A8Ea53601f5cD2dc00fDBc13d4dF4A8c7",
        rpc_url="https://rpc.ankr.com/avalanche",
        decimals=6,
    ),
    ERC20Contract(
        blockchain="arbitrum",
        address="0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9",
        rpc_url="https://rpc.ankr.com/arbitrum",
        decimals=6,
    ),
    # this list is not exhaustive
]
