import socket
import psutil
import subprocess

HOST = '127.0.0.1'
PORT = 5000


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Servidor activo en {HOST}:{PORT}")

conn, addr = server.accept()
print("Cliente conectado desde:", addr)

while True:
    comando = conn.recv(1024).decode()

    
    if comando == "LIST":
        salida = ""
        for p in psutil.process_iter(['pid', 'name']):
            salida += f"PID: {p.info['pid']} - {p.info['name']}\n"
        conn.send(salida.encode())

    
    elif comando == "STATUS":
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory().percent
        conn.send(f"CPU: {cpu}% | MEMORIA: {mem}%".encode())

   
    elif comando.startswith("START"):
        try:
            app = comando.split(" ", 1)[1]
            subprocess.Popen(app, shell=True)
            conn.send(f"Proceso iniciado: {app}".encode())
        except:
            conn.send("Error al iniciar proceso".encode())

    
    elif comando.startswith("STOP"):
        try:
            pid = int(comando.split(" ")[1])
            psutil.Process(pid).terminate()
            conn.send(f"Proceso {pid} detenido".encode())
        except:
            conn.send("Error al detener proceso".encode())

    
    elif comando == "EXIT":
        conn.send("Servidor cerrado".encode())
        break

    else:
        conn.send("Comando no válido".encode())

conn.close()
server.close()
