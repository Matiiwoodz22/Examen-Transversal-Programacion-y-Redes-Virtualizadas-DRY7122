import requests

API_KEY = "4e0d94dc-ded1-4012-a702-b69f88428e03"

def buscar_ciudad(ciudad):
    url = "https://graphhopper.com/api/1/geocode"
    params = {"q": ciudad, "locale": "es", "limit": 1, "key": API_KEY}
    r = requests.get(url, params=params).json()
    if not r.get("hits"):
        return None
    p = r["hits"][0]["point"]
    return p["lat"], p["lng"], r["hits"][0]["name"]

while True:
    origen_txt = input("Ciudad de Origen (o 's' para salir): ")
    if origen_txt.lower() == "s":
        break

    destino_txt = input("Ciudad de Destino: ")
    medio = input("Medio de transporte (car/bike/foot): ").lower()

    origen = buscar_ciudad(origen_txt)
    destino = buscar_ciudad(destino_txt)

    if not origen or not destino:
        print("Ciudad no encontrada")
        continue

    url = "https://graphhopper.com/api/1/route"
    params = {
        "point": [f"{origen[0]},{origen[1]}", f"{destino[0]},{destino[1]}"],
        "vehicle": medio,
        "locale": "es",
        "instructions": "true",
        "key": API_KEY
    }

    ruta = requests.get(url, params=params).json()
    if "paths" not in ruta:
        print("No se pudo calcular la ruta")
        continue

    metros = ruta["paths"][0]["distance"]
    minutos = ruta["paths"][0]["time"] / 1000 / 60

    print(f"Origen: {origen[2]}")
    print(f"Destino: {destino[2]}")
    print(f"Kilómetros: {metros/1000:.2f}")
    print(f"Millas: {(metros/1000)*0.621371:.2f}")
    print(f"Duración: {minutos:.2f} minutos")
    print("Narrativa del viaje:")
    for paso in ruta["paths"][0]["instructions"]:
        print("-", paso["text"])