"""Python object to JSON serialization example.

This file shows how to convert a Python object (such as a dictionary)
into a JSON string using Python's built-in json module.

JSON (JavaScript Object Notation) is a common text format used for
storing and exchanging data between systems.
"""

import json


def main():
    """Create a Python dictionary, convert it to JSON, and save it to a file."""

    # A Python dictionary is a collection of key-value pairs.
    # In this example, the dictionary represents one student.
    student = {
        "name": "Aarav",
        "age": 20,
        "courses": ["Python", "Math", "Data Science"],
        "is_active": True,
        "grade": None,
    }

    # json.dumps() converts a Python object into a JSON string.
    # The indent=4 argument makes the JSON output easy to read.
    json_string = json.dumps(student, indent=4)

    # Print the JSON string so we can see the result.
    print("Serialized JSON string:")
    print(json_string)

    # Optional: Save the JSON string to a file called student.json.
    # This is useful if we want to keep the serialized data for later.
    with open("student.json", "w", encoding="utf-8") as file:
        file.write(json_string)

    print("\nThe JSON data has been saved to student.json")


if __name__ == "__main__":
    main()
