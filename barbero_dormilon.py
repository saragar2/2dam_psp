#el barbero es un daemon
from multiprocessing import Process, Semaphore
import random, time

def atender():

    
def ser_atendido():
    sillas.acquire()
    time.sleep(random.randint(3))
    sillas.release()

if __name__ == "__main__":
    n_barberos = input("Cuántos barberos hay?: ")
    n_clientes = input("Cuántos clientes hay?: ")
    n_sillas = input("Cuántas sillas de espera hay?: ")

    barberos = []
    clientes = []
    sillas = Semaphore(n_sillas)

    for i in range(n_barberos):
        b = Process(target=atender, args=)
        b.daemon = True
        barberos.append(b)
    for i in range(n_clientes):
        c = Process(target=ser_atendido, args=)
        clientes.append(c)

    for i in range(n_barberos):
        barberos[i].start
    for i in range(n_clientes):
        time.sleep(random.randint(10))
        clientes[i].start