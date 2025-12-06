import json

try:
    with open("usuarios.json", "r", encoding="utf-8") as archivo:
        usuarios = json.load(archivo)

    peruanos = [u for u in usuarios if u["pais"] == "Perú"]

    with open("peruanos.json", "w", encoding="utf-8") as salida:
        json.dump(peruanos, salida, ensure_ascii=False, indent=4)

    print(f"Cantidad de usuarios peruanos: {len(peruanos)}")

except FileNotFoundError:
    print("Error: El archivo usuarios.json no existe.")
