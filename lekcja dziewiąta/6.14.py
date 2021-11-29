import json


movies = {
    "name": "2 fast 2 furious",
    "genre": "action",
    "year": 2002,
    "company": "Universal",
    "country": "USA"
}


json_object = json.dump(movies, indent=5)

with open("movies.json", "w") as outfile:
    outfile.write(json_object)