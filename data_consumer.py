#!/usr/bin/env python

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import *
from twisted.internet import reactor, protocol, defer
from twisted.protocols import basic
from analysis import handle_packet, print_summary

class PacketDataClient(basic.Int16StringReceiver):
    def stringReceived(self, data):
        handle_packet(Ether(data))
        self.sendString('OK')

class PacketDataClientFactory(protocol.ClientFactory):
    protocol = PacketDataClient

    def __init__(self, count, dfr):
        self._connectionCount = 0
        self._protocolCount = count
        self._dfr = dfr

    def buildProtocol(self, addr):
        if self._protocolCount == 0:
            return None
        else:
            self._protocolCount -= 1

        return protocol.ClientFactory.buildProtocol(self, addr)

    def startedConnecting(self, connector):
        self._connectionCount += 1
        
    def clientConnectionFailed(self, connector, reason):
        print 'WARNING: count not connect to data provider.'
        self._connectionDecrement()

    def clientConnectionLost(self, connector, reason):
        self._connectionDecrement()

    def _connectionDecrement(self):
        self._connectionCount -= 1
        if self._connectionCount == 0 and self._protocolCount == 0:
            self._dfr.callback(None)

def _clients_done(result):
    reactor.stop()

def run(address, port, connections):
    dfr = defer.Deferred()
    dfr.addCallback(_clients_done)

    factory = PacketDataClientFactory(connections, dfr)

    for _ in xrange(0, connections):
        reactor.connectTCP(address, port, factory)

    reactor.run()

    print_summary()

def main():
    run('localhost', 8000, 10)

if __name__ == '__main__':
    main()
