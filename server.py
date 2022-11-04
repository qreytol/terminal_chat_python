import socket,sys
from threading import Thread

serv = socket.socket()
ip = '26.98.216.164'
port = 4434
my_ip = socket.gethostbyname(socket.getfqdn())
print(my_ip)

def send(socket_serv: socket.socket):
    while True:
        socket_serv.send(bytes(f'{input(">> ")}',encoding='UTF-8'))

def anon_chat(ip: str, port: int, socket_server: socket.socket):
    socket_server.bind((ip,port))
    print('сервер запущений!')
    socket_server.listen()
    conn, addr = socket_server.accept()
    Thread(target=send, args=(conn,)).start()
    while True:
        print(conn.recv(1024).decode())
        
anon_chat(ip,port,serv)