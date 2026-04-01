# WEEK 10 — Quantum-Inspired Networking (Conceptual)

## Overview
This lab explores networking concepts inspired by principles from quantum communication theory. Although no real quantum hardware is used, the system simulates behaviors such as:

- messages that can only be read once
- tokens that expire after a limited time
- probabilistic message delivery
- state-aware message forwarding

The implementation demonstrates how distributed systems can model **ephemeral communication**, **state collapse**, and **secure message handling** using traditional networking tools.

The goal is to develop intuition for designing systems where **message state changes after access**, similar to how quantum measurement affects physical systems.

---

## Learning Objectives

After completing this lab, students should be able to:

- implement one-time-read message tokens
- simulate message state collapse after access
- apply probabilistic routing decisions
- manage token lifecycle in a distributed system
- understand conceptual foundations of quantum-safe communication design

Traits developed:

- security-conscious thinking
- distributed system awareness
- probabilistic modeling mindset
- minimalistic message handling

---

## Repository Structure

```
week10-quantum-network-basic/
│
├── README.md
├── config.py
├── node.py
├── token.py
│
└── docs/
    └── run_instructions.md
```

---

## Core Concepts

### 1. One-Time-Read Tokens
Each message is wrapped in a Token object that allows only one successful read operation.

Once accessed, the message becomes unavailable.

This simulates the quantum concept that observing a system changes its state.

Example:

```python
token = Token("Hello")
print(token.read_token())  # valid
print(token.read_token())  # None
```

---

### 2. Token Expiry
Tokens expire after a fixed time interval defined in `config.py`.

Expired tokens cannot be forwarded or read again.

This prevents stale information from circulating indefinitely.

```
TOKEN_EXPIRY = 10 seconds
```

---

### 3. State Collapse Behavior
When a node reads a token:

- the token state changes permanently
- forwarding decisions depend on token availability
- duplicate reads are prevented

This demonstrates how system state evolves based on interactions.

---

### 4. Probabilistic Routing
Token forwarding may be randomized to simulate uncertain network outcomes.

This models probabilistic state transitions similar to quantum measurement results.

Example idea:

```
60% chance token is forwarded
40% chance token collapses
```

---

## Configuration

Edit `config.py` to modify network parameters:

```python
HOST = "127.0.0.1"

BASE_PORT = 11000

PEER_PORTS = [
    11001,
    11002
]

BUFFER_SIZE = 1024

TOKEN_EXPIRY = 10

UPDATE_INTERVAL = 5
```

Important parameters:

| variable | purpose |
|----------|---------|
| BASE_PORT | port of current node |
| PEER_PORTS | ports of other nodes |
| TOKEN_EXPIRY | lifetime of token |
| UPDATE_INTERVAL | forwarding interval |
| BUFFER_SIZE | socket receive limit |

---

## How It Works

Each node performs two main tasks:

### Server Thread
Listens for incoming tokens from peers.

When a token arrives:
1. token is wrapped in Token object
2. token is read once
3. valid tokens are stored in queue
4. invalid tokens are discarded

---

### Forwarding Thread
Periodically attempts to send tokens to peers.

Token forwarding stops when:

- token is already read
- token expires
- token successfully reaches another node

---

## Running the Lab

### Step 1 — open multiple terminals

Example:

Terminal 1
```
python node.py
```

Terminal 2
```
python node.py
```

Terminal 3
```
python node.py
```

---

### Step 2 — assign different BASE_PORT values

Example:

node A

```
BASE_PORT = 11000
PEER_PORTS = [11001,11002]
```

node B

```
BASE_PORT = 11001
PEER_PORTS = [11000,11002]
```

node C

```
BASE_PORT = 11002
PEER_PORTS = [11000,11001]
```

---

### Step 3 — observe behavior

Expected output:

```
[NODE 11000] Listening for incoming tokens...

[NODE 11001] Received token: Quantum token from 11000

[NODE 11002] Received token: Quantum token from 11001

[NODE 11000] Token expired
```

---

## Expected Results

- tokens are delivered only once per node
- duplicate tokens are rejected
- expired tokens are ignored
- not all tokens reach every node (probabilistic behavior)

---

## Extensions Implemented

Additional functionality may include:

### token expiry enforcement
ensures tokens automatically become invalid after a time period

### duplicate detection
prevents token cloning across network nodes

### probabilistic forwarding
simulates non-deterministic network state changes

### lifecycle logging
tracks token creation, forwarding, expiration, and consumption

---

## Real-World Mapping

Although conceptual, this lab relates to real technologies:

| concept | real-world example |
|--------|-------------------|
| one-time messages | OTP authentication |
| ephemeral communication | secure messaging apps |
| token expiration | session security |
| probabilistic routing | delay tolerant networks |
| state awareness | distributed consensus systems |

---

## Key Takeaway

Traditional networking assumes messages can be copied and resent indefinitely.

Quantum-inspired thinking introduces constraints:

- information may be temporary
- duplication may not be allowed
- access may change system state

These constraints encourage new approaches to:

- privacy-first system design
- secure communication protocols
- distributed state modeling