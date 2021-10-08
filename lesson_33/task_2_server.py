"""
Task 2

Extend the echo server, which returns to client the data, encrypted 
using the Caesar cipher algorithm by a specific key obtained from the client.
"""

import socket
import pickle
from random import randint


HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024).decode('utf-8')
                if not data: break
                
                key = randint(1, 25)
                encrypted = encrypt(data)
                conn.sendall(pickle.dumps((encrypted, key)))


def encrypt(message: str, key: int = 1) -> str:
    """Encrypts the message by shifting the ASCII 
    code by the given key (1 by default)"""
    encrypted = []
    for char in message:
        if char.isalpha():
            if char.isupper():
                char_code = ((ord(char) + key - 65) % 26 + 65)
            elif char.islower():
                char_code = ((ord(char) + key - 97) % 26 + 97)
            encrypted.append(chr(char_code))
        else:
            encrypted.append(char)
            
    return ''.join(encrypted)


def decrypt(message: str, key: int = 1) -> str:
    """Decrypts the message using the key"""
    decrypted = []
    for char in message:
        if char.isalpha():
            if char.isupper():
                char_code = ((ord(char) - key - 65) % 26 + 65)
            elif char.islower():
                char_code = ((ord(char) - key - 97) % 26 + 97)
            decrypted.append(chr(char_code))
        else:
            decrypted.append(char)

    return ''.join(decrypted)


if __name__ == '__main__':
    run_server()