import socket
from config import IP, PORT


def run_client():
    print('run client')
    sock_client = socket.socket()
    sock_client.connect(('localhost', 8081))
    sock_client.send('hello, world!')
    data = sock_client.recv(1024)
    sock_client.close()
    print(data)
