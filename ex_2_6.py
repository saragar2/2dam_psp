from queue import Queue
from threading import Thread
import random, time

def producir(cantidad, cola):
    for i in range (cantidad):
        print(f"Produciendo el número {i}")
        time.sleep(random.randint(1, 3)) #para añadir realismo, se tarda en producir
        cola.put(i)

def consumir(cantidad, cola):
    for i in range (cantidad):
        time.sleep(2) #también se tarda en recibir
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