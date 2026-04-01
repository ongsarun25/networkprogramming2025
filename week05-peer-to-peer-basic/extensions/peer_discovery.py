import socket
import time

def ping_peer(port):

    try:

        s = socket.socket()
        s.settimeout(1)

        s.connect(("127.0.0.1", port))
        s.close()

        return True

    except:

        return False


def discover(base_port, max_peers=5):

    active = []

    for i in range(1, max_peers+1):

        port = base_port + i

        if ping_peer(port):

            active.append(i)

    return active


if __name__ == "__main__":

    peers = discover(9000)

    print("active peers:", peers)