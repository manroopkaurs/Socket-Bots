import socket
import threading
import sys

# Finding the host and port
if len(sys.argv) != 2:
    print("Failed to connect. Try again")
    exit()

HOST = "localhost"
PORT = int(sys.argv[1])

# Starting the server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
names = []


# Message sent out to client in chatroom
def broadcast(message):
    for client in clients:
        client.send(message)

# Handling messages from clients
def handle(client):
    while True:
        try:
            #Broadcasting messages
            message = client.recv(1024)
            broadcast(message)

        except:
            #Removing and closing clients
            index = clients.index(client)
            clients.remove(client)
            client.close()

            name = names[index]
            broadcast('{} left the chat'.format(name).encode('utf-8'))
            names.remove(name)
            break

# Receiving / Listening function for clients message
def receive():
    while True:
        # Accept connection - prints out the clients name on the server terminal
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Requests and stores name from client.py
        client.send(bytes('in_client_name'.encode('utf-8')))
        name = client.recv(1024).decode('utf-8')
        names.append(name)
        clients.append(client)

        # Message printed out on server.py terminal when client is connected
        print(f"Welcome to the bot {name}")
        # Broadcast the client_name on the client.py terminal
        broadcast(f"Welcome to the chat {name}! You are now connected to the server.".encode('utf-8'))

        # Start handling thread for client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()