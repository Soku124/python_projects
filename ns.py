#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip) # Creating ARP request
    # arp_request.pdst=ip
    # print(arp_request.summary())
    # scapy.ls(scapy.ARP()) # list all the field we can have

    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") # creating broadcast packet
    
    arp_request_broadcast = broadcast/arp_request

    # print(arp_request_broadcast.summary())
    # arp_request_broadcast.show()

    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    # print(answered_list.summary())

    print("_"*45)
    print("IP\t\t\tMAC Address\n-------------------------------------------")

    clients_list = []

    for element in answered_list:
        clients_dict = {"ip":element[1].psrc,"mac":element[1].hwsrc}
        clients_list.append(clients_dict)
        # print(element[1].psrc,end="\t\t")
        # print(element[1].hwsrc)
    return clients_list

def print_result(results_list):

    for element in results_list:
        print(element["ip"], end="\t\t")
        print(element["mac"])

results_list = scan("192.168.73.2/24")
        
print_result(results_list=results_list)





