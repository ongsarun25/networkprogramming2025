# Run Instructions

Bio-inspired routing simulates how ants discover optimal paths.

Paths that succeed receive reinforcement.

Paths that fail decay over time.

Eventually the network prefers efficient routes.

---

STEP 1

open 3 terminals

---

STEP 2

edit config.py

example:

node A
BASE_PORT = 10000

node B
BASE_PORT = 10001

node C
BASE_PORT = 10002

---

STEP 3

run nodes

python node.py

---

STEP 4

observe pheromone table

successful routes increase pheromone

unused routes decay

network adapts automatically

---

Expected Behavior

network gradually prefers certain peers

messages follow reinforced paths

routing decisions evolve dynamically