import asyncio
from unittest import TestCase


class BaseTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls._loop = asyncio.get_event_loop()

    @classmethod
    def tearDownClass(cls):
        cls._loop.close()
