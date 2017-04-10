# COMS 4701 Jianpu Ma

"""

Create ICMP(ping) between 2 machine
show the response
Monitor the packet : tcpdump -i eth0 -vv -XX
Copy the ouput from tcpdump and response to result file

"""


### usage: $ python sa.py <valid ip address>

import sys
from scapy.all import *
import socket


def main():

    try:
        ip = sys.argv[1]
    except IndexError:
        print "Error: Provide IP address"
        exit(0)


    try:
        p = sr1(IP(dst=ip) / ICMP() / Raw(load="TEST"))
    except socket.error:
        print "Can't open socket maybe you are not root?"
        exit(0)
    if p:
        """
        If got response print it.
        """
        p.show()


if __name__ == "__main__":
    main()