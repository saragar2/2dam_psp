from queue import Queue
from threading import Thread
import random

def producir(cantidad, cola):
    for i in range (cantidad):
        # cola.put(random.randint(1, 10))
        cola.put(i)

def consumir(cantidad, cola):
    for i in range (cantidad):
        print(f"Número recibido: {cola.get()}")
if __name__ == "__main__":
    cantidad = 10
    cola = Queue()
    productor = Thread(target=producir, args=(cantidad, cola,))
    consumidor = Thread(target=consumir, args=(cantidad, cola,))

    productor.start()
    consumidor.start()

    productor.join()
    consumidor.join()
    print("----------fin-----------")