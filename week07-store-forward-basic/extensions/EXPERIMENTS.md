# Week 7 – Store-and-Forward Networking Experiments

This document records experiments performed to understand delay-tolerant communication where messages are stored locally when delivery fails and forwarded later when connectivity becomes available.

Store-and-forward networking assumes unreliable connectivity and uses memory as a temporary transport layer.

This principle is used in systems where continuous connectivity cannot be guaranteed.

---

## Experiment 1 – Basic Store and Forward

### Goal

Verify that messages are stored locally when a peer is offline and forwarded later when the peer becomes available.

### Method

Configuration:

Node 8000:
PEER_PORTS = [8001]

Node 8001 is initially offline.

Run node 8000 first:

python node.py

### Result

Console output:

[NODE 8000] Peer 8001 unavailable, storing message
[NODE 8000] Queue size: 1

After starting node 8001:

[NODE 8000] Retrying to 8001...
[NODE 8000] Sent stored message to 8001

Node 8001 receives:

[NODE 8001] Received: Hello from node 8000

### Observation

Messages are successfully delivered after connectivity is restored.

### Insight

Store-and-forward guarantees eventual delivery even when nodes are temporarily offline.

---

## Experiment 2 – Multiple Queued Messages

### Goal

Verify that multiple messages are stored and delivered in FIFO order.

### Method

Keep node 8001 offline.

Send multiple messages from node 8000.

Example messages:

Message 1
Message 2
Message 3

Start node 8001 later.

### Result

Messages delivered in same order:

Message 1 → Message 2 → Message 3

### Observation

Queue preserves ordering.

### Insight

FIFO queues maintain message sequence consistency.

---

## Experiment 3 – Retry Mechanism

### Goal

Observe periodic retry attempts.

### Method

Set:

RETRY_INTERVAL = 3 seconds

Keep peer offline for 15 seconds.

### Result

Console output:

Retry attempt 1
Retry attempt 2
Retry attempt 3
Retry attempt 4

After peer becomes online:

Message delivered successfully.

### Observation

Retry loop continues automatically without blocking main program.

### Insight

Background retry logic allows asynchronous recovery.

---

## Experiment 4 – Queue Growth During Extended Failure

### Goal

Observe queue growth when peer unavailable for long duration.

### Method

Keep peer offline.

Send many messages:

for i in range(10):
    send_message()

### Result

Queue size increases:

Queue size: 10

Messages remain stored until delivery possible.

### Observation

Queue acts as temporary storage buffer.

### Insight

Queue capacity planning is important for large-scale systems.

---

## Experiment 5 – Persistent Queue Storage

### Goal

Ensure messages survive node restart.

### Method

Implement queue serialization using JSON.

Save queue contents to file.

Restart node.

### Result

Queued messages restored after restart.

Example file:

queue_8000.json

### Observation

Messages not lost during crash or shutdown.

### Insight

Persistent storage increases reliability.

Common in email and messaging systems.

---

## Experiment 6 – Exponential Backoff Retry

### Goal

Reduce retry frequency over time to avoid network overload.

### Method

Retry interval doubles after each failure:

2 seconds
4 seconds
8 seconds
16 seconds

### Result

Retry frequency decreases gradually.

Network congestion reduced.

### Observation

Repeated failures trigger slower retry attempts.

### Insight

Exponential backoff balances persistence with efficiency.

Widely used in TCP congestion control.

---

## Experiment 7 – Priority Message Queue

### Goal

Ensure urgent messages delivered before normal messages.

### Method

Define two queue levels:

High priority
Normal priority

Add urgent message:

queue.add_message("Emergency alert", priority="high")

### Result

High priority message delivered first.

### Observation

Queue prioritization affects delivery order.

### Insight

Critical systems require priority-based scheduling.

---

## Experiment 8 – Maximum Retry Limit

### Goal

Prevent infinite retry attempts.

### Method

Set:

MAX_ATTEMPTS = 5

Send message while peer remains offline.

### Result

After 5 attempts:

[NODE 8000] Giving up on message to 8001

Message removed from queue.

### Observation

System avoids infinite retry loops.

### Insight

Systems must balance persistence with resource limits.

---

## Experiment 9 – Message Expiration (TTL)

### Goal

Remove outdated messages automatically.

### Method

Set:

MESSAGE_TTL = 60 seconds

Messages older than 60 seconds removed.

### Result

Expired messages deleted from queue.

### Observation

Queue maintains relevant data only.

### Insight

Prevents outdated information delivery.

---

## Experiment 10 – Multi-Peer Delivery

### Goal

Store messages for multiple offline peers simultaneously.

### Method

Configuration:

PEER_PORTS = [8001, 8002]

Keep both peers offline initially.

Start peers one at a time.

### Result

Messages delivered individually when each peer becomes available.

### Observation

Queue tracks messages per peer.

### Insight

Store-forward supports multiple destinations independently.

---

## Behavior Summary

| Feature | Behavior |
|--------|---------|
| Delivery guarantee | Eventual |
| Immediate connectivity required | No |
| Retry mechanism | Periodic |
| Failure handling | Store locally |
| Queue type | FIFO |
| Persistence | Optional |
| Reliability | High |
| Latency | Variable |

---

## Comparison with Previous Weeks

### Week 6 – MANET

Messages may be dropped permanently.

Delivery depends on probability.

### Week 7 – Store-and-Forward

Messages buffered locally.

Delivery occurs when connection restored.

Reliability significantly improved.

---

## Real-World Applications

Store-and-forward architecture is widely used in real systems:

Email servers buffer messages until recipient server reachable.

Satellite communication experiences long delays between transmission windows.

IoT sensors store data when internet unavailable.

Mobile messaging apps queue messages when device offline.

Space communication networks rely on delayed transmission.

Remote scientific stations buffer data until connection available.

---

## Reflection

Store-and-forward networking demonstrates that reliability can be achieved without constant connectivity.

Instead of requiring stable links, systems adapt by preserving information locally.

Queue management becomes an essential component of distributed systems.

Persistence ensures important messages are not lost during temporary network disruptions.

Delay-tolerant architecture enables communication in extreme environments.

---

## Conclusion

Store-and-forward networking introduces resilience through persistence.

Nodes buffer messages during link failure and retry delivery automatically.

Exponential backoff prevents network congestion.

Priority queues allow critical messages to be delivered first.

Persistent storage ensures reliability even across system restarts.

Understanding store-and-forward prepares students for real-world distributed communication challenges.

---

Status: Completed

Week: 7

Topic: Store-and-Forward Networking

Course: Network Programming