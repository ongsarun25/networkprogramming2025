import socket
import threading
import sys
import time

HOST = "127.0.0.1"
BASE_PORT = 9000
BUFFER = 1024

peer_id = int(sys.argv[1])

PORT = BASE_PORT + peer_id

def listen():

    s = socket.socket()
    s.bind((HOST, PORT))
    s.listen()

    while True:

        conn, addr = s.accept()

        data = conn.recv(BUFFER).decode()

        print("received:", data)

        conn.send(b"ACK")

        conn.close()

def send(target, msg):

    port = BASE_PORT + target

    for attempt in range(3):

        try:

            s = socket.socket()
            s.settimeout(2)

            s.connect((HOST, port))

            s.send(msg.encode())

            ack = s.recv(BUFFER)

            print("ACK received")

            s.close()

            return

        except:

            print("retry", attempt+1)

            time.sleep(1)

    print("failed delivery")

threading.Thread(target=listen, daemon=True).start()

while True:

    t = int(input("target: "))

    m = input("message: ")

    send(t, m)