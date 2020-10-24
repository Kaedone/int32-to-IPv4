import socket
import struct

def int32_to_ip(int32):
    return socket.inet_ntoa(struct.pack("!I", int32))
