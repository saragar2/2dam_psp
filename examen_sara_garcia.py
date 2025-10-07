import random, time
from multiprocessing import Semaphore, Lock, Process, Value

def estudiante(i, libros_sem, mutex, flag_hablando, libros_devueltos, hablando_id):
    time.sleep(random.randint(1, 10)) #el tiempo que tadan en llegar los estudiantes es aleatorio, entre 1 y 10 segundos

    libros_sem.acquire()
    with mutex:
        print(f"Estudiante {i} toma un libro")
    percent = random.randint(1, 10) #cada estudiante "elige" un número aleatorio del 1 al 10
    if (percent == 1 or percent == 2 or percent == 3): #Al solo haber tres números correctos, la probabilidad de que les toque hablar es del 30%
        with mutex:
            hablando_id.value = i
            flag_hablando.value = 1
            print(f"Estudiante {i} está hablando")
    else:
        with mutex:
            print(f"Estudiante {i} estudia en silencio")
    time.sleep(random.randint(1, 3)) #simulamos que el estudiante está hablando/estudiando

    libros_sem.release()
    with mutex:
        if (hablando_id.value == i): #comprobamos que la persona que está devolviendo el libro es la misma que estaba hablando
            flag_hablando.value = 0
        print(f"Estudiante {i} devuelve un libro")
        libros_devueltos.value += 1

def bibliotecario(flag_hablando, libros_devueltos, mutex):
    while (True):
        with mutex:
            print("+++El bibliotecario despierta")
            if (flag_hablando.value == 1):
                print("Bibliotecario: ¡Silencio!")  #Según lo he planteado, es posible que el bibliotecario mande callar más de una vez
                                                    #a la misma persona porque sigue hablando. Supongamos que el estudiante 5 tiene que
                                                    #hablar durante 3 segundos. Durante esos 3 segundos que el estudiante esté hablando,
                                                    #el bibliotecario le mandará callar (respetando los descansos de 1 segundo)
            if (libros_devueltos.value == 10): #cuando todos los libros se hayan devuelto, el bibliotecario saldrá. Podría ponerse en la
                                               #condición del bucle en vez de True, pero es necesario que libros_devueltos esté cubierto por un mutex
                break
            print("---El bibliotecario descansa")
        time.sleep(1)

if __name__ == "__main__":
    alumnos = []						#listado de los alumnos que entran en la biblioteca
    libros_sem = Semaphore(3)			#semáforo que simboliza los tres libros disponibles para leer
    mutex = Lock()						#un Lock para evitar que los print se solapen y regular el acceso a las variables compartidas
    flag_hablando = Value("i", 0)		#variable compartida que será 0 si nadie habla y 1 si alguien habla
    hablando_id = Value("i", 0)			#variable compartida que señala quién está hablando
    libros_devueltos = Value("i", 0)	#variable compartida que cuenta cuántos libros han sido devueltos

    for i in range(10):
        a = Process(target=estudiante, args=(i + 1, libros_sem, mutex, flag_hablando, libros_devueltos, hablando_id))
        alumnos.append(a)
        a.start()

    b = Process(target=bibliotecario, args=(flag_hablando, libros_devueltos, mutex))
    b.start()

    for i in range (10):
        alumnos[i].join()
    
    b.join()
