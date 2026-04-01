# node.py

import socket
import threading
import time
from config import *
from delivery_table import DeliveryTable


delivery_table = DeliveryTable()

# message queue format
# (message, timestamp)
message_queue = []


def send_message(peer_port, message):

    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.settimeout(2)

        s.connect((HOST, peer_port))

        s.sendall(message.encode())

        s.close()

        print(f"[{BASE_PORT}] sent -> {peer_port} : {message}")

        return True

    except Exception:

        return False


def forward_loop():

    while True:

        delivery_table.simulate_dynamic_update()

        delivery_table.show_table()

        candidates = delivery_table.get_best_candidates(
            FORWARD_THRESHOLD
        )

        for msg, timestamp in message_queue[:]:

            age = time.time() - timestamp

            if age > MESSAGE_TTL:

                print(f"[{BASE_PORT}] message expired: {msg}")

                message_queue.remove((msg, timestamp))

                continue

            for peer in candidates:

                success = send_message(peer, msg)

                if success:

                    message_queue.remove((msg, timestamp))

                    print(
                        f"[{BASE_PORT}] forwarded opportunistically"
                    )

                    break

        time.sleep(UPDATE_INTERVAL)


def start_server():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((HOST, BASE_PORT))

    server.listen()

    print(f"[{BASE_PORT}] listening...")

    while True:

        conn, addr = server.accept()

        data = conn.recv(BUFFER_SIZE).decode()

        print(f"[{BASE_PORT}] received: {data}")

        message_queue.append((data, time.time()))

        conn.close()


def initial_send():

    for peer in PEER_PORTS:

        msg = f"hello from {BASE_PORT}"

        success = send_message(peer, msg)

        if not success:

            print(f"[{BASE_PORT}] storing message")

            message_queue.append((msg, time.time()))


if __name__ == "__main__":

    # initialize delivery probabilities
    for peer in PEER_PORTS:

        delivery_table.update_probability(
            peer,
            0.6
        )

    threading.Thread(
        target=start_server,
        daemon=True
    ).start()

    threading.Thread(
        target=forward_loop,
        daemon=True
    ).start()

    time.sleep(2)

    initial_send()

    while True:

        time.sleep(1)