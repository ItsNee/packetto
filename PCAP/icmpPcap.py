import socket
import sys
from general import *
from networking.ethernet import Ethernet
from networking.ipv4 import IPv4
from networking.icmp import ICMP
from networking.tcp import TCP
from networking.udp import UDP
from networking.pcap import Pcap
from networking.http import HTTP

TAB_1 = '\t - '
TAB_2 = '\t\t - '
TAB_3 = '\t\t\t - '
TAB_4 = '\t\t\t\t - '

DATA_TAB_1 = '\t   '
DATA_TAB_2 = '\t\t   '
DATA_TAB_3 = '\t\t\t   '
DATA_TAB_4 = '\t\t\t\t   '


def icmp():
    pcap = Pcap('capture.pcap')
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    interfaceSelection = input("Please enter the interface to sniff-> ")
    conn.bind((interfaceSelection,0))
    n = 0
    print('[ICMP][PCAP]')
    numberInput = input("Please enter numbers of packet to scan: ")
    number = int(numberInput)
    while True:
        while n < number:
            raw_data, addr = conn.recvfrom(65535)
            pcap.write(raw_data)
            eth = Ethernet(raw_data)

            print('\nEthernet Frame:')
            print(TAB_1 + 'Destination: {}, Source: {}, Protocol: {}'.format(eth.dest_mac, eth.src_mac, eth.proto))

            #IPv4 
            if eth.proto == 8:
                ipv4 = IPv4(eth.data)
                print(TAB_1 + 'IPv4 Packet:')
                print(TAB_2 + 'Version: {}, Header Length: {}, TTL: {},'.format(ipv4.version, ipv4.header_length, ipv4.ttl))
                print(TAB_2 + 'Protocol: {}, Source: {}, Target: {}'.format(ipv4.proto, ipv4.src, ipv4.target)) 
                #ICMP
                if ipv4.proto == 1:
                    icmp = ICMP(ipv4.data)
                    print(TAB_1 + 'ICMP Packet:')
                    print(TAB_2 + 'Type: {}, Code: {}, Checksum: {},'.format(icmp.type, icmp.code, icmp.checksum))
                    print(TAB_2 + 'ICMP Datadadadada:')
                    print(format_multi_line(DATA_TAB_3, icmp.data))
            else:
                print('Ethernet Data:')
                print(format_multi_line(DATA_TAB_1, eth.data))
                n+=1
        sys.exit()

            
    pcap.close()


icmp()