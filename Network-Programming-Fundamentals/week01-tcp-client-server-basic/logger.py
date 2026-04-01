# logger.py
from datetime import datetime

def log_event(level, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    print(f"[{timestamp}] [{level}] {message}")

def log_info(message):
    log_event("INFO", message)

def log_error(message):
    log_event("ERROR", message)

# extensions/server_logger.py
import socket
import time
from config import HOST, PORT, BUFFER_SIZE

def log(msg):
    with open("server.log", "a") as f:
        f.write(msg + "\n")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

conn, addr = server.accept()

data = conn.recv(BUFFER_SIZE)

if data:
    msg = data.decode()
    timestamp = time.strftime("%H:%M:%S")

    log(f"{timestamp} {msg}")

    conn.sendall(b"logged")