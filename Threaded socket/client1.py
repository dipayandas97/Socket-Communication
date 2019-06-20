import socket
host = '127.0.0.1'
port = 8080
msg = "Helo from client 1"
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((host,port))

    while True:
        
        client.send(msg.encode())
