"""JSON string to Python object deserialization example.

This file shows how to convert a JSON string back into a Python object
using the Python built-in json module.

The process of converting JSON data into a Python object is called
JSON deserialization.
"""

import json


def main():
    """Read a JSON string, convert it to a Python dictionary, and print values."""

    # A JSON string is text data that looks like a Python dictionary.
    # Notice that JSON uses double quotes for strings and true/false/null.
    json_string = '''
    {
        "name": "Aarav",
        "age": 20,
        "courses": ["Python", "Math", "Data Science"],
        "is_active": true,
        "grade": null
    }
    '''

    # json.loads() means "load string".
    # It receives a JSON string and returns a Python dictionary.
    student_object = json.loads(json_string)

    # The object returned is a Python dictionary.
    print("Deserialized Python object:")
    print(student_object)

    # Access the values of the dictionary using keys.
    print("\nStudent profile:")
    print("Name:", student_object["name"])
    print("Age:", student_object["age"])
    print("Courses:", ", ".join(student_object["courses"]))

    # Tell the user the type of the deserialized object.
    print("\nType of the returned object:", type(student_object))


if __name__ == "__main__":
    main()
