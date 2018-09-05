from enum import Enum
import json

class Subject(Enum):
    math = "MATH"
    history = "HISTORY"
    literacy = "LITERACY"

# Subjects you have to do homework for tomorrow
tomorrow_subjects = [Subject.math, Subject.history]

# List of homework
list_of_homework = [
    {"subject": Subject.literacy, "description": "Lorem ipsum dolor sit amet"},
    {"subject": Subject.math, "description": "Lorem ipsum dolor sit amet"}
]

# Generate list of homework from a JSON string.
json_filename = "example_data.json"

with open(json_filename) as f:
    data = json.load(f)

# TODO: Replace subject of a homework with enum one.

print(repr(data))

# Find homework that you have to do for tomorrow
def parser(tomorrow_subjects):
    homework_for_tomorrow = []

    for subject in tomorrow_subjects:
        # https://stackoverflow.com/a/4391722
        homework_number = next((index for (index, d) in enumerate(list_of_homework)
                                if d["subject"] == subject), None)

        if(homework_number != None):
            homework_for_tomorrow.append(list_of_homework[homework_number])

    return homework_for_tomorrow

# Print out homework you have to do for tomorrow
homework_for_tomorrow = parser(tomorrow_subjects)

for homework in homework_for_tomorrow:
    print(homework)