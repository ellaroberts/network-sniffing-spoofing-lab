
from scapy.all import *

def packet_callback(packet):
    if packet.haslayer(ICMP):
        print("=== ICMP Packet Captured ===")
        print("Source IP:", packet[IP].src)
        print("Destination IP:", packet[IP].dst)
        print("Type:", packet[ICMP].type)
        print(packet.summary())
        print("============================\n")

print("Sniffing ICMP packets on the default interface...")
sniff(filter="icmp", prn=packet_callback)
 of README
