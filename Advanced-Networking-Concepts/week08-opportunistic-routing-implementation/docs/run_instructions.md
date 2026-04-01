# Run Instructions

This lab simulates opportunistic routing behavior.

Multiple nodes maintain probability tables indicating how likely each peer can deliver a message.

Messages are forwarded only when probability exceeds threshold.

---

## Step 1

open 3 terminals

---

## Step 2

edit config.py in each folder copy

Example:

Node A:
BASE_PORT = 9000

Node B:
BASE_PORT = 9001

Node C:
BASE_PORT = 9002

---

## Step 3

run nodes

python node.py

---

## Step 4

observe output

nodes will:

store messages if peers unavailable
forward opportunistically when probability increases
expire messages after TTL

---

## Expected behavior

probability table changes over time

messages forwarded when good encounter occurs

demonstrates probabilistic routing logic