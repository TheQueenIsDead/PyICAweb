"""
Handler for all ESI related queries. This file uses EsiPy, a Python Swagger library
that enables interactions between PyICA and the EvE API (ESI). More info here: https://github.com/Kyria/EsiPy
"""

import requests


class EsiHandler(object):

    # TODO Add ESI SSO to perform search on structures

    @staticmethod
    def __perform_request(url):
        """
        Support function that attempts to perform a GET request on a specified URL and returns data
        :param url: URL to perform GET request
        :return:  Data returned by GET request
        """
        with requests.get(url) as response:
            if response:
                data = response.json()
            if response.status_code != 200:  # Status code not OK
                raise Exception(f'REQUEST ERROR: Request to {url} failed with code: {response.status_code}')

        return data

    @staticmethod
    def request_market_groups():
        """
        Requests to get all current market groups in EvE Online
        :return: A list of marketable entity group ID's
        """
        get_market_groups = 'https://esi.evetech.net/latest/markets/groups/?datasource=tranquility'
        try:
            return EsiHandler.__perform_request(get_market_groups)
        except Exception as e:
            # FIXME: Perform proper error handling
            pass

    @staticmethod
    def request_type_info(type_id):
        """
        Requests info about specified type ID from EvE Online
        :param type_id: Valid EvE Online entity ID
        :return: Information on specified type
        """
        get_universe_types_typeid = f'https://esi.evetech.net/latest/universe/types/{type_id}/?datasource=tranquility&language=en-us'
        try:
            return EsiHandler.__perform_request(get_universe_types_typeid)
        except Exception as e:
            # FIXME: Perform proper error handling
            pass

    @staticmethod
    def request_regions():
        """
        Requests to get all current regions in EvE Online
        :return: A list of region ID's
        """
        get_universe_regions = 'https://esi.evetech.net/latest/universe/regions/?datasource=tranquility'
        try:
            return EsiHandler.__perform_request(get_universe_regions)
        except Exception as e:
            # FIXME: Perform proper error handling
            pass

    @staticmethod
    def request_region_info(region_id):
        """
        Requests info about a specified region ID from EvE Online
        :param region_id: Valid EvE Online region ID
        :return: Information on a specified region
        """
        get_universe_regions_regionid = f'https://esi.evetech.net/latest/universe/regions/{region_id}/?datasource=tranquility&language=en-us'
        try:
            return EsiHandler.__perform_request(get_universe_regions_regionid)
        except Exception as e:
            # FIXME: Perform proper error handling
            pass

    @staticmethod
    def request_market_region_history(region_id, type_id):
        """
        Requests all market history for a given type in a specified region
        :param region_id: Valid EvE Online region ID
        :param type_id: Valid EvE online type ID
        :return: Return a list of historical market statistics for the specified type in a region
        """
        get_markets_regionid_history_typeid = f'https://esi.evetech.net/latest/markets/{region_id}/history/?datasource=tranquility&type_id={type_id}'
        try:
            return EsiHandler.__perform_request(get_markets_regionid_history_typeid)
        except Exception as e:
            # FIXME: Perform proper error handling
            pass
