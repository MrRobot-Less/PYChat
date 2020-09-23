import socket, threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.108", 8080))

def send_message():
    msg = input()
    s.send(msg.encode())

def recv_message():
    msg = s.recv(1024).decode()
    print(msg)

while True:
    
    threading.Thread(target=recv_message).start()
    threading.Thread(target=send_message).start()