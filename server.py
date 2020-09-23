import threading
import socket, sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print(ip_address)
clients = []
ip_port = 8080

s.bind((ip_address, ip_port))
s.listen(2)
def add_conection():
    clients.append(s.accept())
    print("+1 pessoa se conectou")
    
def send_message(_from, msg):
    for c in clients:
        if(c[1] != _from):
            c[0].send(msg)

def recv_message(obj,client):
    #obj, client = obj_client
    msg = obj.recv(1024)
    print(obj)
    send_message(client, msg)


while True:
    server = threading.Thread(target=add_conection).start()
    for client in clients:
        #print(client)
        threading.Thread(target=recv_message, args=client).start()
        