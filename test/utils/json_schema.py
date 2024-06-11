import json
from jsonschema import validate
import jsonschema

def json_validate(json_data, json_schema_path):
    # JSON data is received but JSON schema is a file read from path
    with open(json_schema_path) as json_schema:
        schema = json.load(json_schema)

    try:
        validate(instance=json_data, schema=schema)
    except jsonschema.exceptions.ValidationError as error:
        # JSON is not valid
        return { "result": "error", "message": error.message }
    # JSON is valid
    return { "result": "success", "message": "JSON is valid" }
