from threading import Thread, Semaphore, Lock
import time, random

def rojos(refugios, mutex, puntos_rojo, puntos_azul, id, refugiados_rojo): #Los comentarios de los azules son válidos también para los rojos
    time.sleep(random.randint(0,2))
    print(f"        [ ROJO-{id} ] Ha entrado a la partida")
    while(True):
        refugios.acquire()
        with mutex:
            refugiados_rojo[0] += 1
        print(f"        [ ROJO-{id} ] Está refugiado")
        time.sleep(random.randint(2,3))
        print(f"        [ ROJO-{id} ] Sale del refugio")
        with mutex:
            refugiados_rojo[0] -= 1
        refugios.release()

        print(f"        [ ROJO-{id} ] Empieza a disparar")
        time.sleep(random.randint(1,2))
        with mutex:
            probabilidad = 10 - refugiados_azul[0]
        if (1 == random.randint(1,probabilidad)):
            with mutex:
                print(f"        [ ROJO-{id} ] ¡Ha acertado!")
                puntos_rojo[0] += 1
                print(f"---ROJO {puntos_rojo[0]} : {puntos_azul[0]} AZUL---")
        else:
            print(f"        [ ROJO-{id} ] Ha fallado...")


def azules(refugios, mutex, puntos_rojo, puntos_azul, id,refugiados_azul):
    time.sleep(random.randint(0,2))                 #el tiempo que tardan en entrar a la partida
    print(f"[ AZUL-{id} ] Ha entrado a la partida")
    while(True):                    #no hay una condición de escape porque están condenados a jugar al paintball por el resto de la eternidad
        refugios.acquire()                  #Solo dejaremos pasar a cuatro jugadores en total a los refugios
        with mutex:
            refugiados_azul[0] += 1                 #Para saber cuanta gente hay descubierta de cada equipo, contaremos cuántos hay a cubierto
        print(f"[ AZUL-{id} ] Está refugiado")
        time.sleep(random.randint(2,3))                 #El tiempo que pasan refugiados
        print(f"[ AZUL-{id} ] Sale del refugio")
        with mutex:
            refugiados_azul[0] -= 1                 #Anotamos que alguien ha salido del refugio
        refugios.release()

        print(f"[ AZUL-{id} ] Empieza a disparar")
        time.sleep(random.randint(1,2))
        with mutex:
            probabilidad = 10 - refugiados_rojo[0]                  #Calculamos la probabilidad de que al disparar acertemos contra un rival
        if (1 == random.randint(1,probabilidad)):                  #Si se acierta, se anunciará el disparo correcto y la puntuación actual de ambos equipos
            with mutex:
                print(f"[ AZUL-{id} ] ¡Ha acertado!")
                puntos_azul[0] += 1
                print(f"---ROJO {puntos_rojo[0]} : {puntos_azul[0]} AZUL---")
        else:                   #Si no se acierta, se anuncia y sigue adelante con la partida
            print(f"[ AZUL-{id} ] Ha fallado...")

if __name__ == "__main__":
    equipo_rojo = [] #Jugadores del equipo rojo
    equipo_azul = [] #Jugadores del equipo azul
    refugios = Semaphore(4) #Los cuatro refugios disponibles
    mutex = Lock() #Un mutex para proteger las variables compartidas
    puntos_rojo = [0] #Variable compartida que representa la puntuacion del equipo rojo
    puntos_azul = [0] #Variable compartida que representa la puntuacion del equipo azul
    refugiados_rojo = [0] #Variable compartida que representa cuantos refugiados rojos hay
    refugiados_azul = [0] #Variable compartida que representa cuantos refugiados azules hay

    #Generamos los 20 hilos que representan a los jugadores
    for i in range(1,10):
        r = Thread(target=rojos, args=(refugios, mutex, puntos_rojo, puntos_azul, i, refugiados_rojo))
        r.start()
        equipo_rojo.append(r)

    for i in range(1,10):
        a = Thread(target=azules, args=(refugios, mutex, puntos_rojo, puntos_azul, i, refugiados_azul))
        equipo_rojo.append(a)
        a.start()
    
    #Teniendo en cuenta que el programa solo puede terminar mediante interrupción manual, no he considerado necesario el uso de join()