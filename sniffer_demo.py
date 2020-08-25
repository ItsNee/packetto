import socket
import struct
import textwrap

def main():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    while True:
        raw_data, addr = conn.recvfrom(65536)
        
        dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)
        print('\nEthernet Frame:')
        print('Destination: {}, Source: {}, Protocol: {}'.format(dest_mac, src_mac, eth_proto))

        #IPv4 
        if eth_proto == 8:
            (version, header_length, ttl, proto, src, target, data) = ipv4_packet(data)
            print('IPv4 Packet:')
            print('Version: {}, Header_Length: {}, TTL: {}'.format(version, header_length, ttl))
            print('Protocol: {}, Source: {}, Target: {}'.format(proto, src, target))

            #ICMP 
            if proto == 1:
                icmp_type, code, checksum, data = icmp_packet(data)
                print('ICMP Packet:')
                print('Type: {}, Code: {}, Checksum: {},'.format(icmp_type, code, checksum))
                print('Data:')
                print(format_multi_line(data))

            #TCP Segments
            elif proto == 6:
                (src_port, dest_port, sequence, acknowledgement, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin, data) = tcp_segment(data)
                print('TCP Segment:')
                print('Source Port: {}, Destination Port: {}'.format(src_port, dest_port))
                print('Sequence: {}, Acknowledge: {}'.format(sequence, acknowledgement))
                print('Flags:')
                print('URG: {}, ACK: {}, PSH: {}, RST: {}, SYN: {}, FIN: {}'.format(flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin))
                print('Data:')
                print(format_multi_line(data))

            #UDP Segments
            elif proto == 17:
                src_port, dest_port, length, data = udp_segment(data)
                print('UDP Segment:')
                print('Source Port: {}, Destination Port: {}, Length: {}'.format(src_port, dest_port, length))

            #Others
            else:
                print('Data: ')
                print(format_multi_line(data))

        else:
            print('Data: ')
            print(format_multi_line(data))

#To unpack the ethernet frame by ! 6s 6s H where 6b for receiver, 6b for sender, H for proto and data for first 14b
def ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
    return get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[14:]

#To properly format the MAC Addr into like AA:BB:CC:DD:EE:FF
def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    return ':'.join(bytes_str).upper()

#To unpack the IPv4 Packet where 8b 1b 1b 2b 4b 4b and total data is 20b
def ipv4_packet(data):
    #Get first byte of data
    version_header_length = data[0]
    #Get version by overlapping HL
    version = version_header_length >> 4
    #get whole header length to know where data starts
    header_length = (version_header_length & 15) * 4
    ttl, proto, src, target = struct.unpack('! 8x B B 2x 4s 4s', data[:20])
    return version, header_length, ttl, proto, ipv4(src), ipv4(target), data[header_length:]

#To properly format IPv4 Address
def ipv4(addr):
    return '.'.join(map(str,addr))

#To unpack ICMP Packets 
def icmp_packet(data):
    icmp_type, code, checksum = struct.unpack('! B B H', data[:4])
    return icmp_type, code, checksum, data[4:]

#To unpack TCP segment
def tcp_segment(data):
    (src_port, dest_port, sequence, acknowledgement, offset_reserved_flags) = struct.unpack('! H H L L H', data[:14])
    #Overlap to get offset so basically 00000... then offset
    offset = (offset_reserved_flags >> 12) * 4
    #Get and separate diff types of flags
    flag_urg = (offset_reserved_flags & 32) >> 5
    flag_ack = (offset_reserved_flags & 16) >> 4
    flag_psh = (offset_reserved_flags & 8) >> 3
    flag_rst = (offset_reserved_flags & 4) >> 2
    flag_syn = (offset_reserved_flags & 2) >> 1
    flag_fin = offset_reserved_flags & 1
    return src_port, dest_port, sequence, acknowledgement, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin, data[offset:]

#To unpack UDP segment
def udp_segment(data):
    src_port, dest_port, size = struct.unpack('! H H 2x H', data[:8])
    return src_port, dest_port, size, data[8:]

#Formatting Multi-line data
def format_multi_line(prefix, string, size=80):
    size -= len(prefix)
    if isinstance(string, bytes):
        string = ''.join(r'\x{:02x}'.format(byte) for byte in string)
        if size % 2:
            size -= 1
    return '\n'.join([prefix + line for line in textwrap.wrap(string, size)])


main()