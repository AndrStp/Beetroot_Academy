"""
Task 2

Echo server with threading
Create a socket echo server which handles each connection in a separate Thread
"""

import socket
import threading


class ThreadedServer(object):
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 65432
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        print('Server\'s listening...')
        while True:
            client, address = self.sock.accept()
            client.settimeout(10)
            threading.Thread(target=self.listenToClient, args=(client,address)).start()

    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size)
                if data:
                    # Set the response to echo back the recieved data 
                    response = data
                    client.send(response)
                else:
                    raise Exception('Client disconnected')
            except:
                client.close()
                return False


if __name__ == "__main__":
    ThreadedServer().listen()