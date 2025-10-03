import socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind(("10.0.2.7",2001))

server_socket.listen()
print("Server:Bağlantı bekleniyor...")

conn,addr = server_socket.accept()  #addr = ip + port (tuple)   conn = connection line
print("Bağlandı:",addr)

data = conn.recv(1024).decode()
print("Client'tan gelen:",data)

conn.send("Merhaba!".encode())

conn.close()