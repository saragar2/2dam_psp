from multiprocessing import Process
import os
import time

def mostrar_estado(i):
    print(i, ": PID del proceso actual:", os.getpid())
    time.sleep(2)

if (__name__ == '__main__'):
    p1 = Process(target=mostrar_estado, args=[1])
    p2 = Process(target=mostrar_estado, args=[2])
    p1.start()
    p2.start()
    p1.join()
    p2.join()