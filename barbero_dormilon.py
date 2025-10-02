#el barbero es un daemon
import random, time
from multiprocessing import Process, Semaphore

# def atender():

    
def ser_atendido(id: int, barberos_sem, sillas_sem):
    time.sleep(random.randint(1, 10))
    print("\033[;36m" + f"El cliente {id} ha llegado a la barbería")
    sillas_sem.acquire()
    try:
        print("\033[;26m" + f"El cliente {id} está esperando a ser atendido")
    finally:
        sillas_sem.release()
    barberos_sem.acquire()
    try:
        print("\033[;46m" + f"Al cliente {id} le están cortando el pelo" + '\033[0;m')
        time.sleep(random.randint(1, 3))
    finally:
        barberos_sem.release()
    print("\033[;30m" + f"El cliente {id} se va de la barbería" +'\033[0;m')

if __name__ == "__main__":
    n_barberos = int(input("Cuántos barberos hay?: "))
    n_clientes = int(input("Cuántos clientes hay?: "))
    n_sillas = int(input("Cuántas sillas de espera hay?: "))

    barberos = []
    clientes = []
    barberos_sem = Semaphore(n_barberos)
    sillas_sem = Semaphore(n_sillas)

    # for i in range(n_barberos):
    #     b = Process(target=atender, args= i + 1)
    #     b.daemon = True
    #     b.start()
    #     barberos.append(b)

    for i in range(n_clientes):
        c = Process(target=ser_atendido, args=(i + 1, barberos_sem, sillas_sem))
        clientes.append(c)
        c.start()

    for i in range(n_clientes):
        clientes[i].join()