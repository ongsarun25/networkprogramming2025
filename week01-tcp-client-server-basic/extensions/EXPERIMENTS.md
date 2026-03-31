This behavior is useful for demonstration but not realistic for real systems.

Real servers typically run continuously and accept multiple connections sequentially.

Modification

Wrapped the accept() logic inside a loop:

while True:
    conn, addr = server_socket.accept()

    data = conn.recv(BUFFER_SIZE)

    if data:
        msg = data.decode()
        reply = f"ACK: {msg}"

        conn.sendall(reply.encode())

    conn.close()
Learning Insight

TCP communication consists of repeated connection cycles:

listen → accept → communicate → close → accept again

This demonstrates that:

servers must remain available
connections are temporary
TCP sessions are independent
Experiment 2 – Multi-Message Client Session
Problem

Original client sends only one message per connection.

Many real-world applications maintain a session with multiple messages exchanged before closing.

Examples:

chat applications
database connections
API sessions
remote shells
Modification

Client sends multiple messages over a single TCP connection:

messages = [
    "hello",
    "how are you?",
    "bye"
]

for m in messages:
    client.sendall(m.encode())

    response = client.recv(BUFFER_SIZE)

    print(response.decode())
Learning Insight

TCP is stream-oriented, not message-oriented.

Key observations:

multiple send() operations can share one connection
server must handle repeated recv()
connection persists until explicitly closed

Experiment 3 – Timeout Handling
Problem

Blocking socket operations may hang indefinitely if the peer stops responding.

Example:

recv() blocks forever if client disconnects unexpectedly.

Modification

Added timeout protection:

conn.settimeout(10)

try:
    data = conn.recv(BUFFER_SIZE)

except socket.timeout:

    print("connection timeout")
Learning Insight

Blocking I/O is simple but potentially dangerous.

Timeouts introduce controlled failure conditions.

This reflects real production concerns:

network latency
packet loss
client crashes
slow connections
Experiment 4 – Logging System
Problem

Original server prints messages only to terminal.

Real systems maintain logs for:

debugging
auditing
monitoring
failure analysis
Modification

Added simple logging mechanism:

def log(msg):

    with open("server.log", "a") as f:

        f.write(msg + "\n")

Server now records timestamps:

timestamp = time.strftime("%H:%M:%S")

log(f"{timestamp} {msg}")
Learning Insight

Observability is essential in network systems.

Logs allow reconstruction of events:

client connected → message received → response sent

Next Direction

Future weeks may introduce:

UDP communication
peer-to-peer interaction
message persistence
application-layer protocol design
distributed coordination

Week 1 establishes discipline required for these topics.