#!/usr/bin/env python

import scapy.all as scapy

arp_request = scapy.ARP(psdt="192.168.0.1/24")

ether_broadcart = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

arp_broadcast = arp_request/ether_broadcart

answered_list = scapy.srp(arp_broadcast, timeout=1, verbose=False)[0]

print(answered_list)