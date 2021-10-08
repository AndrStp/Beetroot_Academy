"""
Task 1

During the lesson, we have created a server and client, which use TCP/IP protocol
for communication via sockets. In this task, you have to create a server and 
client, which will use user datagram protocol (UDP) for communication.
"""

import socket


HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    data, addr = s.recvfrom(4096)
    if data:
        print('Connected by', addr)
        s.sendto(data, addr)

