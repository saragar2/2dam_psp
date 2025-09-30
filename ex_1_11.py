import time, random
from multiprocessing import Process, Semaphore, Lock, Value

BUFFER_SIZE = 3  # número de sitios en la bandeja

def productor(bandeja, mutex, espacios_libres, pasteles_listos):
    while True:
        time.sleep(random.randint(1, 3))   # simula hacer un pastel
        espacios_libres.acquire()          # espera que haya sitio libre
        with mutex:                        # sección crítica
            bandeja.value += 1
            print(f"Productor: puso pastel ({bandeja.value}/{BUFFER_SIZE})")
        pasteles_listos.release()          # indica que hay pastel listo

def consumidor(bandeja, mutex, espacios_libres, pasteles_listos):
    while True:
        pasteles_listos.acquire()          # espera a que haya pastel
        time.sleep(random.randint(1, 2))   # simula comérselo
        with mutex:                        # sección crítica
            bandeja.value -= 1
            print(f"Consumidor: se comió un pastel ({bandeja.value}/{BUFFER_SIZE})")
        espacios_libres.release()          # libera espacio en la bandeja

if __name__ == "__main__":
    bandeja = Value('i', 0)
    mutex = Lock()
    espacios_libres = Semaphore(BUFFER_SIZE)
    pasteles_listos = Semaphore(0)

    p = Process(target=productor, args=(bandeja, mutex, espacios_libres, pasteles_listos))
    c = Process(target=consumidor, args=(bandeja, mutex, espacios_libres, pasteles_listos))

    p.start()
    c.start()

    # Aquí no hacemos join() porque nunca van a terminar
    p.join()
    c.join()