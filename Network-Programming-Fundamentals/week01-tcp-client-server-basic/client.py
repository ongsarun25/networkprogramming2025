# client.py
import socket
from config import HOST, PORT, BUFFER_SIZE

def send_message(message):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        
        print(f"[CLIENT] Sending: {message}")
        client_socket.sendall(message.encode())
        
        response = client_socket.recv(BUFFER_SIZE)
        print(f"[CLIENT] Received: {response.decode()}")
        
    except Exception as e:
        print(f"[CLIENT] Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    import sys
    msg = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Hello Advanced Server"
    send_message(msg)


# extensions/client_multi_message.py
import socket
from config import HOST, PORT, BUFFER_SIZE

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

messages = [
    "hello",
    "how are you?",
    "bye"
]

for m in messages:
    client.sendall(m.encode())
    resp = client.recv(BUFFER_SIZE)
    print(resp.decode())

client.close()