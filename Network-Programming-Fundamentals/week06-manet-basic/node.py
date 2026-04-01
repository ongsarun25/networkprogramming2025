# Step 1: Node Maintains a Neighbor Table
# node.py
import socket
import threading
import random
from config import HOST, BASE_PORT, BUFFER_SIZE, NEIGHBORS, FORWARD_PROBABILITY, TTL

neighbor_table = set(NEIGHBORS)

def handle_incoming(conn, addr):
    data = conn.recv(BUFFER_SIZE).decode()
    msg, ttl = data.split('|')
    ttl = int(ttl)
    print(f"[NODE {BASE_PORT}] Received from {addr}: {msg} (TTL={ttl})")
    conn.close()
    
    # Forward probabilistically
    if ttl > 0 and random.random() < FORWARD_PROBABILITY:
        forward_message(msg, ttl - 1, exclude=addr[1])

def start_server(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, port))
    server.listen()
    print(f"[NODE {port}] Listening for neighbors...")
    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_incoming, args=(conn, addr)).start()
#________________________________________
# Step 2: Node Forwards Messages with TTL
def forward_message(message, ttl, exclude=None):
    for peer_port in neighbor_table:
        if peer_port == exclude:
            continue
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, peer_port))
            s.sendall(f"{message}|{ttl}".encode())
            s.close()
        except ConnectionRefusedError:
            print(f"[NODE {BASE_PORT}] Peer {peer_port} unreachable")
#________________________________________
#Step 3: Node Sends Initial Message
if __name__ == "__main__":
    threading.Thread(target=start_server, args=(BASE_PORT,), daemon=True).start()
    
    # Send a test message to neighbors
    test_message = f"Hello from node {BASE_PORT}"
    forward_message(test_message, TTL)


import uuid
import time

# Store recently seen message IDs
seen_messages = {}

MESSAGE_CACHE_TTL = 30  # seconds

def is_duplicate(message_id):
    """Check if message already processed."""
    now = time.time()
    
    # Clean expired entries
    expired = [mid for mid, ts in seen_messages.items() if now - ts > MESSAGE_CACHE_TTL]
    for mid in expired:
        del seen_messages[mid]
    
    if message_id in seen_messages:
        return True
    
    seen_messages[message_id] = now
    return False


HEARTBEAT_INTERVAL = 5

def heartbeat():
    
    while True:
        
        for neighbor in list(neighbor_table):
            
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)
                s.connect((HOST, neighbor))
                s.close()
                
            except:
                print(f"[NODE {BASE_PORT}] Removing inactive neighbor {neighbor}")
                neighbor_table.remove(neighbor)
        
        time.sleep(HEARTBEAT_INTERVAL)

threading.Thread(target=heartbeat, daemon=True).start()

