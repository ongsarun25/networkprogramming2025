# config.py

HOST = "127.0.0.1"

# change this per node instance
BASE_PORT = 9000

# peers in experiment
PEER_PORTS = [9001, 9002]

BUFFER_SIZE = 1024

# forwarding decision threshold
FORWARD_THRESHOLD = 0.5

# how often forwarding logic runs
UPDATE_INTERVAL = 5

# message lifetime (seconds)
MESSAGE_TTL = 30