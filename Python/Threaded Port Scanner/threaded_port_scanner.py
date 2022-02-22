# Import Queue to make sure ports are only scanned once
from queue import Queue
# Import socket to make connection attempts 
import socket 
# Import threading to run multiple scans at the same time
import threading

# Define global variables to be used throughout functions
# tgt = input IP-addr or domain of the host that will be scanned
tgt = "xxx.xxx.xxx.xxx"
# queue = empty queue that will be filled with ports to be scanned
queue = Queue()
# open_ports = empty list to store open port numbers
open_ports = []

# Define portscan function 
# Add Try, Except (if true, port open) (if false, port closed)
def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((tgt, port))
        return True
    except:
        return False

# Define function for the ports to be scanned
def get_ports(mode):
    if mode == 1:
        # Scan the 1023 standardized ports 
        for port in range(1,1024):
            queue.put(port)
    elif mode == 2:
        # Scan all reserve ports as well
        for port in range(1, 49152):
            queue.put(port)
    elif mode == 3:
        # Scan most important ports
        ports = [20, 21, 22, 23, 25, 53, 80, 110, 443]
        for port in ports:
            queue.put(port)
    elif mode ==4:
        # Choose ports manually
        ports = input("Enter the ports you want to scan (seperate each port by blank space): ")
        ports = ports.split()
        # Map integer data type to every element of list 
        ports = list(map(int, ports))
        for port in ports:
            queue.put(port)

# Define function to grab port nums from queue, scan them, and print results
def grab_n_scan():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} is open.".format(port))
            open_ports.append(port)
        
# Define main function to create, start, and manage threads
def multithread(threads, mode):
    get_ports(mode)
    thread_list = []
    for t in range(threads):
        thread = threading.Thread(target=grab_n_scan)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()
    print("Open ports: ", open_ports)

# Choose numbers of threads, choose mode 
multithread(100,2)
