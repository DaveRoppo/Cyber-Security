#Creating a TCP server

#Import socket library
from http import server
import socket
#family:AF_INET for IPv4 - type:SOCK_STREAM for TCP
serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#Define host variable, grab the server IP address with gethostbyname()
host = socket.gethostname()
#Define port variable for the listening port 
port = 444
#Bind host and port to serversocket
serversocket.bind((host, port))
#Listen for TCP connections 
serversocket.listen(1)
#While loop for initializing the connection
while True:
    clientsocket, address = serversocket.accept()

    print("Recieved connection from " % str(address))
    #Message to send to client following a successful connection
    message = "Thank you for connecting to the server" + "\r\n"
    
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()

