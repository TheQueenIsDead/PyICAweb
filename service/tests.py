"""
Testing file for all modules in the Service Package
"""

import logging
from service.esi import EsiHandler
from service.fitparser import Parser


def test_request_market_groups():
    """
    Tests EsiHandler.request_market_groups()
    :return: True if tests pass, default=false
    """
    try:
        result = EsiHandler.request_market_groups()
        assert result is not None, "Returned value cannot be NoneType."
        assert type(result) == list, "Returned type is not a list."
        assert len(result) > 0, "Returned list is empty."

    except AssertionError as error:
        logging.error("One or more tests failed at: EsiHandler.request_market_groups()")
        logging.error(error)
        return False

    return True


def test_request_type_info():
    """
    Tests EsiHandler.request_type_info()
    :return: True if tests pass, default=false
    """
    try:
        # Valid type ID
        result = EsiHandler.request_type_info(11111)
        assert result is not None, "Returned value cannot be NoneType."
        assert type(result) == dict, "Returned type is not dict."
        assert result['name'] == "Insulated Stabilizer Array", "Request is returning bad data."
        assert result['group_id'] == 302, "Request is returning bad data."

        # Invalid type ID
        result = EsiHandler.request_type_info(111111111)
        assert result is None, "Returned value is not None for invalid type ID."

        # Non-Integer type ID
        result = EsiHandler.request_type_info("aaaaa")
        assert result is None, "Returned value is not None for non-int type ID."

    except AssertionError as error:
        logging.error("One or more tests failed at: EsiHandler.request_type_info().")
        logging.error(error)
        return False

    return True


def test_request_regions():
    """
    Tests EsiHandler.request_regions()
    :return: True if tests pass, default=false
    """
    try:
        result = EsiHandler.request_regions()
        assert result is not None, "Returned value cannot be NoneType."
        assert type(result) == list, "Returned type is not a list."
        assert len(result) > 0, "Returned list is empty"

    except AssertionError as error:
        logging.error("One or more tests failed at: EsiHandler.request_regions().")
        logging.error(error)
        return False

    return True


def test_request_region_info():
    """
    Tests EsiHandler.request_region_info()
    :return: True if tests pass, default=false
    """
    try:
        # Valid region ID
        result = EsiHandler.request_region_info(10000002)
        assert result is not None, "Returned value cannot be NoneType"
        assert type(result) == dict, "Returned type is not dict"
        assert result['name'] == "The Forge", "Request is returning bad data."

        # Invalid region ID
        result = EsiHandler.request_region_info(1111)
        assert result is None, "Returned value is not None for invalid region ID"

        # Non-Integer region ID
        result = EsiHandler.request_region_info("aaaa")
        assert result is None, "Returned value is not None for a non-int region ID"

    except AssertionError as error:
        logging.error("One or more tests failed at: EsiHandler.request_region_info().")
        logging.error(error)
        return False

    return True


def test_request_market_region_history():
    """
    Tests EsiHandler.request_market_region_history()
    :return: True if tests pass, default=false
    """
    try:
        # Valid type ID, valid region ID
        result = EsiHandler.request_market_region_history(10000039, 28668)
        assert result is not None, "Returned result cannot be NoneType."
        assert type(result) is list, "Returned type is not list."
        assert len(result) > 0, "Returned list is empty"  # This item will always have market history

        # Invalid type ID
        result = EsiHandler.request_market_region_history(10000039, 11)
        assert result is None, "Returned value is not None for invalid type ID."

        # Invalid region ID
        result = EsiHandler.request_market_region_history(1, 28668)
        assert result is None, "Returned value is not None for invalid region ID."

        # Non-Integer type ID
        result = EsiHandler.request_market_region_history(10000039, "aaaaa")
        assert result is None, "Returned value is not None for non-int type ID."

        # Non-Integer region ID
        result = EsiHandler.request_market_region_history("aaaaa", 28668)
        assert result is None, "Returned value is not None for non-int region ID."

    except AssertionError as error:
        logging.error("One or more tests failed at: EsiHandler.request_market_region_history().")
        logging.error(error)
        return False

    return True


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.info("Running all tests...")

    if (
        # Esi tests
        test_request_market_groups() and
        test_request_type_info() and
        test_request_regions() and
        test_request_region_info() and
        test_request_market_region_history()
    ):
        logging.info("All tests passed.")

    else:
        logging.warn("Some tests failed.")
