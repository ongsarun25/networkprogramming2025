# Week 6 – MANET (Mobile Ad-Hoc Network) Experiments

This document records experiments performed to understand how decentralized mobile nodes communicate without fixed infrastructure.

A Mobile Ad-Hoc Network (MANET) allows nodes to dynamically form a network, discover neighbors, and forward messages cooperatively. Each node behaves as both a host and a router.

The main goal is to simulate real-world situations where traditional network infrastructure is unavailable, such as disaster recovery, battlefield communication, or remote sensing.

---

## Experiment 1 – Basic Message Propagation

### Goal

Verify that nodes can forward messages to neighbors using TTL (Time-To-Live).

### Method

Run three nodes with the following configuration:

Node 7000:
NEIGHBORS = [7001]

Node 7001:
NEIGHBORS = [7000, 7002]

Node 7002:
NEIGHBORS = [7001]

Set:

FORWARD_PROBABILITY = 1.0
TTL = 3

Run nodes in three terminals.

### Result

Message from node 7000 propagates:

7000 → 7001 → 7002

Console output example:

[NODE 7000] Forwarding to 7001: Hello (TTL=3)
[NODE 7001] Received: Hello (TTL=3)
[NODE 7001] Forwarding to 7002: Hello (TTL=2)
[NODE 7002] Received: Hello (TTL=2)

### Observation

Messages successfully travel across multiple hops.

TTL decreases at each hop.

### Insight

TTL prevents infinite routing loops and controls network propagation distance.

---

## Experiment 2 – Probabilistic Forwarding Behavior

### Goal

Observe how probabilistic forwarding affects delivery reliability.

### Method

Set:

FORWARD_PROBABILITY = 0.5
TTL = 3

Send multiple messages from node 7000.

### Result

Some messages reach node 7002 while others do not.

Example:

Message 1 → delivered
Message 2 → dropped at intermediate node
Message 3 → delivered
Message 4 → dropped

### Observation

Lower forwarding probability introduces packet loss.

Delivery success becomes non-deterministic.

### Insight

Probabilistic routing reduces network congestion but decreases reliability.

Trade-off exists between redundancy and efficiency.

---

## Experiment 3 – TTL Limitation Effect

### Goal

Confirm TTL limits propagation depth.

### Method

Set:

TTL = 1

Topology:

7000 → 7001 → 7002

### Result

Message only reaches node 7001.

Node 7002 never receives the message.

### Observation

TTL=1 allows only one hop.

### Insight

TTL defines the maximum number of network hops.

Low TTL reduces traffic but limits reachability.

---

## Experiment 4 – Unreachable Neighbor Detection

### Goal

Observe behavior when neighbor node is offline.

### Method

Set:

Node 7000:
NEIGHBORS = [7999]

Port 7999 does not exist.

### Result

Console output:

[NODE 7000] Neighbor 7999 unreachable

### Observation

System handles connection failure gracefully.

No crash occurs.

### Insight

Fault tolerance is essential in decentralized systems.

Nodes must expect intermittent connectivity.

---

## Experiment 5 – Duplicate Message Detection

### Goal

Prevent repeated processing of identical messages.

### Method

Attach message ID to each packet:

message_id = uuid.uuid4()

Maintain cache of previously seen message IDs.

If duplicate message detected, drop packet.

### Result

Duplicate messages are ignored:

[NODE 7001] Duplicate dropped: 81f3-92ad

### Observation

Flooding protocols can generate redundant traffic.

Duplicate detection improves efficiency.

### Insight

Real routing protocols maintain packet history to avoid loops.

---

## Experiment 6 – Adaptive Forwarding Probability

### Goal

Adjust forwarding probability dynamically based on network density.

### Method

Define adaptive function:

Few neighbors → high probability
Many neighbors → lower probability

Example logic:

1 neighbor → probability 1.0
3 neighbors → probability 0.7
5 neighbors → probability 0.5

### Result

Sparse networks maintain connectivity.

Dense networks reduce redundant transmissions.

### Observation

Dynamic adaptation balances reliability and efficiency.

### Insight

Real MANET protocols optimize routing dynamically.

---

## Experiment 7 – Message Path Tracking

### Goal

Track route taken by each message.

### Method

Append node ID to packet path:

Path example:

7000 → 7001 → 7002

Console output:

[NODE 7002] Path: 7000 → 7001 → 7002

### Result

Routing path becomes visible.

### Observation

Helps identify network topology.

Useful for debugging routing errors.

### Insight

Path tracking provides transparency in decentralized routing.

---

## Experiment 8 – Gossip Protocol Simulation

### Goal

Reduce network congestion using selective forwarding.

### Method

Instead of forwarding to all neighbors, forward to subset:

fanout = 50% of neighbors

Example:

Neighbors = [7001,7002,7003,7004]

Forward to only 2 randomly selected nodes.

### Result

Lower network traffic.

Message still propagates through network probabilistically.

### Observation

Gossip protocols reduce overhead.

Delivery latency may increase slightly.

### Insight

Gossip-based routing is widely used in distributed databases.

---

## Experiment 9 – Dynamic Neighbor Discovery

### Goal

Allow nodes to automatically discover available neighbors.

### Method

Scan nearby port range periodically.

Add reachable ports to neighbor table.

Update every 5 seconds.

### Result

Nodes automatically detect active neighbors.

Neighbor table updates dynamically.

### Observation

Topology changes without manual configuration.

### Insight

Real MANET nodes continuously monitor link availability.

---

## Experiment 10 – Heartbeat Monitoring

### Goal

Detect inactive nodes automatically.

### Method

Send periodic heartbeat check to neighbors.

Remove neighbors that fail to respond.

### Result

Inactive nodes removed from routing table.

Network adapts automatically.

### Observation

Neighbor table becomes self-healing.

### Insight

Heartbeat protocols maintain network stability.

---

## MANET Behavior Summary

| Feature | Behavior |
|--------|---------|
| Infrastructure | None |
| Routing | Cooperative |
| Reliability | Probabilistic |
| Topology | Dynamic |
| Fault tolerance | Required |
| Packet delivery | Not guaranteed |
| Loop prevention | TTL |
| Redundancy control | Probability |

---

## Comparison with Previous Weeks

### Week 5 – Peer-to-Peer

Peers connect directly to known nodes.

Connections are stable.

Topology remains static.

### Week 6 – MANET

Nodes forward messages dynamically.

Connections may change frequently.

Topology evolves continuously.

Nodes behave as routers.

---

## Real-World Applications

MANET architectures are widely used in environments where infrastructure is unavailable:

Disaster recovery communication

Military tactical networks

Drone swarm coordination

Environmental sensor networks

Remote scientific expeditions

Emergency response teams

Autonomous vehicle coordination

Internet-of-Things mesh networks

---

## Reflection

MANET systems operate under uncertainty.

Nodes must make local decisions without global knowledge.

Probabilistic forwarding increases resilience in unstable environments.

TTL ensures network stability by preventing infinite loops.

Dynamic neighbor discovery enables adaptive network topology.

MANET principles are foundational for modern distributed and resilient communication systems.

---

## Conclusion

MANET simulation demonstrates decentralized communication without fixed infrastructure.

Each node contributes to routing and delivery.

Probabilistic forwarding balances redundancy and efficiency.

TTL prevents infinite propagation loops.

Dynamic topology reflects real-world mobile networks.

Understanding MANET behavior prepares students for designing resilient distributed systems.

---

Status: Completed

Week: 6

Topic: Mobile Ad-Hoc Network Simulation

Next Topic: Store-and-Forward Networking