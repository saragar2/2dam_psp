import socket
import threading
import sys

HOST = "127.0.0.1"
PORT = 12345

def recibir_mensajes(sock):
	try:
		while True:
			mensaje = sock.recv(1024)  # Recibir datos del servidor
			if not mensaje:
				print("Conexión cerrada por el servidor.")
				break
			print("\n" + mensaje.decode())  # Mostrar mensajes de otros clientes
	except:
		pass
	finally:
		sock.close()
		sys.exit()  # Termina el hilo y el programa

if __name__ == "__main__":
	cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	cliente.connect((HOST, PORT))  # Conectar al servidor

	print("Conectado al servidor. Escribe 'salir' para desconectarte.")

	# Iniciar hilo para recibir mensajes del servidor
	hilo = threading.Thread(target=recibir_mensajes, args=(cliente,))
	hilo.daemon = True
	hilo.start()

	try:
		while True:
			mensaje = input()  # Leer mensaje del usuario

			if mensaje.lower() == "salir":  # Comando para desconectarse
				break

			cliente.send(mensaje.encode())  # Enviar mensaje al servidor
	except KeyboardInterrupt:
		pass
	finally:
		cliente.close()  # Cerrar conexión
		print("Desconectado.")
