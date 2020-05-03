import socket
from threading import *
import time

host = '127.0.0.1'
port = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen(1)
print('Wainting for client to connect...')
conn, addr = server.accept()
print('Connected to ',repr(addr))

class Receive(Thread):
    def run(self):
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print('Received from Client: ', data.decode())
            time.sleep(0.2)
            

class Send(Thread):
    def run(self):
        while True:
            msg = input('>')
            if not msg:
                break;
            conn.send(msg.encode())
            time.sleep(0.2)


R = Receive()
S = Send()

R.start()
time.sleep(0.2)
S.start()
