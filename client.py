import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('73.210.125.214', 8000))

msg = s.recv(1024)
print(msg.decode('utf-8'))
inp=''
while inp != 'STOP':
    inp = input('What would you like to tell the server Owner')
    s.send(bytes(inp, "utf-8"))
    msg = s.recv(1024)
    print(msg.decode('utf-8'))