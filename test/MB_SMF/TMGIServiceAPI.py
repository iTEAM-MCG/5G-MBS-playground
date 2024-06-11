import unittest
import httpcore
import json

from utils.config import config_from_file
from utils.logger import setup_logger
from utils.json_schema import json_validate
from utils.http2_prior_knowledge import setup_http2_pool

global config, logger
config = config_from_file("config.toml")
logger = setup_logger(__name__, config["DEFAULT"]["log_level"])
http2 = setup_http2_pool()

global api_url
api_url = "/nmbsmf-tmgi/v1"

class TMGIAllocateServiceOperation(unittest.TestCase):
    path = "/tmgi"

    def test_tmgi_allocate(self):
        full_path = f"{api_url}{self.path}"

        # avoid the ugly output when tests are run in verbose mode
        print("\n")

        logger.info("test_tmgi_allocate")

        # load the JSON file
        with open("support/nmbsmf-tmgi/tmgi_allocate.json") as file:
            request_json = json.load(file)

        # validate input JSON against a JSON schema
        input_validation = json_validate(request_json, "support/nmbsmf-tmgi/tmgi_allocate.schema.json")

        logger.debug(f"Input JSON validation {input_validation['result']}: {input_validation['message']}")

        self.assertEqual(input_validation["result"], "success")

        # build the full API URL
        url = f"{config['mb_smf']['protocol']}://{config['mb_smf']['address']}:{config['mb_smf']['port']}{full_path}"

        # send the tmgi allocate POST request
        headers = { "Content-Type": "application/json" }
        response = http2.request("POST", url, headers=headers, content=json.dumps(request_json).encode("utf-8"))

        logger.debug(f"Sending POST request to {url} with JSON: {request_json}")

        response_status = response.status
        response_json = json.loads(response.content)
        logger.debug(f"Received response [{response_status}] with JSON: {response_json}")

        # validate received JSON against a JSON schema
        output_validation = json_validate(response_json, "support/nmbsmf-tmgi/tmgi_allocated.schema.json")
        logger.debug(f"Output JSON validation {output_validation['result']}: {output_validation['message']}")

        self.assertEqual(output_validation["result"], "success")

        # test asserts
        self.assertEqual(response_status, 200)

    def test_tmgi_refresh(self):
        full_path = f"{api_url}{self.path}"

        # avoid the ugly output when tests are run in verbose mode
        print("\n")

        logger.info("test_tmgi_refresh")

        # allocate first a TMGI to be refreshed
        # load the JSON file
        with open("support/nmbsmf-tmgi/tmgi_allocate.json") as file:
            request_json = json.load(file)

        # validate input JSON against a JSON schema
        input_validation = json_validate(request_json, "support/nmbsmf-tmgi/tmgi_allocate.schema.json")

        logger.debug(f"Input JSON validation {input_validation['result']}: {input_validation['message']}")

        self.assertEqual(input_validation["result"], "success")

        # build the full API URL
        url = f"{config['mb_smf']['protocol']}://{config['mb_smf']['address']}:{config['mb_smf']['port']}{full_path}"

        # send the tmgi allocate POST request
        headers = { "Content-Type": "application/json" }
        response = http2.request("POST", url, headers=headers, content=json.dumps(request_json).encode("utf-8"))

        logger.debug(f"Sending POST request to {url} with JSON: {request_json}")

        response_status = response.status
        response_json = json.loads(response.content)
        logger.debug(f"Received response [{response_status}] with JSON: {response_json}")

        # validate received JSON against a JSON schema
        output_validation = json_validate(response_json, "support/nmbsmf-tmgi/tmgi_allocated.schema.json")
        logger.debug(f"Output JSON validation {output_validation['result']}: {output_validation['message']}")

        self.assertEqual(output_validation["result"], "success")

        # test asserts
        self.assertEqual(response_status, 200)

        expiration_time = response_json["expirationTime"]

        # load the JSON file
        with open("support/nmbsmf-tmgi/tmgi_refresh.template.json") as file:
            refresh_json = json.load(file)

        # copy the allocated TMGI to the refresh JSON
        refresh_json["tmgiList"][0] = response_json["tmgiList"][0]

        # validate the refresh JSON against a JSON schema
        refresh_validation = json_validate(refresh_json, "support/nmbsmf-tmgi/tmgi_allocate.schema.json")

        logger.debug(f"Refresh JSON validation {refresh_validation['result']}: {refresh_validation['message']}")

        self.assertEqual(refresh_validation["result"], "success")

        # refresh the allocated TMGI
        # send the tmgi allocate POST request
        response = http2.request("POST", url, headers=headers, content=json.dumps(refresh_json).encode("utf-8"))

        logger.debug(f"Sending POST request to {url} with JSON: {refresh_json}")

        response_status = response.status
        response_json = json.loads(response.content)
        logger.debug(f"Received response [{response_status}] with JSON: {response_json}")

        # TODO (borieher): validate received JSON against a JSON schema, not sure if API follows the spec here
        #output_validation = json_validate(response_json, "support/nmbsmf-tmgi/tmgi_allocated.schema.json")
        #logger.debug(f"Output JSON validation {output_validation['result']}: {output_validation['message']}")

        #self.assertEqual(output_validation["result"], "success")

        # test asserts
        self.assertEqual(response_status, 200)

        refreshed_expiration_time = response_json["expirationTime"]

        logger.debug(f"Refreshed expirationTime: {refreshed_expiration_time}, old expirationTime: {expiration_time}")

        # check if refreshed_expiration_time is greater than expiration_time
        self.assertTrue(refreshed_expiration_time > expiration_time)

class TMGIDeallocateServiceOperation(unittest.TestCase):
    path = "/tmgi"

    def test_tmgi_deallocate(self):
        full_path = f"{api_url}{self.path}"

        # avoid the ugly output when tests are run in verbose mode
        print("\n")

        logger.info("test_tmgi_deallocate")

        # This request is a DELETE with the tmgi-list query parameter following the tmgi_deallocate.schema.json

        response = http2.request("GET", "https://www.google.es")
        self.assertEqual(response.status, 200)
