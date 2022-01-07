import socket
import threading
import sys

hostToScan = input("Hostname: ")
hostIP = socket.gethostbyname(hostToScan)
print("Scanning host", hostIP)

def port_scanner(port):
    try:
        #initialize socket
        thisSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #set a connection timeout
        thisSocket.settimeout(0.5)

        #connect to the IP address port number
        thisSocket.connect((hostIP, port))
        try:
            service = thisSocket.recv(100)
            print(service)
            print(f"Port {port} is open[+] using service {service}")
        except:
            print(f"Port {port} is open [+]")
    except:
        pass

for port in range(1,5000):
    thread = threading.Thread(target=port_scanner, args=[port])
    thread.start()

print("Scan of host " + hostToScan + " complete")
print("-" * 60)