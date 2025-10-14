from threading import Thread
import random, time

def correr(id, vueltas):
    for i in range(vueltas):
        tiempo = random.randint(5, 15) / 10
        time.sleep(tiempo)
        print(f"El coche {id} ha terminado la vuelta {i + 1} en {tiempo}")
    print(f"El coche {id} ha terminado la carrera")

if __name__ == "__main__":
    vueltas = int(input("Cuantas vueltas se van a dar? "))
    t1 = Thread(target=correr, args=(1,vueltas))
    t2 = Thread(target=correr, args=(2,vueltas))
    t3 = Thread(target=correr, args=(3,vueltas))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    print("¡La carrera ha terminado!")