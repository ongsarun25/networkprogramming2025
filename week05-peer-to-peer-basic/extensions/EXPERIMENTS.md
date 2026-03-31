# Week 5 – Peer-to-Peer Experiments

This document records experiments performed to understand decentralized communication using peer-to-peer architecture.

Unlike client-server systems, peer-to-peer networks distribute responsibility across all nodes. Each peer must be capable of both sending and receiving messages concurrently.

Peer-to-peer systems introduce resilience, flexibility, and complexity.

---

## Experiment 1 – Bidirectional Messaging

### Goal

Verify that peers can both send and receive messages.

### Method

Run two peers:

Terminal 1
python peer.py 1

Terminal 2
python peer.py 2

Send messages in both directions.

### Result

Peer 1 → Peer 2 communication works.
Peer 2 → Peer 1 communication works.

Both nodes act as sender and receiver.

### Observation

Connections are created dynamically when sending.

Listening socket remains active continuously.

### Insight

Peer-to-peer nodes must maintain continuous availability while initiating connections when needed.

---

## Experiment 2 – Multi-Peer Communication

### Goal

Test network with more than two peers.

### Method

Run 3 peers:

python peer.py 1
python peer.py 2
python peer.py 3

Send messages between all peers.

### Result

Each peer can communicate with any other peer.

Network topology forms a mesh.

### Observation

Each peer manages its own connections independently.

No central coordination required.

### Insight

Peer-to-peer networks scale horizontally by adding more nodes.

However, complexity increases with network size.

---

## Experiment 3 – Broadcast to All Known Peers

### Goal

Simulate group messaging without central server.

### Method

Maintain list of known peers.

Send same message to multiple peers.

### Result

All peers receive identical message.

### Observation

Sender must manually send message to each peer.

Multiple connections created sequentially.

### Insight

Peer-to-peer broadcast increases traffic compared to multicast.

Tradeoff between decentralization and efficiency.

---

## Experiment 4 – Peer Discovery Simulation

### Goal

Simulate mechanism for discovering active peers.

### Method

Each peer periodically sends ping messages.

Other peers respond with acknowledgement.

### Result

Peer list updated dynamically.

Offline peers detected through connection failure.

### Observation

Peer discovery requires additional communication overhead.

System must tolerate incomplete or outdated peer lists.

### Insight

Decentralized systems must handle uncertainty and partial knowledge.

Discovery protocols are essential for scalable P2P networks.

---

## Experiment 5 – Reliable Messaging Layer

### Goal

Add basic acknowledgement mechanism.

### Method

Receiver sends ACK message.

Sender resends if ACK not received.

### Result

Messages delivered reliably despite transient failures.

### Observation

Reliability requires additional state tracking.

Complexity increases significantly.

### Insight

TCP provides reliability automatically.

Peer-to-peer protocols often implement custom reliability layers.

---

## P2P Characteristics Summary

| Property | Behavior |
|---------|----------|
| Central authority | None |
| Communication direction | Bidirectional |
| Fault tolerance | High |
| Complexity | High |
| Scalability | Horizontal |
| Resource control | Distributed |

---

## Comparison with Previous Weeks

Week 1 – Client Server

Centralized control.

Single server responsible for communication.

---

Week 3 – Broadcast

One sender transmits to all nodes.

Receivers passive.

---

Week 4 – Multicast

Receivers subscribe to group.

Selective distribution.

---

Week 5 – Peer-to-Peer

All nodes equal.

All nodes responsible.

Connections dynamic.

---

## Real World Systems Using P2P

BitTorrent distributes file chunks across many peers.

Blockchain networks propagate transactions across nodes.

IPFS stores content across distributed peers.

Voice communication systems sometimes establish direct peer connections.

---

## Limitations of Peer-to-Peer

Peer availability unpredictable.

Security harder to enforce.

Network topology constantly changing.

Discovery mechanisms required.

Coordination more complex.

---

## Reflection

Peer-to-peer networking removes dependency on central infrastructure.

This increases system resilience but requires careful coordination.

Designers must consider:

peer discovery

failure handling

message routing

network scalability

Peer-to-peer systems emphasize cooperation between independent nodes.

---

## Conclusion

Peer-to-peer architecture distributes responsibility across nodes.

Each peer contributes resources to the network.

This creates robust and scalable systems capable of functioning without central authority.

Understanding peer-to-peer communication prepares students for distributed computing challenges.