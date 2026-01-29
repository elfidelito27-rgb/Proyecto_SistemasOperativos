import socket

# LISTA DE SERVIDORES (Simula el descubrimiento de servicios)
servidores = {
    "1": ("Servidor_Local", "127.0.0.1"),
    "2": ("Servidor_Remoto_1", "192.168.1.XX") # Aqui se coloca una IP aleatoria
}

def conectar_a_servidor(ip, puerto=5000):
    try:
        m_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        m_socket.connect((ip, puerto))
        print(f"\n--- Conectado exitosamente al servidor en {ip} ---")
        return m_socket
    except Exception as e:
        print(f"Error al conectar con {ip}: {e}")
        return None

print("=== MIDDLEWARE DE GESTION DISTRIBUIDA ===")
for k, v in servidores.items():
    print(f"[{k}] {v[0]} ({v[1]})")

opcion = input("Selecciona el servidor para monitorear: ")
if opcion in servidores:
    ip_elegida = servidores[opcion][1]
    canal = conectar_a_servidor(ip_elegida)
    
    if canal:
        # Aquí se integra la lógica de envío de comandos de Oswal
        while True:
            cmd = input("Comando (LIST, STATUS, START, STOP, EXIT): ")
            canal.send(cmd.encode())
            if cmd == "EXIT": break
            print("Respuesta:", canal.recv(4096).decode())
        canal.close()
        .,