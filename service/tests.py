"""
Testing file for all modules in the Service Package
"""

import logging
import unittest
from service.esi import EsiHandler
from service.fitparser import Parser


class TestEsi(unittest.TestCase):
    def test_request_market_groups(self):
        """
        Tests EsiHandler.request_market_groups()
        """
        result = EsiHandler.request_market_groups()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)

    def test_request_type_info(self):
        """
        Tests EsiHandler.request_type_info()
        """
        # Valid type ID
        # Insulated Stabilizer Array=11111
        result = EsiHandler.request_type_info(11111)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        self.assertEqual(result['name'], "Insulated Stabilizer Array")
        self.assertEqual(result['group_id'], 302)

        # Invalid type ID
        result = EsiHandler.request_type_info(111111111)
        self.assertIsNone(result)

        # Non-Integer type ID
        result = EsiHandler.request_type_info("aaaaa")
        self.assertIsNone(result)

    def test_request_regions(self):
        """
        Tests EsiHandler.request_regions()
        """
        result = EsiHandler.request_regions()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)

    def test_request_region_info(self):
        """
        Tests EsiHandler.request_region_info()
        """
        # Valid region ID
        # The Forge=10000002
        result = EsiHandler.request_region_info(10000002)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        self.assertEqual(result['name'], "The Forge")

        # Invalid region ID
        result = EsiHandler.request_region_info(1111)
        self.assertIsNone(result)

        # Non-integer region ID
        result = EsiHandler.request_region_info("aaaa")
        self.assertIsNone(result)

    def test_request_market_region_history(self):
        """
        Tests EsiHandler.request_market_region_history()
        """
        # Valid type ID, valid region ID
        # Esoteria=10000039, Nanite Repair Paste=28668
        result = EsiHandler.request_market_region_history(10000039, 28668)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)

        # Invalid type ID
        result = EsiHandler.request_market_region_history(10000039, 11)
        self.assertIsNone(result)

        # Invalid region ID
        result = EsiHandler.request_market_region_history(1, 28668)
        self.assertIsNone(result)

        # Non-integer type ID
        result = EsiHandler.request_market_region_history(10000039, "aaaaa")
        self.assertIsNone(result)

        # Non-integer region ID
        result = EsiHandler.request_market_region_history("aaaaa", 28668)
        self.assertIsNone(result)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.info("Running all tests...")

    unittest.main()
