import socket
from config import IP, PORT, PACKET_SIZE


def run_server():
    print("Running server")
    serv_config = (IP, PORT)    #server params
    socket_obj = socket.socket()
    socket_obj.bind(serv_config)    #port binding
    print(f"Binding port: {PORT}")
    socket_obj.listen()     #start listen port
    print(f"Start listen port: {PORT}")
    conn, addr = socket_obj.accept()    #wait coonection
    print(f"Connected: {addr}")
    data = True
    while data:
        data = conn.recv(10).decode("utf-8")
        print(data)
        conn.send(b"PRINAYL")   #sending a response
        if data[:4] == "exit":
            break
    conn.close()
