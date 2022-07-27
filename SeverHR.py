import csv
import socket
import threading
import time
import pandas as pd

Header = 64
Port = 6809
ser = socket.gethostbyname(socket.gethostname())
ADDR = (ser, Port)
form = 'utf-8'

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.bind(ADDR)
#print(ser)


def handle_client(conn, addr):
    print(f"New connection {addr} connected")
    connected = True



def start():
    c.listen()
    while True:
        conn, addr = c.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()}")



print("Server is connecting")
start()



