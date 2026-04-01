# Week 1 Extensions – TCP Client–Server Experiments

This document records my additional exploration beyond the base lab provided by the instructor.

The original lab demonstrates the minimal TCP client–server interaction pattern.  
My goal in these extensions is to deepen understanding of:

- TCP connection lifecycle
- blocking vs controlled behavior
- session-based communication
- server robustness
- concurrent client simulation

All original files remain unchanged.  
All experiments are implemented as additional modules.

---

# Overview of Added Experiments

| File | Purpose | Concept Practiced |
|------|--------|------------------|
| server_loop.py | persistent server | connection lifecycle |
| client_multi_message.py | session communication | TCP state |
| server_with_timeout.py | prevent infinite blocking | defensive networking |
| server_logger.py | logging system | observability |
| stress_test_client.py | simulate concurrent clients | scalability awareness |

---

# Experiment 1 – Persistent Server

### Problem

The base lab server handles only one client connection and then exits:

```python
conn, addr = server_socket.accept()
...
conn.close()
server_socket.close()