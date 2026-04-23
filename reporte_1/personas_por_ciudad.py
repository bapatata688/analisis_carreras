import csv

# diccionario con llave id_trabajadores que sera una lista
encuestas = {"id_trabajadores": []}
with open("../dataset_10000_personas.csv", "r", encoding="utf-8") as encuesta:
    id_encuestados = csv.DictReader(encuesta)
    # recorrer la id en el csv y agregarlo al diccionario en id_trabajadores
    for encuestado in id_encuestados:
        id_actual = encuestado["id"]
        encuestas["id_trabajadores"].append(id_actual)
total_identidades = len(encuestas["id_trabajadores"])
print(f"Total de identidades: {total_identidades}")
