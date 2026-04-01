# Week 2 Extensions – UDP Behavior Experiments

The base lab introduces UDP communication as a contrast to TCP.

Unlike TCP, UDP does not establish a connection, does not guarantee delivery, and does not ensure ordering.

The goal of these extensions is to explore the consequences of this design choice.

Instead of relying on built-in reliability, we observe how application logic must compensate.

All original instructor files remain unchanged.

Additional experimental modules are placed in the extensions folder.

---

# Overview of Experiments

| File | Goal | Concept |
|------|-----|--------|
| udp_sequence_sender.py | detect missing packets | reliability awareness |
| udp_sequence_receiver.py | track received IDs | unordered delivery |
| udp_ack_sender.py | implement retry logic | application-layer reliability |
| udp_ack_receiver.py | send manual acknowledgements | reliability construction |
| udp_flood_sender.py | send high-speed datagrams | packet loss observation |
| udp_random_delay_receiver.py | simulate network jitter | ordering instability |

---

# Experiment 1 – Sequence Numbers

## Problem

UDP does not provide:

- delivery guarantee
- ordering guarantee
- duplicate protection

The receiver cannot detect missing messages without additional information.

## Approach

Embed sequence numbers into each datagram.

Example message format:

0|Hello
1|Hello
2|Hello

Sender:

```python
for i in range(10):

    message = f"{i}|test message"

    sock.sendto(message.encode(), (HOST, PORT))