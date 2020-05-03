import socket
from threading import *
import time

host = '127.0.0.1'
port = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host,port))

class Receive(Thread):
    def run(self):
        while True:
            data = client.recv(1024);
            if not data:
                break;
            print('Received from Server: ',data.decode())
            time.sleep(0.2)

class Send(Thread):
    def run(self):
        while True:
            msg = input('>')
            if not msg:
                break
            client.send(msg.encode())
            time.sleep(0.2)

R = Receive()
S = Send()

R.start()
time.sleep(0.2)
S.start()

            
