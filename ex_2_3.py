from threading import Thread
from multiprocessing import Process
import time, random

#-----1-----
# def saludar(id):
#     print(f"HOLA SOY {id}, ADIOS")

# if __name__ == "__main__":
#     h2 = Thread(target=saludar, args=(2,))
#     h3 = Thread(target=saludar, args=(3,))
#     h1 = Thread(target=saludar, args=(1,))

#     h1.start()
#     h2.start()
#     h3.start()

#     h1.join()
#     h2.join()
#     h3.join()

#     print("sacabao")

#-----2-----
def no_se_no_soy_religiosa(idp, idt):
    print(f"HOLA SOY {idt}, HIJO LEGITIMO DE {idp}")
    time.sleep(random.randint(1,3))

def genesis(id):
    papis1 = str(id) + "1"
    papis2 = str(id) + "2"
    h1 = Thread(target=no_se_no_soy_religiosa, args=(id, papis1,))
    h2 = Thread(target=no_se_no_soy_religiosa, args=(id, papis2,))

    h1.start()
    h2.start()

    h1.join()
    h2.join()

if __name__ == "__main__":
    p1 = Process(target=genesis, args=(1,))
    p2 = Process(target=genesis, args=(2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()