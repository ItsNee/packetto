import socket
import struct
from general import *


class Ethernet:

    def __init__(self, raw_data):
        #To unpack the ethernet frame by ! 6s 6s H where 6b for receiver, 6b for sender, H for proto and data for first 14b
        dest, src, prototype = struct.unpack('! 6s 6s H', raw_data[:14])

        self.dest_mac = get_mac_addr(dest)
        self.src_mac = get_mac_addr(src)
        self.proto = socket.htons(prototype)
        self.data = raw_data[14:]