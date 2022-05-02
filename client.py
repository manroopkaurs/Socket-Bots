import socket
import sys
import threading
import bot1, bot2, bot3, bot4
import time

# Finding the host and port
if len(sys.argv) != 2:
    print("Failed to connect. Try again")
    exit()

HOST = "localhost"
PORT = int(sys.argv[1])

# Starting the client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# For client to type inn their name
name = input('Enter your name: ')

# Function for the messages received from client
def receive():
    while True:
        # Connection is right = message from client will be handled
        try:
            msg = client.recv(1024).decode('utf-8')
            if msg == 'in_client_name':
                client.send(name.encode('utf-8'))
            else:
                print(msg)
        # If connection fails, client is closed and has to try again.
        except:
            print("Connection failed, try again!")
            client.close()
            break

# Function for the client input, as well as the output from the bots
def accept():
    while True:
        try:
            time.sleep(1) # Adding some time between broadcast and input for client
            client_input = input(f'{name}: ') # The clients input
            time.sleep(1) # Adding some sleep time between the bots, so that the print out in terminal will go a bit slower and easier to read
            print('Meghan: ' + bot1.find_response(client_msg= client_input)) # The bots look for an answer based on the clients input in terminal
            time.sleep(1)
            print('Alice: ' + bot2.find_response(client_msg= client_input))
            time.sleep(1)
            print('Valerie: ' + bot3.find_response(client_msg= client_input))
            time.sleep(1)
            print('Samantha: ' + bot4.find_response(client_msg= client_input))

        except:
            print("Chatbot is closed")
            client.close()


# Start thread for receive() and accept()
receive_thread = threading.Thread(target=receive)
receive_thread.start()

accept_thread = threading.Thread(target=accept)
accept_thread.start()

