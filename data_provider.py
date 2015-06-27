#!/usr/bin/env python

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import *
from twisted.internet import reactor, protocol
from twisted.protocols import basic

PACKETS = None

class PacketDataServer(basic.Int16StringReceiver):
    def connectionMade(self):
        if not self._sendPacket():
            self.transport.loseConnection()

    def stringReceived(self, data):
        if data != 'OK':
            print 'WARNING: protocol violation by client.'
            self.transport.loseConnection()
        elif not self._sendPacket():
                self.transport.loseConnection()

    def _sendPacket(self):
        packet = self._getPacket()
        if packet is None:
            return False

        packet_string = str(packet)
        self.sendString(packet_string)
        return True

    def _getPacket(self):
        if PACKETS:
            return PACKETS.pop(0)

        return None

def run(port):
    global PACKETS
    PACKETS = rdpcap('capture.pcap')

    factory = protocol.ServerFactory()
    factory.protocol = PacketDataServer
    reactor.listenTCP(port, factory)
    reactor.run()

def main():
    run(8000)

if __name__ == '__main__':
    main()
