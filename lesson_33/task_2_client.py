"""
Task 2

Extend the echo server, which returns to client the data, encrypted 
using the Caesar cipher algorithm by a specific key obtained from the client.
"""


import socket
import pickle


HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

def connect_to_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        message = input('Enter your message here: ')
        s.sendall(message.encode('utf-8'))
        encrypted_message, key = pickle.loads(s.recv(1024))

        if decrypt(encrypted_message) != message:
            raise Exception('Failed to encrypt')

        print('Encrypted message:', encrypted_message)
        print('Key:', key)


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
    connect_to_server()