import socket
import threading

HEADER = 64
PORT = 5050
SERVER = 'localhost'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

messages = []
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handling_clients(conn, addr):
    print(f'[NEW CONNECTION]: {addr}')
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            message = conn.recv(msg_length).decode(FORMAT)
            if message == DISCONNECT_MESSAGE:
                connected = False
            print(f'[CLIENT {addr}]: {message}')
            mess_age = input('[SERVER]: Type Your Message: ').encode(FORMAT)
            mess_age_len = len(mess_age)
            send_len = str(mess_age_len).encode(FORMAT)
            send_len += b' ' * (HEADER - len(send_len))
            conn.send(send_len)
            conn.send(mess_age)

    conn.close()

def start():
    server.listen(999)
    print(f'[SERVER]: Server Is Listening To {SERVER}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handling_clients, args=(conn, addr))
        thread.start()
        print(f'[ACTIVE CLIENTS]: {threading.activeCount() -1}')

print('[SERVER IS STARTING]')
start()