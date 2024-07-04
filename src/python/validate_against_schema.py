#!python
import json
import sys
from jsonschema import validate, ValidationError, SchemaError


def load_json_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8-sig') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Failed to decode JSON from file '{filepath}': {e}")
        sys.exit(1)


def validate_json(_json_data, _schema):
    try:
        validate(instance=_json_data, schema=_schema)
    except ValidationError as e:
        print(f"Validation Error: {e.message}")
        sys.exit(1)
    except SchemaError as e:
        print(f"Schema Error: {e.message}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python validate_json.py <json_file> <schema_file>")
        sys.exit(1)

    json_file = sys.argv[1]
    schema_file = sys.argv[2]

    json_data = load_json_file(json_file)
    schema = load_json_file(schema_file)

    validate_json(json_data, schema)

    print("JSON file is valid against the schema.")
