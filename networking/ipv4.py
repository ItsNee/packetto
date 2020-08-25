import struct


class IPv4:
    #To unpack the IPv4 Packet where 8b 1b 1b 2b 4b 4b and total data is 20b
    def __init__(self, raw_data):
        version_header_length = raw_data[0]
        self.version = version_header_length >> 4
        self.header_length = (version_header_length & 15) * 4
        self.ttl, self.proto, src, target = struct.unpack('! 8x B B 2x 4s 4s', raw_data[:20])
        self.src = self.ipv4(src)
        self.target = self.ipv4(target)
        self.data = raw_data[self.header_length:]

    #To properly format IPv4 Address
    def ipv4(self, addr):
        return '.'.join(map(str, addr))