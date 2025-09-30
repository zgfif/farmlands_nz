import unittest
from applib.collect_data import CollectData


class TestCollectData(unittest.TestCase):
    def test_collecting_data(self):
        url = 'https://shop.farmlands.co.nz/collections/chicken-and-poultry'

        CollectData(url=url).perform()
