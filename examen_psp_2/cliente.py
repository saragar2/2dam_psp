import socket
from threading import Thread

def enviar(cliente):
    nombre = input("Cómo te llamas?: ")
    cliente.sendall(nombre.encode("UTF-8"))
    while True:
        msg = input(f"[{nombre}] Di algo: ")
        if (msg == "/salir"):
            break
        cliente.sendall(msg.encode("UTF-8"))
        print(cliente.recv(1024).decode("UTF-8"))
    cliente.close()
    

def main():
    id = 0
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(("0.0.0.0", 65434))

    hilo = Thread(target=enviar, args=(cliente,))
    hilo.start()
        

if __name__ == "__main__":
    main()