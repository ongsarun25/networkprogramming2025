# WEEK 8 — Opportunistic Routing (Basic)

## Concept

Traditional routing assumes stable paths.

Opportunistic routing assumes:

paths appear unpredictably.

Nodes forward messages only when a good forwarding opportunity appears.

---

## Key Idea

Each node maintains probability of successful delivery through neighbors.

Messages are forwarded only when:

delivery_probability > threshold

---

## Features implemented

delivery probability table

message queue

TTL expiration

dynamic probability simulation

opportunistic forwarding decision

---

## Architecture

node = router + probability estimator

forwarding decision based on:

historical encounter likelihood

---

## How it behaves

messages may wait in queue

when probability increases:

node forwards message

network adapts dynamically

---

## Relationship to real networks

Delay Tolerant Networks (DTN)

wildlife tracking sensors

space communication systems

disaster recovery networks

mobile mesh networks