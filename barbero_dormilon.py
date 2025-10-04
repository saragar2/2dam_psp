import random, time
from multiprocessing import Process, Semaphore, Lock, Value

def atender(id, clientes_sem, mutex, atendidos, total_clientes):
    while (True):
        clientes_sem.acquire() #Simulando que el barbero está esperando clientes
        with mutex:
            if (atendidos.value >= total_clientes.value):
                break
            print(f"\033[;33mEl barbero {id} está atendiendo a un cliente\033[0;m")
        time.sleep(random.randint(1, 3)) #Simulando el tiempo que tarda en cortar el pelo
        with mutex:
            atendidos.value += 1
            print(f"\033[;32mEl barbero {id} ha terminado un corte, y procede a dormir.\033[0;m")


def ser_atendido(id, barberos_sem, clientes_sem, sillas_sem, mutex, rechazados):
    time.sleep(random.randint(1, 10)) #Simulando el tiempo que tarda en llegar el cliente
    with mutex:
        print(f"\033[;36mEl cliente {id} ha llegado a la barbería\033[0;m")
    if (not sillas_sem.acquire(block=False)): #Si no hay sillas, teniendo en cuenta que el semáforo tiene desactivada la cola, el cliente se va
        with mutex:
            rechazados.value += 1
            print(f"\033[;31mEl cliente {id} se va porque no hay sillas disponibles\033[0;m")
        return
    with mutex:
        print(f"\033[;34mEl cliente {id} está esperando a ser atendido\033[0;m")
    barberos_sem.acquire() 	#El cliente espera a que un barbero esté libre
    sillas_sem.release() 	#El cliente se levanta de la silla de espera
    clientes_sem.release() 	#El cliente avisa a un barbero de que está listo para ser atendido
    with mutex:
        print(f"\033[;35mAl cliente {id} le están cortando el pelo\033[0;m")
    time.sleep(random.randint(1, 3)) #Simulando el tiempo que tarda en ser atendido
    barberos_sem.release() #El cliente libera al barbero
    with mutex:
        print(f"\033[;30mEl cliente {id} se va de la barbería\033[0;m")


if __name__ == "__main__":
    n_barberos = int(input("Cuántos barberos hay?: "))
    n_clientes = int(input("Cuántos clientes hay?: "))
    n_sillas = int(input("Cuántas sillas de espera hay?: "))

    barberos_sem = Semaphore(n_barberos)  # Controla cuántos barberos atienden a la vez
    clientes_sem = Semaphore(0)           # Clientes esperando a ser atendidos
    sillas_sem = Semaphore(n_sillas)      # Sillas de espera
    mutex = Lock()                        # Exclusión mutua para mensajes

    atendidos = Value('i', 0)
    rechazados = Value('i', 0)
    total_clientes = Value('i', n_clientes)

    barberos = []
    for i in range(n_barberos):
        b = Process(target=atender, args=(i+1, clientes_sem, mutex, atendidos, total_clientes))
        b.daemon = True
        b.start()
        barberos.append(b)

    clientes = []
    for i in range(n_clientes):
        c = Process(target=ser_atendido, args=(i+1, barberos_sem, clientes_sem, sillas_sem, mutex, rechazados))
        clientes.append(c)
        c.start()

    for c in clientes:
        c.join()

    with mutex:
        print("\n\033[;36m--- Jornada terminada en la barbería ---\033[0;m")
        print(f"Clientes atendidos: {atendidos.value}")
        print(f"Clientes que se fueron sin ser atendidos: {rechazados.value}")
        print("-----------------------------------------")
