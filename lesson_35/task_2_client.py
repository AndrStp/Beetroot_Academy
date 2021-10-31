import socket


def connect_to_server():
    HOST = '127.0.0.1'
    PORT = 65432
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT)) # Establish connection with server.
        while True:
            message = input('Enter your name here: ')
            if message == '/exit':
                break
            s.sendall(message.encode('utf-8'))
            recv_message = s.recv(1024).decode('utf-8')
            print('Received message:', recv_message)


if __name__ == '__main__':
    connect_to_server()