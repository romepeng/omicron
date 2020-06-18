#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author: Aaron-Yang [code@jieyu.ai]
Contributors: 

"""
import logging
import pickle

import aiohttp
import cfg4py
from arrow import Arrow

from omicron.core.types import FrameType
from omicron import get_local_fetcher

logger = logging.getLogger(__name__)
cfg = cfg4py.get_instance()


async def _quotes_server_get(item: str, params: dict = None):
    url = f"{cfg.omega.server.url}/quotes/{item}"
    try:
        async with aiohttp.ClientSession() as client:
            async with client.get(url, json=params) as resp:
                if resp.status == 200:
                    content = await resp.content.read(-1)
                    return pickle.loads(content)
    except aiohttp.ClientConnectionError as e:
        logger.exception(e)
        logger.warning("failed to fetch %s with args: %s", item, params)

    return None


async def get_security_list():
    fetcher = get_local_fetcher()
    if fetcher:
        return await fetcher.get_security_list()
    else:
        return await _quotes_server_get('security_list')


async def get_bars(code: str, end: Arrow, n_bars: int, frame_type: FrameType):
    fetcher = get_local_fetcher()
    if fetcher:
        return await fetcher.get_bars(code, end, n_bars, frame_type)
    else:
        params = {
            "code":       code,
            "end":        end.format("YYYYMMDD HH:mm"),
            "n_bars":     n_bars,
            "frame_type": frame_type.value
        }

        return await _quotes_server_get("bars", params)