from enum import Enum
import json

class Subject(Enum):
    math = "MATH"
    history = "HISTORY"
    literacy = "LITERACY"


def get_tomorrow_subjects():
    # Subjects you have to do homework for tomorrow
    tomorrow_subjects = []  # [Subject.math, Subject.history]

    # Load tomorrow_subjects.json
    with open("tomorrow_subjects.json") as f:
        tomorrow_subjects_json = json.load(f)

    for subject in tomorrow_subjects_json:
        tomorrow_subjects.append(Subject[subject.lower()])

    return tomorrow_subjects

def get_homework():
    # List of homework
    #
    # list_of_homework = [
    #     {"subject": Subject.literacy, "description": "Lorem ipsum dolor sit amet"},
    #     {"subject": Subject.math, "description": "Lorem ipsum dolor sit amet"}
    # ]

    # Generate list of homework from a JSON string.
    json_filename = "example_data.json"


    with open(json_filename) as f:
        list_of_homework = json.load(f)

    return list_of_homework

# Find homework that you have to do for tomorrow
def get_homework_for_tomorrow(tomorrow_subjects, list_of_homework):
    homework_for_tomorrow = []

    for subject in tomorrow_subjects:
        # https://stackoverflow.com/a/4391722
        homework_number = next((index for (index, d) in enumerate(list_of_homework)
                                if d["subject"] == subject.value), None)

        if(homework_number != None):
            homework_for_tomorrow.append(list_of_homework[homework_number])

    return homework_for_tomorrow

# CLI FOR DEVELOPMENT
if __name__ == '__main__':
    # Print out homework you have to do for tomorrow
    homework_for_tomorrow = get_homework_for_tomorrow(
        get_tomorrow_subjects(),
        get_homework()
    )

    for homework in homework_for_tomorrow:
        print(homework)