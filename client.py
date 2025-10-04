import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #AF_INET = IPv4 / AF_INET6 = IPv6
# SOCK_STREAM = use TCP protocol , SOCK_DGRAM = use UDP
client_socket.connect(("10.0.2.7",2001)) #connect takes one parameter so () is required
client_socket.settimeout(60)
try:
    while True:
        message = input("Client >> ")
        client_socket.send(message.encode())
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                print("Server disconnected!")
                break
            print("From Server:",data)
        except socket.timeout:
            print("The server is not responding.")
            break
        except KeyboardInterrupt:
            print("Connection being terminated.")
            break

        if message.lower().strip() == "quit" :
            break
except Exception as e:
    print("An error occurred:",e)
finally:
    client_socket.close()
