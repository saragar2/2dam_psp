from multiprocessing import Process, Semaphore
import time
import random

def usar_recurso(sem, i):
    sem.acquire() # Se intenta acceder. Si no se puede, espera
    try:
        print(f"Proceso {i} usando el recurso")
        time.sleep(random.uniform(0.5, 2)) # Espera tantos segundos como un número decimal aleatorio entre 0.5 y 2
        print(f"Proceso {i} liberando el recurso")
    finally:
        sem.release() # Libera su sitio en el semáforo
if __name__ == "__main__":
    sem = Semaphore(2) # Máximo 2 procesos a la vez
    procesos = []
    for i in range(5):
        p = Process(target=usar_recurso, args=(sem, i))
        procesos.append(p)
        p.start()
    for p in procesos:
        p.join()