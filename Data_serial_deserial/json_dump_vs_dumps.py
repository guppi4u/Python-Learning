"""Compare json.dump() and json.dumps() in Python.

json.dumps() converts a Python object into a JSON string.
json.dump() writes that JSON text directly into a file.

This file shows the difference with a beginner-friendly example.
"""

import json


def explain_dumps_and_dump():
    """Show how dumps creates a JSON string and dump writes it to a file."""

    # A Python dictionary object that we want to convert into JSON.
    student = {
        "name": "Aarav",
        "age": 20,
        "courses": ["Python", "Math"],
        "is_active": True,
    }

    # json.dumps() converts the Python object into a JSON string.
    # It returns the JSON text as a string and keeps it in memory.
    json_string = json.dumps(student, indent=4)

    print("Using json.dumps():")
    print(json_string)
    print("\nThe returned value from json.dumps() is a string.")

    # json.dump() writes the JSON data directly to a file.
    # It needs a file object opened for writing.
    with open("student_dump.json", "w", encoding="utf-8") as file:
        json.dump(student, file, indent=4)

    print("\nUsing json.dump():")
    print("The JSON data has been written to student_dump.json")


if __name__ == "__main__":
    explain_dumps_and_dump()
