import time
import random
import asyncio
import threading
import multiprocessing

# Simular una descarga
def descargar(url):
    tiempo = random.uniform(0.5, 2) 
    time.sleep(tiempo)
    return f"OK: {url}"

# Versión async
async def descargar_async(url):
    tiempo = random.uniform(0.5, 2)
    await asyncio.sleep(tiempo)
    return f"OK: {url}"

# Lista de URLs
urls = [f"https://api.fake.com/recurso/{i}" for i in range(50)]


# 1) Modo secuencial (normal)
def modo_secuencial():
    resultados = []
    for url in urls:
        resultados.append(descargar(url))
    return resultados


# 2) Multihilo
def modo_hilos():
    resultados = []
    hilos = []

    def tarea(url):
        resultados.append(descargar(url))

    for url in urls:
        t = threading.Thread(target=tarea, args=(url,))
        hilos.append(t)
        t.start()

    for t in hilos:
        t.join()

    return resultados


# 3) Asincronía con asyncio
async def modo_asyncio():
    tareas = [descargar_async(url) for url in urls]
    resultados = await asyncio.gather(*tareas)
    return resultados


# 4) Multiproceso
def modo_multiproceso():
    with multiprocessing.Pool() as pool:
        resultados = pool.map(descargar, urls)
    return resultados


# MEDIR TIEMPOS
def medir(nombre, funcion):
    inicio = time.time()
    if nombre == "asyncio":
        resultados = asyncio.run(funcion())
    else:
        resultados = funcion()
    fin = time.time()
    return fin - inicio


# MAIN
if __name__ == "__main__":
    tiempos = {}

    tiempos["secuencial"] = medir("secuencial", modo_secuencial)
    tiempos["hilos"] = medir("hilos", modo_hilos)
    tiempos["asyncio"] = medir("asyncio", modo_asyncio)
    tiempos["multiproceso"] = medir("multiproceso", modo_multiproceso)

    print("\nRESULTADOS")
    for k, v in tiempos.items():
        print(f"{k}: {v:.2f} segundos")

    # Comparar
    mas_rapido = min(tiempos, key=tiempos.get)
    mas_lento = max(tiempos, key=tiempos.get)

    print("\nCOMPARACIÓN")
    print(f"Más rápido  → {mas_rapido}")
    print(f"Más lento   → {mas_lento}")

    print("\nEXPLICACIÓN")
    print("""
• asyncio suele ser más rápido cuando hay muchas esperas, ya que no bloquea el programa.
• threading también es rápido porque mientras un hilo espera, otro trabaja.
• multiprocessing es útil para tareas pesadas de CPU, pero aquí es más lento porque crear procesos toma tiempo.
• secuencial es el que se demora más porque hace todo uno por uno.
""")
