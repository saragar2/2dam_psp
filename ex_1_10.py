from multiprocessing import Process, Manager, Value, Lock
import time, random

def retirar(cantidad, lock, saldo, i):
    with lock:
        if (saldo.value < cantidad):
            print(i, ": Saldo insuficiente")
        else:
            time.sleep(1)
            saldo.value = saldo.value - cantidad
            print(i, ": Cantidad retirada. Saldo restante:", saldo.value)
        

def routine(lock, saldo, i):
    while(1):
        retirar(random.randint(5, 30), lock, saldo, i)
        if (saldo.value < 10):
            return

if __name__ == "__main__":
    saldo = Value('i', random.randint(100, 500))
    lock = Lock()

    p1 = Process(routine(lock, saldo, 1))
    p2 = Process(routine(lock, saldo, 2))
    p3 = Process(routine(lock, saldo, 3))
    p4 = Process(routine(lock, saldo, 4))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    
    p1.join()
    p2.join()
    p3.join()
    p4.join()