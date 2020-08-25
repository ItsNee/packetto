#!/bin/python3

import sys
import getopt
import socket
from datetime import datetime as dt
import struct
import textwrap


#Helpful functions
def nl():
	print('\n') #prints new line when function is called

def banner():
    #Add a pretty banner
    nl()
    print("""
     _______                      __                    __      __               
    /       \                    /  |                  /  |    /  |              
    $$$$$$$  | ______    _______ $$ |   __   ______   _$$ |_  _$$ |_     ______  
    $$ |__$$ |/      \  /       |$$ |  /  | /      \ / $$   |/ $$   |   /      \ 
    $$    $$/ $$$$$$  |/$$$$$$$/ $$ |_/$$/ /$$$$$$  |$$$$$$/ $$$$$$/   /$$$$$$  |
    $$$$$$$/  /    $$ |$$ |      $$   $$<  $$    $$ |  $$ | __ $$ | __ $$ |  $$ |
    $$ |     /$$$$$$$ |$$ \_____ $$$$$$  \ $$$$$$$$/   $$ |/  |$$ |/  |$$ \__$$ |
    $$ |     $$    $$ |$$       |$$ | $$  |$$       |  $$  $$/ $$  $$/ $$    $$/ 
    $$/       $$$$$$$/  $$$$$$$/ $$/   $$/  $$$$$$$/    $$$$/   $$$$/   $$$$$$/
                                                            """)
    nl()

#check for length
def null_checker():
    if len(sys.argv) == 1:
        print("Invalid number of arguments entered :(")
        print("Syntax --> python3 packeto.py -H\n")
        sys.exit()

#argument stuff
def get_arguement():
    full_cmd_arguments = sys.argv

    argument_list = full_cmd_arguments[1:]

    #print (argument_list)
    hyphencounter=0
    for i in argument_list:
        if '-' in i:
            lol="lol" #34ST3R 3GG :3 d1stin?
        else:
            hyphencounter = hyphencounter + 1
    
    if hyphencounter > 0:
        print("Invalid argument(s) entered :(")
        print("Syntax --> python3 packeto.py -a\n")
        sys.exit()

    short_options = "h:Ha:i:u:t:"
    long_options = ["help", "all=", "icmp=", "http=", "udp=","tcp="]

    try:
        arguments, values = getopt.getopt(argument_list, short_options, long_options)
        #print(arguments)
    except getopt.error as err:
        # Output error, and return with an error code
        print (str(err))
        print ("\n")
        sys.exit(2)

    for current_argument, current_value in arguments:
        #print(current_argument)
        if current_argument in ("-H", "--help"):
            print ("Displaying help\n")
            help_method()
        elif current_argument in ("-a", "--all"):
            if current_value == "o":
                from PCAP.snifferPcap import main
            elif current_value == "n":
                from IPV4.sniffer import main


        elif current_argument in ("-i", "--icmp"):
            if current_value == "o":
                from PCAP.icmpPcap import icmp
            elif current_value == "n":
                from IPV4.icmp import icmp



        elif current_argument in ("-h", "--http"):
            if current_value == "o":
                from PCAP.httpPcap import http
            elif current_value == "n":
                from IPV4.http import http



        elif current_argument in ("-u", "--udp"):
            if current_value == "o":
                from PCAP.udpPcap import udp
            elif current_value == "n":
                from IPV4.udp import udp



        elif current_argument in ("-t", "--tcp"):
            if current_value == "o":
                from PCAP.tcpPcap import tcp
            elif current_value == "n":
                from IPV4.tcp import tcp
        # else:
        #     print ("Need option! \n")

def help_method():
    print ("\n")
    print ("-H, --help: Displays all commands and what they do. (no shame in asking for help :))")
    print ("\n")
    print ("-a<o/n>, --all<o/n>")
    print ("O for output to Pcapfile, N for no output to Pcapfile")
    print (" Sets option to capture all packets going through network interface.")
    print ("\n")
    print ("-h<o/n>, --http<o/n>")
    print ("O for output to Pcapfile, N for no output to Pcapfile")
    print (" Sets option to capture http packets only.")
    print ("\n")
    print ("-t<o/n>, --tcp<o/n>")
    print ("O for output to Pcapfile, N for no output to Pcapfile")
    print (" Sets option to capture tcp packets only.")
    print ("\n")
    print ("-u<o/n>, --udp<o/n>")
    print ("O for output to Pcapfile, N for no output to Pcapfile")
    print (" Sets option to capture udp packets only.")
    print ("\n")
    print ("-i<o/n>, --icmp<o/n>")
    print ("O for output to Pcapfile, N for no output to Pcapfile")
    print (" Sets option to capture icmp packets only.")
    print ("\n")
    print ("***************************************************************************************")
    print ("PCAPFILES WOULD BE SAVED IN THE SAME LOCATION WHERE THE PROGRAM IS RUNNING ON")
    print ("***************************************************************************************")




#Unpack the ethernet frame by ! 6s 6s H where 6b for receiver, 6b for sender, h for proto and data for first 14b
def ethernet_frame(data):
  dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
  return get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[14:]

#Return properly formatted MAC Addr
def get_mac_addr(bytes_addr):
  bytes_str = map('{:02x}'.format, bytes_addr)
  return ':'.join(bytes_str).upper()

#main code
def main():
  banner()
  null_checker()
  get_arguement()

#call main
main()
                                                     
                                                                             
