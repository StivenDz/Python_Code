DATA = [
    {
        "name": "Facundo",
        "age": 72,
        "organization": "Platzi",
        "Position": "Technical coach",
        "language": "Python"
    },
    {
        "name": "Luisana",
        "age": 32,
        "organization": "Globant",
        "Position": "UX Designer",
        "language": "javascript"
    },
    {
        "name": "Hector",
        "age": 19,
        "organization": "Globant",
        "Position": "Associate",
        "language": "ruby"
    },
    {
        "name": "Gabriel",
        "age": 20,
        "organization": "Platzi",
        "Position": "Associate",
        "language": "javascript"
    },
    {
        "name": "Isabella",
        "age": 30,
        "organization": "Platzi",
        "Position": "QA Manager",
        "language": "java"
    },
    {
        "name": "Karo",
        "age": 23,
        "organization": "Everis",
        "Position": "Backend Developer",
        "language": "Python"
    },
    {
        "name": "Ariel",
        "age": 32,
        "organization": "Rappi",
        "Position": "Support",
        "language": ""
    },
    {
        "name": "Juan",
        "age": 17,
        "organization": "",
        "Position": "Student",
        "language": "go"
    },
    {
        "name": "Pablo",
        "age": 32,
        "organization": "Master",
        "Position": "Human Resources Manager",
        "language": "Python"
    },
    {
        "name": "Lorena",
        "age": 56,
        "organization": "Python organization",
        "Position": "Language Marker",
        "language": "Python"
    }
]


def run():
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "Python"]
    all_Platzi_workers = [worker["name"]for worker in DATA if worker["organization"] == "Platzi"]
    adults = list(filter(lambda worker: worker ["age"] > 18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))
    old_people = list(map(lambda worker: worker | {"old":worker["age"]>70}, DATA))


    for worker in old_people:
        print(worker)

# TAREA TRANFORMAR LAS HOF EN LIST COMP Y LAS LIST COMOP EN HOF

if __name__ == "__main__":
    run()