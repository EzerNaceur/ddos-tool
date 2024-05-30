# Simple and slow http-flooding attack script
This Python script simulates a DDoS (Distributed Denial of Service) attack using multithreading. The script allows you to specify the target IP address, the port to attack, whether to use a spoofed IP address, and the number of threads to run the attack method.

## Prerequisites

- Python 3.x
- Required Python modules: socket, threading, argparse, ipaddress, random

## Usage

To run the script, use the following command:

```sh
python ddos_simulation.py -d <destination_ip> -p <port> -s -t <threads>
```

## Flags

- -d or --destination: The target IP address (required).
- -p or --port: The port to attack (default is 80; only port 80 is supported currently).
- -s or --spoof: Use a spoofed random IP address in the request headers.
- -t or --threads: Specify the number of threads to run the attack (default is 500).

## Examples

```sh
# Basic usage with required parameters
python ddos_simulation.py -d 192.168.1.1

# Specify the port and use IP spoofing
python ddos_simulation.py -d 192.168.1.1 -p 80 -s

# Specify the number of threads
python ddos_simulation.py -d 192.168.1.1 -t 1000
```

## Disclaimer

This script is for educational purposes only. Unauthorized use of this script to attack a system is illegal and unethical. Always obtain proper authorization before testing or attacking any system.
