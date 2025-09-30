import unittest
from applib.request_items import RequestItems



class TestRequstItems(unittest.TestCase):
    def test_request_items(self):
        result = RequestItems().perform()
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 44)

