import config
import pytest

from helpers.assert_response import ALL_USERS_RESPONSE, CREATE_USER, SINGLE_USER, UPDATED_USER
from helpers.logging import logger
from helpers.reqres_api_methods import get, post, put
from helpers.verify import Verify


@pytest.mark.debug
def test_get_all_users():

    response = get(url=config.list_users_url)
    json_resp = response.json()
    total = json_resp["total"]
    data = json_resp["data"]

    logger.info("Verify that status code for GET all users returns 200")
    Verify.equals(200, response.status_code, "Status code does not equal to 200")

    logger.info(f"Verify that 'total' from payload equals to 12")
    Verify.equals(12, total, "Number of users does not equals to 12")

    logger.info(f"Verify that response '{ALL_USERS_RESPONSE}' corresponds to received '{data}'")
    Verify.equals(ALL_USERS_RESPONSE, data, f"Data does not correspond to '{ALL_USERS_RESPONSE}'")


@pytest.mark.debug
def test_create_user():
    """ Create a new user"""
    query = {
        "name": "morpheus",
        "job": "leader",
        "id": '211'
    }
    response = post(url=config.create_user_url, json=query)

    logger.info("Verify that status code after creating user returns 201")
    Verify.equals(201, response.status_code, "Status code does not equal to 201")

    logger.info(f"Verify that response '{CREATE_USER}' corresponds to received '{query}'")
    Verify.equals(CREATE_USER, query, f"Data does not correspond to '{CREATE_USER}'")


@pytest.mark.debug
def test_get_single_user():
    """Get a single user"""

    response = get(url=config.single_user_url)
    json_resp = response.json()

    logger.info("Verify that status code for GET all users returns 200")
    Verify.equals(200, response.status_code, "Status code does not equal to 200")

    logger.info(f"Verify that response '{SINGLE_USER}' corresponds to received '{json_resp}'")
    Verify.equals(SINGLE_USER, json_resp, f"Data does not correspond to '{SINGLE_USER}'")


@pytest.mark.debug
def test_update_user():
    """ Update existed user via PUT method"""
    query = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = put(url=config.single_user_url, json=query)

    logger.info("Verify that status code after updating user returns 200")
    Verify.equals(200, response.status_code, "Status code does not equal to 200")

    logger.info(f"Verify that response '{UPDATED_USER}' corresponds to received '{query}'")
    Verify.equals(UPDATED_USER, query, f"Data does not correspond to '{UPDATED_USER}'")


@pytest.mark.debug
def test_logged_in_user():
    """Use is logged in via POST method"""

    query = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    exp_token = {"token": "QpwL5tke4Pnpja7X4"}

    response = post(url=config.logged_in_url, json=query)

    logger.info("Verify that status code after logging user returns 200")
    Verify.equals(200, response.status_code, "Status code does not equal to 200")

    logger.info(f"Verify that user is logged in successfully and '{response.json()}' equals to token '{exp_token}'")
    Verify.equals(exp_token, response.json(), "User is not logged in successfully")



