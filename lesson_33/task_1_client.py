"""
Task 1

During the lesson, we have created a server and client, which use TCP/IP protocol
for communication via sockets. In this task, you have to create a server and 
client, which will use user datagram protocol (UDP) for communication.
"""

"""
Task 2

Extend the echo server, which returns to client the data, encrypted 
using the Caesar cipher algorithm by a specific key obtained from the client.
"""

import socket


HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect((HOST, PORT))
    sent_message = input('Enter your message here: ')
    s.sendall(sent_message.encode('utf-8'))
    recv_message = s.recv(4096)

    print('Recieved:', recv_message)