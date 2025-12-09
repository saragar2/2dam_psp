import socket
from threading import Thread

def comunicar(clientes, direcciones, id):
    print(f"{direcciones[id]} se ha unido")
    nombre = clientes[id].recv(1024).decode("UTF-8")
    print(f"{direcciones[id]} ahora se llama {nombre}")
    while True:
        try:
            msg = clientes[id].recv(1024).decode("UTF-8")
            if not msg or msg == "/salir":
                break
            for i in clientes:
                msg2 = "[" + nombre + "] " + msg
                clientes[i].sendall(msg2.encode("UTF-8"))

        except:
            break
    print(f"{nombre} se ha desconectado")
    clientes[id].close()
    

def main():
    lista_clientes = []
    lista_direcciones = []
    id = 0
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(("0.0.0.0", 65434))
    servidor.listen()
    print("Esperando conexiones...")

    while True:
        cliente1, direcc1 = servidor.accept()
        lista_clientes.append(cliente1)
        lista_direcciones.append(direcc1)

        hilo = Thread(target=comunicar, args=(lista_clientes, lista_direcciones, id))
        hilo.start()
        id += 1
        

if __name__ == "__main__":
    main()