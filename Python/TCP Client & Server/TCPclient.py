#import socket library
import socket
#Create socket object
clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname()

port = 444

clientsocket.connect((host, port))
#Set max amount of data 
message = clientsocket.recv(1024)

#Close the connection
clientsocket.close()
#decode ascii
print(message.decode('ascii'))


