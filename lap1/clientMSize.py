from socket import *

s = socket(AF_INET, SOCK_STREAM)

host = '127.0.0.1'
port = 8000

s.connect((host, port))
#sending
M=input("the sent message is:")
s.send(M.encode('utf-8'))

# Receive from the server
resevedMessage = b''
while True:
    message= s.recv(1024)
    if not message:
        break
    resevedMessage += message
print("Server response:", resevedMessage.decode('utf-8'))

s.close()
