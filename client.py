import socket #importaccion de socket de red 

HOST = '127.0.0.1'  # host computadora 
PORT = 5000 #puerto de enlace 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4(AF_INET) #TCP (SOCK_STREAM)
client.connect((HOST, PORT))#MARCACION DEL cliente de encendido 

print("Conectado al servidor")#impresion del mensaje 

while True: #bucle infinito hasta el exit comand
    print("\nComandos disponibles:")#impresion de los comandos print
    print("LIST               -> Listar procesos")
    print("STATUS             -> CPU y memoria")
    print("START <programa>   -> Iniciar proceso")
    print("STOP <pid>         -> Detener proceso")
    print("EXIT               -> Salir")

    comando = input(">> ")#lectura de los comandos 
    client.send(comando.encode())#respuesta del servidor esperando

    respuesta = client.recv(4096).decode()#recibe
    print(respuesta)#se imprime la respuesta 

    if comando == "EXIT":#se termina el bucle comando exit 
        break

client.close()#se cierra el servidor
...