import requests
import logging


def get(url):
    """Return GET request"""
    logging.debug("Return GET request")
    return requests.get(url)


def post(url, json):
    """Return POST request"""
    logging.debug(f"Return Post request with '{json}'")
    return requests.post(url, json=json)


def put(url, json, **headers):
    """Return PUT request"""
    logging.debug("Return Put request")
    return requests.put(url, json=json, headers=headers)


def delete(url, **headers):
    """Return DELETE request"""
    logging.debug("Return Delete request")
    return requests.delete(url, headers=headers)

