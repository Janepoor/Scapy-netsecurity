import string
from scapy.all import *
import sys

def loop():
    try:
        sourceport = int(sys.argv[1])
        destport = int(sys.argv[2])
    except IndexError as E:
        print "E"


    loopbackip="127.0.0.1"
    for i in range(3000, 3021):
        send(IP(dst=loopbackip) / TCP(dport=i))

    """
    Generate 5 packets and then send them
    """

    for i in range(0, 5):

        randomstr = ''.join(random.choice(string.letters) for x in range(10))
        send(IP(dst=loopbackip) / TCP(sport=sourceport, dport=destport) / Raw(load=randomstr))

    p = Packet(sourceport, destport)

def main():
    loop()

if __name__ == '__main__':
    main()
