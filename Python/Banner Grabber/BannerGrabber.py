#Import socket library
import socket

def banner(ip, port):
    s = socket.socket()
    s.connect((ip, int(port)))
    print(str(s.recv(1024)).strip("b"))

def main():
    ip = input("Please enter the IP address: ")
    port = str(input("Please enter the port number: "))
    banner(ip, port)

main()
