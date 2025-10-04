import socket
from asyncio import timeout

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind(("10.0.2.7",2001))

server_socket.listen()
print("Server:Waiting for connection...")

conn,addr = server_socket.accept()  #addr = ip + port (tuple)   conn = connection line
print("Connected:",addr)
conn.settimeout(60)
# server_socket = Connection-waiting socket (listener)        conn = Actual connection socket (communication line)

while True:
    try:
        data = conn.recv(1024).decode()
        if not data:
            print("Client disconnected!")
            break
        print("From Client:",data)

        message = input("Server >> ")
        conn.send(message.encode())
    except socket.timeout:
        print("Client is not responding.")
        break
    except KeyboardInterrupt:
        print("Connection being terminated.")
        break

conn.close()
server_socket.close()