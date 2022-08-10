#import nmap module (install with pip)
import nmap
#Create scanner variable, used to call nmap class
scanner = nmap.PortScanner()
#Prompt user
print("Welcome, this is an nmap automation tool")
print("<--------------------------------------->")

ip_addr = input("Please enter the IP address you want to scan: ")
print("The IP you entered is:", ip_addr)
type(ip_addr)

#Create variable, ask user what type of scan to execute
resp = input(""" \nPlease enter the type of scan you would like to run
                    1) SYN ACK Scan
                    2) UDP Scan
                    3) Comprehensive Scan\n""")

print("You have selected to run option: ", resp)

if resp == "1":
    #Print nmap version
    print("Nmap Version: ", scanner.nmap_version())
    #Define type of scan
    scanner.scan(ip_addr, "1-1024", "-v -sS")
    #Print scan info
    print(scanner.scaninfo())
    #Print status of IP address 
    print("IP Status: ", scanner[ip_addr].state())
    #Print protocols
    print(scanner[ip_addr].all_protocols())
    #Print open TCP ports
    print("Open Ports: ", scanner[ip_addr]["tcp"].keys())
elif resp == "2":
    #Print nmap version
    print("Nmap Version: ", scanner.nmap_version())
    #Define type of scan
    scanner.scan(ip_addr, "1-1024", "-v -sU")
    #Print scan info
    print(scanner.scaninfo())
    #Print status of IP address 
    print("IP Status: ", scanner[ip_addr].state())
    #Print protocols
    print(scanner[ip_addr].all_protocols())
    #Print open UDP ports
    print("Open Ports: ", scanner[ip_addr]["udp"].keys())
elif resp == "3":
    #Print nmap version
    print("Nmap Version: ", scanner.nmap_version())
    #Define type of scan
    scanner.scan(ip_addr, "1-1024", "-v -sS -sV -sC -A -O")
    #Print scan info
    print(scanner.scaninfo())
    #Print status of IP address 
    print("IP Status: ", scanner[ip_addr].state())
    #Print protocols
    print(scanner[ip_addr].all_protocols())
    #Print open TCP ports
    print("Open Ports: ", scanner[ip_addr]["tcp"].keys())
elif resp >= "4":
    print("Please enter a valid option (1-3): \n")
