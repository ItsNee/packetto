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


def udp():
    pcap = Pcap('capture.pcap')
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    interfaceSelection = input("Please enter the interface to sniff-> ")
    conn.bind((interfaceSelection,0))
    n = 0
    print('[UDP][PCAP]')
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

                #UDP Segments
                if ipv4.proto == 17:
                    udp = UDP(ipv4.data)
                    print(TAB_1 + 'UDP Segment:')
                    print(TAB_2 + 'Source Port: {}, Destination Port: {}, Length: {}'.format(udp.src_port, udp.dest_port, udp.size))
                n+=1

            else:
                print('Ethernet Data:')
                print(format_multi_line(DATA_TAB_1, eth.data))
                n+=1
        sys.exit()

            
    pcap.close()

udp()