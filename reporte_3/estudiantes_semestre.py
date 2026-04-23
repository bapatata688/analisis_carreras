import csv

encuestas = {"carreras": []}
with open("../dataset_10000_personas.csv", "r", encoding="utf-8") as encuestas:
    encuesta = csv.DictReader(encuestas)
    for columna in encuesta:
        semestre = columna["semestre"]
        print(semestre)
        if semestre not in encuestas["carreras"]:
            encuestas["carreras"].append(semestre)
