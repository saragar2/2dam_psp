from multiprocessing import Process
import os

# Función que se ejecutará en el proceso hijo
def mostrar_mensaje():
    print("Este mensaje proviene de un proceso hijo.")
if __name__ == '__main__': # Para que no se ejecute en el hijo
    p = Process(target=mostrar_mensaje) # Crear proceso hijo
    p.start() # Iniciar ejecución del proceso hijo
    print("PID del proceso actual:", os.getpid()) # ID único del proceso actual
    print("PID del proceso padre:", os.getppid()) # ID del proceso que lo ha lanzado
    p.join() # Esperar que termine
print("Proceso principal finalizado.")