import socket
from Rsa import *
from Rc4 import *

def start_client():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the server's address and port
    server_address = ('localhost', 5000)
    client_socket.connect(server_address)


     # Sending the first part of the public key
    p=generate_large_prime()
    q=generate_large_prime()
    n=p*q
    nSend=n
    print ("the first part of the public key is ",nSend)
    nStr=str(nSend)
    client_socket.send(nStr.encode())

        # Sending the phi_n
    phi_n=(q-1)*(p-1)
    phi_nStr=str(phi_n)
    print ("the phi_n is ",phi_n)
    client_socket.send(phi_nStr.encode())
        # Sending the second part of the public key
    e = get_second_part_public_key(phi_n)
    eSend=e
    print ("the second part of the public key is ",eSend)
    eStr=str(eSend)
    client_socket.send(eStr.encode())


    # Sending the key of Rc4 by Rsa 
    keyRc4 = input("Enter a key of the Rc4 algorithm to send to the server: ")
    keyRc4EncryptedArrayInt= encrypt(keyRc4,e,n)
    keyRc4cipherText=arrayIntToFullText(keyRc4EncryptedArrayInt)
    print ("the cipher int is ",convertToInt(keyRc4cipherText))
    print("the key Rc4 Encrypted cipher text is ",keyRc4cipherText)
    client_socket.send(keyRc4cipherText.encode())



    # Continuously send and receive messages to and from the server
    while True:

        # Receive a response from the server
        response = client_socket.recv(1024)

        encRc4=response.decode()
        plainTextRc4=convertMessageRc4(keyRc4,encRc4)

        # Print the response from the server
        print(f"Server says: ",plainTextRc4)

        response = input("Enter a message to send to the server: ")
        sendRc4=convertMessageRc4(keyRc4,response) 
        client_socket.send(sendRc4.encode())

    # Close the client socket
    client_socket.close()

if __name__ == '__main__':
    start_client()
