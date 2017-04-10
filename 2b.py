"""
Program to send HTTP GET messages.
"""

from scapy.all import *
import binascii
import ConfigParser
import sys

config = ConfigParser.RawConfigParser()

class SendGet(object):
    """
        Send HTTP GET request to the server.
    """

    def __init__(self):
        #Initialize the parameter
        config.read('inpartb.txt')
        self.saddress = config.get('ip', 'src_address')
        self.daddress = config.get('ip', 'dst_address')
        self.payload = config.get('payload', 'getmessage')

        # Create IP packet
        ip = IP(src=self.saddress, dst=self.daddress)
        tcp = TCP(dport=int(config.get('ip', 'dst')),
                sport=int(config.get('ip', 'source')))
        # Attach the payload to the layered packet
        packet = ip / tcp / Raw(load=binascii.unhexlify(self.payload))
        packet.show()
        print str(packet)
        send(packet)


def main():
    s = SendGet()


if __name__ == "__main__":
    main()