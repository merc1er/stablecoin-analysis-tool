import logging
import asyncio
from math import floor
from decimal import Decimal
from time import perf_counter
from datetime import datetime

from contracts import usdt_contracts
from models import ERC20Contract, TotalSupply
from network import http_post


# Logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


def convert_total_supply_value(hex_value: str, decimals: int) -> Decimal:
    """
    The value returned when calling totalSupply() via RPC call is in hexadecimal and raw
    integer format.

    This function converts it into a decimal, human readable format.

    Args:
        hex_value: The total supply in raw integer hexadecimal value.
        decimals: The amount of decimal places for the token. This is part of the ERC-20
            standard.

    Returns:
        The human-readable Decimal representation of the total supply.
    """

    raw_integer_value = int(hex_value, 16)
    decimal_value = raw_integer_value / 10 ** Decimal(decimals)

    return decimal_value


async def get_total_supply(contract: ERC20Contract) -> TotalSupply | None:
    """
    Gets the total supply of a given ERC-20 contract.

    Args:
        contract: The ERC20Contract object of the token we want the supply of.

    Returns:
        ... None otherwise.
    """

    logger.info(f"Getting total supply on the following chain: {contract.blockchain}.")

    payload = {
        "jsonrpc": "2.0",
        "method": "eth_call",
        "params": [
            {
                "to": contract.address,
                "data": "0x18160ddd",  # totalSupply() function
            },
            "latest",
        ],
        "id": 1,
    }

    json_response = await http_post(url=contract.rpc_url, payload=payload)

    if not json_response:
        return None

    logger.debug(json_response)
    total_supply = convert_total_supply_value(
        str(json_response["result"]), contract.decimals
    )

    # Format the total supply nicely for better readability.
    readable_total_supply = format(floor(total_supply), ",")
    logger.info(
        f"Total supply on {contract.blockchain} is: {readable_total_supply} USDT."
    )

    return TotalSupply(blockchain=contract.blockchain, value=total_supply)


async def main() -> None:
    # fetch the supply for those tokens using the JSON RPC API
    time_before = perf_counter()
    data = await asyncio.gather(
        *[get_total_supply(contract) for contract in usdt_contracts]
    )
    logger.info(f"Total execution time: {perf_counter() - time_before} seconds.")

    # Save the data into a CSV file.
    with open("comparator/output.csv", "a") as f:
        for item in data:
            line = f"{datetime.now()},{item.blockchain},{item.floored_value}\n"
            f.write(line)


asyncio.run(main())
