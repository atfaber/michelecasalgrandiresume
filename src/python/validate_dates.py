import json
import sys
from datetime import datetime


def validate_dates(_resume):
    date_format = "%b %Y"

    for job in _resume['experience']:
        try:
            from_date = datetime.strptime(job['from'], date_format)

            if job['to'].strip().lower() == 'present':
                to_date = datetime.strptime("Dec 2999", date_format)
            else:
                to_date = datetime.strptime(job['to'], date_format)
        except KeyError as e:
            print(f"Error: Missing key in JSON data: {e}")
            sys.exit(1)
        except ValueError as e:
            print(f"Error: Incorrect date format: {e}")
            sys.exit(1)

        error = None
        if to_date < from_date:
            error = "after"
        elif to_date == from_date:
            error = "the same as"

        if error is not None:
            raise ValueError(f"Error: 'to' date {job['to']} is {error} 'from' date {job['from']}.")

        print(f"'from' {job['from']} is before 'to' {job['to']} - Validation successful.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_dates.py <json_file>")
        sys.exit(1)

    json_file = sys.argv[1]

    try:
        with open(json_file, 'r') as file:
            json_data = json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{json_file}' was not found.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Failed to decode JSON from file '{json_file}': {e}")
        sys.exit(1)

    validate_dates(json_data)
