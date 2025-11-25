import socket
import threading

HOST = "127.0.0.1"
PORT = 12345

clientes = []                 # Lista con los sockets de clientes conectados
clientes_lock = threading.Lock()  # Lock para acceso seguro a la lista

def manejar_cliente(conn, addr):
	print(f"[+] Cliente conectado: {addr}")

	try:
		while True:
			mensaje = conn.recv(1024)  # Recibir mensaje del cliente
			if not mensaje:
				break  # Si no se recibe nada, el cliente se desconectó

			# Reenviar mensaje a todos los clientes excepto al que lo envió
			with clientes_lock:
				for c in clientes:
					if c != conn:
						try:
							c.send(mensaje)
						except:
							pass  # Si un cliente falla al recibir, simplemente se ignora
	except Exception as e:
		print(f"[!] Error con {addr}: {e}")

	# Si llegamos aquí, el cliente se desconectó o falló
	with clientes_lock:
		if conn in clientes:
			clientes.remove(conn)  # Eliminar del registro de clientes

	conn.close()  # Cerrar socket del cliente
	print(f"[-] Cliente desconectado: {addr}")


if __name__ == "__main__":
	servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	servidor.bind((HOST, PORT))     # Asociar IP y puerto
	servidor.listen()               # Iniciar escucha
	print(f"Servidor escuchando en {HOST}:{PORT}")

	try:
		while True:
			conn, addr = servidor.accept()  # Aceptar nuevo cliente

			# Registrar cliente en la lista compartida
			with clientes_lock:
				clientes.append(conn)

			# Crear un hilo para manejar al nuevo cliente
			hilo = threading.Thread(target=manejar_cliente, args=(conn, addr))
			hilo.daemon = True
			hilo.start()

	except KeyboardInterrupt:
		print("\n[!] Cerrando servidor...")

	finally:
		# Cerrar todas las conexiones activas
		with clientes_lock:
			for c in clientes:
				c.close()
		servidor.close()
