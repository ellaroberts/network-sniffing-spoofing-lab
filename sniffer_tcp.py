#!/usr/bin/env python3
from scapy.all import *

def packet_callback(packet):
    if packet.haslayer(TCP):
        print("=== TCP Packet Captured ===")
        print("Source IP:", packet[IP].src)
        print("Destination IP:", packet[IP].dst)
        print("Source Port:", packet[TCP].sport)
        print("Destination Port:", packet[TCP].dport)
        print(packet.summary())
        print("===========================\n")

print("Sniffing TCP packets on the default interface...")
sniff(filter="tcp", prn=packet_callback)
