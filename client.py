import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = 'localhost'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
print(f'[SERVER]: You Are Connected with{ADDR}')

def send(msg):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' ' * (HEADER - len(send_len))
    client.send(send_len)
    client.send(message)
while True:
    msg = str(input('Type Your Message: '))
    send(msg)
    recv_msg = client.recv(HEADER).decode(FORMAT)
    if recv_msg:
        recv_msg = int(recv_msg)
        message = client.recv(recv_msg).decode(FORMAT)
        print(f'[SERVER]: {message}')
    if msg == DISCONNECT_MESSAGE:
        break