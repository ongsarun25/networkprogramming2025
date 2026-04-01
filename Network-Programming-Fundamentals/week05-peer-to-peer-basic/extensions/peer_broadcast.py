import socket
import threading
import sys
from config import HOST, BASE_PORT, BUFFER_SIZE

peer_id = int(sys.argv[1])
PORT = BASE_PORT + peer_id

KNOWN_PEERS = [1,2,3,4,5]

def listen():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"[PEER {peer_id}] listening on {PORT}")

    while True:
        conn, addr = server.accept()
        data = conn.recv(BUFFER_SIZE).decode()

        print(f"[PEER {peer_id}] received: {data}")

        conn.close()

def send(target_id, msg):

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, BASE_PORT + target_id))
        s.send(msg.encode())
        s.close()

    except:
        print(f"[PEER {peer_id}] peer {target_id} offline")

def broadcast(msg):

    for p in KNOWN_PEERS:

        if p != peer_id:
            send(p, msg)

threading.Thread(target=listen, daemon=True).start()

while True:

    cmd = input("message (or 'all'): ")

    if cmd == "all":

        msg = input("broadcast message: ")
        broadcast(msg)

    else:

        target = int(cmd)
        msg = input("message: ")

        send(target, msg)