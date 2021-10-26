import logging


class Verify:
    @staticmethod
    def equals(expected, actual, message_on_fail):
        """Method to check that actual information equals to expected information"""
        try:
            assert expected == actual, message_on_fail
        except AssertionError as err:
            err_type = err.__class__.__name__
            logging.error(f"{err_type}: {message_on_fail}")
            logging.debug(f"{expected} should be equal to {actual}")
            raise err

    @staticmethod
    def true(condition, message_on_fail):
        """Method to check that condition return True statement"""
        try:
            assert condition, message_on_fail
        except AssertionError as err:
            err_type = err.__class__.__name__
            logging.error(f"{err_type}: {message_on_fail}")
            logging.debug(f"{condition} is true")
            raise err

    @staticmethod
    def false(condition, message_on_fail):
        """Method to check that condition return False statement"""
        try:
            assert not condition, message_on_fail
        except AssertionError as err:
            err_type = err.__class__.__name__
            logging.error(f"{err_type}: {message_on_fail}")
            logging.debug(f"{condition} is false")
            raise err

    @staticmethod
    def contains(expected, actual, message_on_fail):
        """Method to check that actual information contains expected information"""
        try:
            assert expected in actual, message_on_fail
        except AssertionError as err:
            err_type = err.__class__.__name__
            logging.error(f"{err_type}: {message_on_fail}")
            logging.debug(f"{expected} value contains {actual}")
            raise err
