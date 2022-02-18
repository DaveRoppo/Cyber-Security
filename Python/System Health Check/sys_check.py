import shutil
import psutil
import time
import requests
import socket 

def CheckDiskUsage():
	du = shutil.disk_usage("/")
	free = du.free/du.total * 100
	return float(free) > 20 
	
def CheckCPUusage():
	usage = psutil.cpu_percent(1)
	return float(usage) < 75 
	
def check_localhost():
	localhost = socket.gethostbyname('localhost')
	return localhost ==  "127.0.0.1"

def check_connectivity():
	request = requests.get("http://google.com")
	status = request.status_code
	return status == 200
	
if not CheckDiskUsage() or not CheckCPUusage() or not check_localhost() or not check_connectivity():
	print("Issue Detected.")
	du = shutil.disk_usage("/")
	free = du.free/du.total * 100
	print("Free Disk Space:", free,"%")
	usage = psutil.cpu_percent(1)
	print("CPU Usage:", usage)
	request = requests.get("http://google.com")
	status = request.status_code
	print("Status code: ", status)
	localhost = socket.gethostbyname('localhost')
	print("Local host: ", localhost)
	
else:
	print("\nSystem is healthy.")
	time.sleep(.8)
	print("\nNetwork connectivity is good.")
	time.sleep(.8)
	du = shutil.disk_usage("/")
	free = du.free/du.total * 100
	print("\nFree Disk Space:", free,"%")
	usage = psutil.cpu_percent(1)
	print("\nCPU Usage:", usage)
	print("\n")
	
