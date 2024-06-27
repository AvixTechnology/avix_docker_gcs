import socket

HOST = '192.168.0.66'  # Host IP address
PORT = 12345  # The same port your server is listening on

def run_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f'Connected to server at {HOST}:{PORT}')
        message = 'Hello, server!'
        s.sendall(message.encode('utf-8'))
        data = s.recv(1024)
        print(f'Received from server: {data.decode("utf-8")}')

if __name__ == "__main__":
    run_client()
