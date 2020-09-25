import threading
import socket, sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print(ip_address)

clients = []

ip_port = int(input("port: "))
len_connections = int(input("limit Connections: "))

s.bind((ip_address, ip_port))
s.listen(len_connections)

def add_conection():
    clients.append(s.accept())
    client_name = clients[len(clients)-1][0].recv(1024).decode()
    print(client_name+" has connected")
    
def send_message(_from, msg):
    for c in clients:
        if(c[1] != _from):
            c[0].send(msg)

def recv_message(obj,client):
    
    msg = obj.recv(1024)
    if(msg):
        send_message(client, msg)

if __name__ == '__main__':
    
    while True:
        threading.Thread(target=add_conection).start()
        for client in clients:
            threading.Thread(target=recv_message, args=client).start()
            
