## Experiment 1 – Packet Loss Observation

### Goal
Observe that UDP does not guarantee delivery.

### Method

Run sender multiple times rapidly:

python sender.py
python sender.py
python sender.py
python sender.py

Receiver output:

[RECEIVER] message 1
[RECEIVER] message 2
(message 3 missing)
[RECEIVER] message 4

### Observation

Some packets may not arrive.

Sender does not detect failure.

### Insight

UDP provides no feedback about delivery success.

Application must tolerate loss.

## Experiment 2 – Sequence Numbers

### Goal
Detect missing datagrams using sequence IDs.

### Sender logic

message format:

0|hello
1|hello
2|hello

### Receiver logic

track received IDs:

if ID missing → packet loss detected

### Observation

receiver output example:

received 0
received 1
received 3

missing packet 2

### Insight

UDP does not track ordering or completeness.

Sequence numbers must be implemented manually.

## Experiment 3 – Manual ACK System

### Goal
Simulate reliable delivery using acknowledgement messages.

### Method

receiver sends "ACK" back to sender.

sender waits for ACK.

if ACK not received → resend message.

### Observation

sender output:

attempt 1 → no ACK
attempt 2 → ACK received

### Insight

Reliability can be implemented at application layer.

TCP provides this automatically.

UDP allows flexibility but increases complexity.

## Experiment 4 – High Speed Sending

### Goal
Observe packet loss when sending many messages quickly.

### Method

send 100 messages rapidly.

for i in range(100):
    send packet

### Observation

receiver output shows gaps in sequence numbers.

Example:

received 1
received 2
received 5
received 6

### Insight

UDP prioritizes speed over reliability.

Operating system buffers may overflow.

Packet loss increases under heavy load.