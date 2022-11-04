import socket
from threading import Thread

sock = socket.socket()
port = 4434
ip = '26.98.216.164'

nickname = input('Введи нік: ')

def send(socket_server):
    while True:
        a = input('>> ')
        socket_server.send(bytes(f'{nickname}: {input(">> ")}',encoding='UTF-8'))

def anon_chat(ip: str,port: int, socket_server: socket.socket):
    socket_server.connect((ip,port))
    socket_server.send(bytes(f'Зайшов {nickname}',encoding='UTF-8'))
    Thread(target=send, args=(sock,)).start()
    while True:
        print(socket_server.recv(1024).decode())

anon_chat(ip, port,sock)
