import socket
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #AF_INET = IPv4 / AF_INET6 = IPv6
# SOCK_STREAM = use TCP protocol , SOCK_DGRAM = use UDP
client_socket.connect(("10.0.2.7",2001)) #connect takes one parameter so () is required

client_socket.send("Merhaba server!".encode())

data = client_socket.recv(1024).decode()
print("Server'dan gelen:",data)

client_socket.close()