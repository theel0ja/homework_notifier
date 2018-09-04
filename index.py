from enum import Enum

# List of subjects
# Subject = Enum("Subjects", "math history literacy")

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


# Find homework that you have to do for tomorrow
homework_for_tomorrow = [];

def build_dict(seq, key):
    return dict((d[key], dict(d, index=index)) for (index, d) in enumerate(seq))

for subject in tomorrow_subjects:
    # https://stackoverflow.com/a/4391722
    homework_number = next((index for (index, d) in enumerate(list_of_homework)
                            if d["subject"] == subject), None)

    if(homework_number != None):
        homework_for_tomorrow.append(list_of_homework[homework_number])

for homework in homework_for_tomorrow:
    print(homework)