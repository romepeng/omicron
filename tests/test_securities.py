#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author: Aaron-Yang [code@jieyu.ai]
Contributors:

"""
import logging
import os
import unittest

import cfg4py
from pyemit import emit

from omicron.models.securities import Securities

from omicron.core.lang import async_run

from omicron.dal import cache, RedisDB

logger = logging.getLogger(__name__)


class TestSecurity(unittest.TestCase):
    """Tests for `omicron` package."""

    @async_run
    async def setUp(self) -> None:
        """Set up test fixtures, if any."""
        os.environ[cfg4py.envar] = 'TEST'
        home = os.path.dirname(__file__)
        config_path = os.path.join(home, '../omicron/config')

        cfg = cfg4py.init(config_path)
        await cache.init()
        await emit.start(emit.Engine.REDIS, dsn=cfg.redis.dsn, exchange='zillionare-omega')

    def tearDown(self):
        """Tear down test fixtures, if any."""

    @async_run
    async def test_000_load(self):
        s = Securities()

        # invalidate cache, then load from remote
        await cache.get_db(RedisDB.SECURITY).delete('securities')
        await s.load()
        logger.info(s)
        self.assertEqual(s[0]['code'], '000001.XSHE')

        # read from cache
        s.reset()
        await s.load()
        self.assertEqual(s[0]['code'], '000001.XSHE')
        self.assertEqual(s['000001.XSHE']['display_name'], '平安银行')
