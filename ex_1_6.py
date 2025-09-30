from multiprocessing import Process, Queue
import time

# ----------1----------

def productor(q):
    for i in range(5):
        print(f"Productor pone: {i}")
        q.put(i)

def consumidor(q):
    for i in range(5):
        dest = q.get()
        print(f"Consumidor recibe: {dest}")

if __name__ == "__main__":
    cola = Queue()
    p1 = Process(target=productor, args=(cola,))
    p2 = Process(target=consumidor, args=(cola,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()