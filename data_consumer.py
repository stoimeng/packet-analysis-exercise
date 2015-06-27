#!/usr/bin/env python

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import *
from twisted.internet import reactor, protocol
from twisted.protocols import basic
from analysis import handle_packet, print_summary

COUNT = 0

class PacketDataClient(basic.Int16StringReceiver):
    def stringReceived(self, data):
        global COUNT
        handle_packet(Ether(data))
        COUNT += 1
        self.sendString('OK')

class PacketDataClientFactory(protocol.ClientFactory):
    protocol = PacketDataClient

    def clientConnectionFailed(self, connector, reason):
        print 'WARNING: cannot connect to data provider.'

    def clientConnectionLost(self, connector, reason):
        print COUNT

def run(address, port, connections):
    factory = PacketDataClientFactory()
    for _ in xrange(0, connections):
        reactor.connectTCP(address, port, factory)
    reactor.run()

def main():
    run('localhost', 8000, 10)

if __name__ == '__main__':
    main()
