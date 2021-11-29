import json


students = {
    "name": "Brad",
    "surname": "Hoover",
    "DOB": 2001,
    "Uni": "Berkley",
    "country": "USA",
    "hometown": "Warsaw",
    "state": "Ohio",
    "major": "IT"
}


json_object = json.dumps(students, indent=5)

with open("student.json", "w") as outfile:
    outfile.write(json_object)