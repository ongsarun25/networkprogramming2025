# Week 4 – UDP Multicast Experiments

This document records experiments performed to understand multicast communication using UDP.

Multicast introduces selective message delivery. Instead of sending data to a specific receiver (unicast) or all receivers (broadcast), multicast sends data to a defined group.

Only receivers that explicitly join the multicast group will receive the message.

Multicast is commonly used in systems that require efficient distribution of the same data to multiple participants.

---

## Experiment 1 – Basic Multicast Reception

### Goal

Verify that receivers must join the multicast group before receiving messages.

### Method

Run receiver:

python receiver.py

Run sender:

python sender.py

### Result

Receiver output:

[RECEIVER] Joined 224.1.1.1:8000
[RECEIVER] ('192.168.x.x', 51000) -> MULTICAST: Hello subscribers

### Observation

Receiver successfully obtained message only after joining multicast group.

Without joining the group, no data is delivered.

### Insight

Multicast communication requires explicit membership registration using IP_ADD_MEMBERSHIP.

Kernel filters packets so only subscribed processes receive them.

---

## Experiment 2 – Multiple Receivers in Same Group

### Goal

Verify that multiple subscribers receive the same multicast message.

### Method

Start multiple receivers:

Terminal 1
python receiver.py

Terminal 2
python receiver.py

Terminal 3
python receiver.py

Start sender:

Terminal 4
python sender.py

### Result

All receivers display the same message.

### Observation

Sender transmits a single datagram.

Network duplicates packet efficiently for all subscribed members.

### Insight

Multicast reduces redundant traffic compared to sending separate unicast packets.

Efficient for streaming and distributed updates.

---

## Experiment 3 – Non-Member Does Not Receive Data

### Goal

Demonstrate that receivers who do not join group will not receive packets.

### Method

Modify receiver by removing:

sock.setsockopt(IPPROTO_IP, IP_ADD_MEMBERSHIP, mreq)

Run modified receiver.

Run sender.

### Result

Modified receiver does not receive any message.

### Observation

Binding to the port alone is insufficient.

Group membership is required.

### Insight

Multicast supports selective listening.

Network avoids sending unnecessary traffic to uninterested nodes.

---

## Experiment 4 – TTL Scope Control

### Goal

Understand effect of TTL on multicast scope.

### Method

Modify config.py:

TTL = 1

Run sender and receiver.

Then modify:

TTL = 5

Observe behavior.

### Result

TTL=1 limits multicast to local network.

Increasing TTL allows multicast to travel further (if routers permit).

### Observation

TTL controls how far multicast packets propagate.

Most local testing environments only allow TTL=1.

### Insight

TTL prevents accidental global multicast flooding.

Scope control improves network safety.

---

## Experiment 5 – Periodic Multicast Messages

### Goal

Simulate real-time data streaming.

### Method

Modify sender to transmit repeatedly:

while True:
    send multicast
    sleep(2)

### Result

Receiver continuously prints messages:

Update #1 10:01:02
Update #2 10:01:04
Update #3 10:01:06

### Observation

Multicast efficiently distributes repeated data streams.

Single sender can serve many receivers simultaneously.

### Insight

Multicast useful for:

live video streaming

financial data feeds

multiplayer game state updates

sensor telemetry

---

## Multicast Characteristics Summary

| Property | Behavior |
|---------|----------|
| Requires connection | No |
| Requires group membership | Yes |
| Delivery guarantee | No |
| Ordering guarantee | No |
| Receiver filtering | Yes |
| Network efficiency | High |
| Typical usage | Streaming and distributed updates |

---

## Comparison with Previous Weeks

### Week 2 – UDP Unicast

One sender communicates with one receiver.

Each receiver requires separate transmission.

Traffic increases linearly with number of receivers.

---

### Week 3 – UDP Broadcast

Sender transmits to all nodes on LAN.

Receivers cannot opt out.

Network resources consumed even by uninterested nodes.

---

### Week 4 – UDP Multicast

Sender transmits once to multicast group.

Only subscribed receivers obtain data.

Network usage optimized.

---

## Real-World Multicast Examples

Multicast is widely used in modern distributed systems:

IPTV broadcasting

Live event streaming

Stock market data feeds

Real-time telemetry systems

Online gaming updates

Video conferencing systems

---

## Limitations of Multicast

Despite advantages, multicast adoption is limited in public internet environments.

Reasons include:

Router configuration complexity

Security concerns

Limited ISP support

Difficulty managing group membership

Many applications simulate multicast using application-layer protocols instead.

---

## Reflection

Multicast introduces the concept of selective participation in communication.

Receivers actively choose which data streams to receive.

This allows efficient scaling of distributed systems.

Compared to broadcast, multicast provides better resource utilization.

Compared to unicast, multicast reduces redundant transmissions.

Understanding multicast prepares students for real-time distributed architectures.

---

## Conclusion

UDP multicast enables scalable one-to-many communication with selective delivery.

Group membership provides control over which nodes receive data.

TTL ensures communication remains within intended network scope.

Multicast balances flexibility, efficiency, and control.

It is an essential concept in modern network system design.