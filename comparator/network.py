"""
Module responsible for network calls. It makes use of the requests library.
"""

import logging
import asyncio
import requests

logger = logging.getLogger(__name__)


JSON = int | str | float | bool | None | dict[str, "JSON"] | list["JSON"]
JSONObject = dict[str, JSON]


def _http_post_sync(url: str, payload: dict = {}) -> JSONObject | None:
    """
    Performs an HTTP POST request to the passed URL, with the passed JSON body payload.

    Args:
        url: The URL to query.
        payload: The JSON body to submit, in dict format.

    Returns:
        A JSONObject if the request is successful, None otherwise.
    """

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"HTTP request to {url} errored: {str(e)}")
        return None


async def http_post(url: str, payload: dict = {}) -> JSONObject | None:
    """
    Asynchronous call of _http_post_sync.
    """

    return await asyncio.to_thread(_http_post_sync, url, payload)
