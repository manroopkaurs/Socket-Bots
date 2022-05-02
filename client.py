import socket
import sys
import threading
import bot1, bot2, bot3, bot4
import time

if len(sys.argv) != 2:
    print("Failed to connect. Try again")
    exit()

HOST = "localhost"
PORT = int(sys.argv[1])

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

name = input('Enter your name: ')

def recieve():
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            if msg == 'in_client_name':
                client.send(name.encode('utf-8'))
            else:
                print(msg)
        except:
            print("Connection failed, try again!")
            client.close()
            break


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



receive_thread = threading.Thread(target=recieve)
receive_thread.start()

accept_thread = threading.Thread(target=accept)
accept_thread.start()

