from socket import *

s = socket(AF_INET, SOCK_STREAM)
print("Socket successfully created")

host = '127.0.0.1'
port = 8000

s.bind((host, port))

s.listen(5)
print("Socket is listening")

# Accept connections from client
while True:
    c, addr = s.accept()
    print('Get connection from', addr)
    
    # Receive data from client
    RecevedMessage = b''
    while True:
        message = c.recv(1024)
        if not message:
            break
        RecevedMessage += message
    print("Received message:", RecevedMessage.decode('utf-8'))
    
    # Send acknowledgment to client
    m=input("the send message is :")
    c.send(m.encode('utf-8'))
    c.close()
