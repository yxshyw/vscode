import socket

HOST = '127.0.0.1'    # The remote host
PORT = 9203              # The same port as used by the server
d = '7d6e2c5f3edb2e7b000103004e018220404c4d474645314738384431303035353534545441393637564735353534343833303032343037353935353534383838363036313530313130303031303535353404754d11460d0c554f'
d = bytes.fromhex(d)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(s.connect((HOST, PORT)))
    print(s.sendall(d))
    data = s.recv(1024)
print(data.hex())