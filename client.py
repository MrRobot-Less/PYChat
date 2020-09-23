import socket, threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = input("Host: ")
ip_port = int(input("Port: "))

s.connect((ip_address, ip_port))

def send_message():
    msg = input()
    s.send(msg.encode())

def recv_message():
    msg = s.recv(1024).decode()
    print(msg)

while True:
    
    threading.Thread(target=recv_message).start()
    threading.Thread(target=send_message).start()