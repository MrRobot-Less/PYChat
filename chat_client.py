import socket, threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

name = input("name: ")
ip_address = input("host: ")
ip_port = int(input("port: "))

def send_message():
    while True:
        msg = input()
        data = name + ": "+msg
        s.send(data.encode())

def recv_message():
    while True:
        msg = s.recv(1024).decode("utf-8")
        print("\n"+msg)

def connect():
    s.connect((ip_address, ip_port))
    s.send(name.encode("utf-8"))

if __name__ == '__main__':
    connect()
    threading.Thread(target=recv_message).start()
    threading.Thread(target=send_message).start()
    
