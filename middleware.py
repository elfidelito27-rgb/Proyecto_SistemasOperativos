import socket

# 1. LISTA DE SERVIDORES
servidores = {
    "1": ("Servidor_Local_5000", "127.0.0.1", 5000),
    "2": ("Servidor_Local_5001", "127.0.0.1", 5001)
}

def conectar_a_servidor(ip, puerto): # Quitamos el valor por defecto de 5000
    try:
        m_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        m_socket.connect((ip, puerto)) # Ahora conecta al puerto que le mandemos
        print(f"\n--- Conectado exitosamente al servidor en {ip}:{puerto} ---")
        return m_socket
    except Exception as e:
        print(f"Error al conectar con {ip}:{puerto}: {e}")
        return None

print("=== MIDDLEWARE DE GESTION DISTRIBUIDA ===")
for k, v in servidores.items():
    # Mostramos Nombre, IP y Puerto en el menú
    print(f"[{k}] {v[0]} ({v[1]}:{v[2]})")

opcion = input("\nSelecciona el servidor para monitorear: ")

if opcion in servidores:
    ip_elegida = servidores[opcion][1]
    puerto_elegido = servidores[opcion][2] # Extraemos el puerto del diccionario
    
    # Intentamos la conexión usando los datos elegidos
    canal = conectar_a_servidor(ip_elegida, puerto_elegido)
    
    if canal:
        # Lógica de envío de comandos
        while True:
            cmd = input("\nComando (LIST, STATUS, START, STOP, EXIT): ")
            canal.send(cmd.encode())
            
            if cmd == "EXIT":
                break
            
            # Recibimos la respuesta del servidor activo
            respuesta = canal.recv(4096).decode()
            print("Respuesta:", respuesta)
        
        canal.close()
else:
    print("Opción no válida. Cerrando Middleware.")
