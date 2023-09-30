import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)as s:
    s.bind((HOST,PORT))
    s.listen(10)

    # a new socket pobject different from the first one for receiving
    conn,addr = s.accept()
    with conn:
        print(f"connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
