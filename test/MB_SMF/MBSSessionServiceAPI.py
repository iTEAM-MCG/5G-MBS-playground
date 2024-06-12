import unittest
import httpcore

from utils.config import config_from_file
from utils.logger import setup_logger
from utils.json_schema import json_validate
from utils.http2_prior_knowledge import setup_http2_pool

global config, logger
config = config_from_file("config.toml")
logger = setup_logger(__name__, config["DEFAULT"]["log_level"])
http2 = setup_http2_pool()

class MBSSessionCreateServiceOperation(unittest.TestCase):

    def test_create_mbs_session(self):
        path = "/post"

        # avoid the ugly output when tests are run in verbose mode
        print("\n")

        logger.info("test_create_mbs_session")

        url = "https://www.google.es"
        response = http2.request("GET", url)

        self.assertEqual(response.status, 200)
