import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',5555))
s.listen()

while True:
    client,address = s.accept()
    print(f"connected {address}")
    client.send("you are connected".encode())
    client.close()