import socket
from Rsa import *
from Rc4 import *

def start_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_address = ('localhost', 5000)
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)
    print("Server is listening for incoming connections...")

    # Wait for a client connection
    client_socket, client_address = server_socket.accept()
    print(f"New client connected: {client_address}")

    data = client_socket.recv(1024)
    # Receiving the first part of the public key
    nStr=data.decode()
    nRec=int(nStr)
    print ("the firt part of the public key ",nRec)

    data = client_socket.recv(1024)
    # Receiving the phi_n
    phi_nStr=data.decode()
    phi_nRec=int(phi_nStr)
    print ("the phi_n is ",phi_nRec)
    # Receiving the second part of the public key
    data = client_socket.recv(1024)
    eStr=data.decode()
    eRec=int(eStr)
    print ("the firt part of the public key ",eRec)


    # receiving the key of Rc4 cipher text
    data = client_socket.recv(1024)
    keyRc4cipherText=data.decode()
    print("the cipher text from the client is ",keyRc4cipherText)
    cipherInt=convertToInt(keyRc4cipherText)
    print("the cipher int is ",cipherInt)
    dServer=inverse_modulaire(eRec,phi_nRec)
    keyRc4=decrypt(cipherInt,dServer,nRec)
    print("the plain text from the client is ",keyRc4)
    



    # Continuously receive and send messages to the client
    while True:
        # Send a response to the client
        response = input("Enter a message to send to the client: ")
        encRc4=convertMessageRc4(keyRc4,response)
        client_socket.send(encRc4.encode())
        # Receive data from the client
        data = client_socket.recv(1024)
        if not data:
            break
        receivRc4=data.decode()
        message=convertMessageRc4(keyRc4,receivRc4)
        print(f"Received message from {client_address}: ",message)
        



    # Close the client connection
    client_socket.close()
    print(f"Connection with {client_address} closed.")

if __name__ == '__main__':
    start_server()
