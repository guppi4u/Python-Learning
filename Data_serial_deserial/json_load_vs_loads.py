"""Compare json.load() and json.loads() in Python.

json.loads() reads a JSON string and converts it into a Python object.
json.load() reads a JSON file and converts the file contents into a Python object.

This file shows the difference with a beginner-friendly example.
"""

import json


def explain_loads_and_load():
    """Show how loads parse a string and load parse a file."""

    # A JSON string stored inside Python as text.
    json_string = '{"name": "Aarav", "age": 20, "courses": ["Python", "Math"]}'

    # json.loads() receives a JSON string and returns a Python dictionary.
    # It works with a string value, not a file.
    python_object_from_string = json.loads(json_string)

    print("Using json.loads():")
    print(python_object_from_string)
    print("Type:", type(python_object_from_string))

    # To demonstrate json.load(), we first create a file with JSON data.
    with open("student_load.json", "w", encoding="utf-8") as file:
        file.write('{"name": "Aarav", "age": 20, "courses": ["Python", "Math"]}')

    # json.load() receives a file object and reads the JSON data from that file.
    with open("student_load.json", "r", encoding="utf-8") as file:
        python_object_from_file = json.load(file)

    print("\nUsing json.load():")
    print(python_object_from_file)
    print("Type:", type(python_object_from_file))


if __name__ == "__main__":
    explain_loads_and_load()
