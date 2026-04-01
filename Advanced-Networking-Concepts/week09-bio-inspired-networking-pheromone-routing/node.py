# node.py

import socket
import threading
import time

from config import *
from pheromone_table import PheromoneTable


pheromone_table = PheromoneTable()

# queue format:
# (message, timestamp)

message_queue = []


def send_message(peer_port, message):

    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.settimeout(2)

        s.connect((HOST, peer_port))

        s.sendall(message.encode())

        s.close()

        print(f"[{BASE_PORT}] sent via {peer_port}")

        # reinforce successful path

        pheromone_table.reinforce(

            peer_port,

            REINFORCEMENT

        )

        return True


    except Exception:

        print(f"[{BASE_PORT}] failed path {peer_port}")

        return False



def forward_loop():

    while True:

        pheromone_table.decay()

        pheromone_table.show_table()

        candidates = pheromone_table.get_best_candidates(

            FORWARD_THRESHOLD

        )


        for msg, timestamp in message_queue[:]:

            age = time.time() - timestamp


            if age > MESSAGE_TTL:

                print(f"[{BASE_PORT}] expired message")

                message_queue.remove((msg, timestamp))

                continue


            for peer in candidates:

                success = send_message(peer, msg)


                if success:

                    message_queue.remove((msg, timestamp))

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



def initial_attempt():

    for peer in PEER_PORTS:

        msg = f"bio-message from {BASE_PORT}"

        success = send_message(peer, msg)


        if not success:

            print(f"[{BASE_PORT}] storing message")

            message_queue.append((msg, time.time()))



if __name__ == "__main__":

    # initialize pheromones

    for peer in PEER_PORTS:

        pheromone_table.reinforce(

            peer,

            INITIAL_PHEROMONE

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

    initial_attempt()


    while True:

        time.sleep(1)