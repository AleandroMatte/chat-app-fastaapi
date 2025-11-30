import logging
from dotenv import load_dotenv
import pytest


@pytest.fixture(scope="session", autouse=True)
def load_environ_vars():
    is_loaded = load_dotenv()
    if not is_loaded:
        logging.info("Unable to load .env file, using server bound variables")
    else:
        logging.info("All variables loaded from dotenv file")
