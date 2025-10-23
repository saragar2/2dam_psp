from threading import Thread, Semaphore
import time

def routine(tenedor_izq, tenedor_der, id):
    while (True): #Se ejecutará sin fin
        tenedor_izq.acquire()
        print(f"{id}---- Ha cogido el tenedor izquierdo")
        tenedor_der.acquire()
        print(f"{id}---- Ha cogido el tenedor derecho")
        print(f"{id}---- Está comiendo") #para haber llegado hasta aquí, tiene que tener agarrados ambos tenedores 
        time.sleep(5) #Simulamos que el filósofo está comiendo
        print(f"{id}---- Ha terminado de comer y procede a pensar")
        tenedor_izq.release()
        tenedor_der.release()
        time.sleep(0.1) #Con esto hacemos que el resto de filósofos tengan tiempo de agarrar los tenedores, así no come siempre el mismo

if __name__ == "__main__":
    n_filos = int(input("Cuántos filósofos participarán? "))
    filos_list = []
    tenedor_list = []

    for _ in range(n_filos): #Creamos la lista de tenedores
        t = Semaphore(1)
        tenedor_list.append(t)

    for i in range(n_filos):
        if ((i + 1) == n_filos):
            f = Thread(target=routine, args=(tenedor_list[i], tenedor_list[0], i + 1,)) #En caso de que el filósofo sea el último, su tenedor derecho será
                                                                                        #el izquierdo del primer filósofo, es decir, el primer tenedor
        else:
            f = Thread(target=routine, args=(tenedor_list[i], tenedor_list[i + 1], i + 1,))
        filos_list.append(f)
        f.start()

#No hay join porque el programa nunca termina (hasta que el usuario lo pare)