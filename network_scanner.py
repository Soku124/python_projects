#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    # arp_request.show()
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # broadcast.show()
    arp_request_broadcast = broadcast/arp_request
    # arp_request_broadcast.show()

    # answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=1)
    # print(answered_list.summary())
    # print(unanswered_list.summary())

    answered_list= scapy.srp(arp_request_broadcast, timeout=1)[0]
    print(answered_list.summary())




    

scan("192.168.0.1/24")
