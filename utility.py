#!/usr/bin/python3
import time, socket
def send_slowly (s, bb):
    for i in range(len(bb)):
        b = bb[i : i + 1]
        time.sleep(1)
        s.sendall(b)