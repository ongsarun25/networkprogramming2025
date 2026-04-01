# Week 3 – UDP Broadcast Experiments

This document records experiments performed to understand UDP broadcast behavior and its limitations within a LAN environment.

Broadcast communication differs significantly from unicast communication. Instead of targeting a specific receiver, broadcast sends data to all nodes in the broadcast domain.

This makes broadcast useful for discovery protocols, but also introduces inefficiency and potential network congestion.

---

## Experiment 1 – Basic Broadcast Reception

### Goal

Verify that multiple listeners can receive the same broadcast message simultaneously.

### Method

Start multiple listeners:

Terminal 1
python listener.py

Terminal 2
python listener.py

Terminal 3
python listener.py

Then start broadcaster:

Terminal 4
python broadcaster.py

### Result

All listeners received the same message:

[LISTENER] From ('192.168.x.x', 52344): DISCOVERY: Who is online?
[LISTENER] From ('192.168.x.x', 52344): DISCOVERY: Who is online?
[LISTENER] From ('192.168.x.x', 52344): DISCOVERY: Who is online?

### Observation

One broadcast message can reach multiple receivers simultaneously.

No additional configuration was required on the listeners besides binding to the correct port.

### Insight

Broadcast allows one-to-many communication without maintaining connection state.

This is efficient for discovery scenarios but inefficient for large networks.

---

## Experiment 2 – Broadcast Without Active Listener

### Goal

Demonstrate that UDP does not store messages if no receiver is listening.

### Method

Run broadcaster before starting any listeners:

Terminal 1
python broadcaster.py

Wait 3 seconds.

Terminal 2
python listener.py

### Result

Listener did not receive any message.

### Observation

UDP does not queue messages for future receivers.

Messages are delivered only to processes actively listening at the time of transmission.

### Insight

Broadcast does not provide persistence.

Applications must handle late joiners explicitly if required.

---

## Experiment 3 – Reply to Broadcast (Discovery Pattern)

### Goal

Implement discovery mechanism where listeners respond to broadcaster.

### Method

Modify listener to reply:

sock.sendto("ONLINE".encode(), addr)

Modify broadcaster to collect replies.

### Result

Broadcaster output:

[BROADCASTER] Discovery sent
[BROADCASTER] Reply from ('192.168.x.101', 7000)
[BROADCASTER] Reply from ('192.168.x.102', 7000)

### Observation

Broadcast can be used to discover active devices on a LAN.

Each listener replies using unicast communication.

### Insight

Broadcast is commonly used for service discovery protocols.

Examples include DHCP and mDNS.

---

## Experiment 4 – Periodic Broadcast Traffic

### Goal

Observe behavior when broadcasts are sent repeatedly.

### Method

Broadcaster sends message every 5 seconds:

while True:
    send broadcast
    sleep(5)

### Result

Listeners continuously receive messages:

DISCOVERY 10:01:01
DISCOVERY 10:01:06
DISCOVERY 10:01:11

### Observation

Frequent broadcast messages create continuous network traffic.

All nodes must process each message.

### Insight

Broadcast traffic should be limited.

Excessive broadcast usage can degrade network performance.

---

## Experiment 5 – Subnet Broadcast Address

### Goal

Compare 255.255.255.255 with subnet-specific broadcast.

### Method

Modify config:

BROADCAST_IP = "192.168.1.255"

### Result

Broadcast still reaches all nodes within subnet.

Does not reach devices outside subnet.

### Observation

Broadcast scope depends on subnet configuration.

Routers typically block broadcast traffic.

### Insight

Broadcast is restricted to local network boundaries.

This improves containment but limits scalability.

---

## Broadcast Behavior Summary

| Property | Behavior |
|---------|----------|
| Connection required | No |
| Delivery guarantee | No |
| Ordering guarantee | No |
| Network scope | LAN only |
| Receiver filtering | Not possible |
| Resource efficiency | Low |
| Discovery suitability | High |

---

## Comparison with Previous Weeks

### Week 1 – TCP Unicast

Client communicates with specific server.

Connection required.

Reliable communication.

---

### Week 2 – UDP Unicast

Client communicates with specific server.

No connection required.

No delivery guarantee.

---

### Week 3 – UDP Broadcast

Sender communicates with all nodes on LAN.

No connection required.

No delivery guarantee.

Receivers decide whether to respond.

---

## Real World Protocol Examples

Broadcast is used in several important protocols:

DHCP

Client sends broadcast to find DHCP server.

ARP

Device broadcasts request to find MAC address associated with IP.

mDNS

Used for local hostname resolution.

Service discovery systems.

---

## Limitations of Broadcast

Broadcast is intentionally restricted in modern networks.

Reasons:

Network congestion risk

Security concerns

Unnecessary processing overhead

Lack of selectivity

Poor scalability

For large scale systems, multicast or directory-based discovery is preferred.

---

## Reflection

Broadcast communication demonstrates that not all network communication is targeted.

Sometimes systems must discover peers dynamically.

Broadcast provides a simple discovery mechanism but must be used carefully.

This experiment highlights tradeoffs between convenience and efficiency.

Understanding broadcast scope helps prevent unintended network load and improves protocol design decisions.

---

## Conclusion

UDP broadcast enables one-to-many communication within a local network.

It is useful for discovery but should be applied sparingly.

Designers must consider network size, traffic frequency, and resource usage when implementing broadcast-based solutions.

Broadcast is a primitive but important tool in distributed systems.