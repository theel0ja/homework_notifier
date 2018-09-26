from flask import Flask, jsonify

from index import Subject, get_tomorrow_subjects, get_homework, get_homework_for_tomorrow


app = Flask(__name__)


@app.route("/api/subjects")
def get_subjects():
    data = []

    for subject in Subject:
        data.append(subject.value)

    return jsonify(data)

@app.route("/api/subjects/for_tomorrow")
def api_get_tomorrow_subjects():
    data = []

    for subject in get_tomorrow_subjects():
        data.append(subject.value)

    return jsonify(data)

@app.route("/api/homework")
def api_get_homework():
    return jsonify(get_homework())

@app.route("/api/homework/for_tomorrow")
def api_get_homework_for_tomorrow():
    return jsonify(get_homework_for_tomorrow())