#!/usr/bin/env python

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import rdpcap, Ether
from twisted.internet import reactor, protocol, defer
from twisted.protocols import basic
from packet_analysis import handle_packet, print_summary

__all__ = ['run']

PACKET_DATA_PROTOCOL_CLIENT_CONFIRM = 'OK'

class PacketDataServer(basic.Int16StringReceiver):
    def connectionMade(self):
        if not self._sendPacket():
            self.transport.loseConnection()

    def stringReceived(self, data):
        if data != PACKET_DATA_PROTOCOL_CLIENT_CONFIRM:
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
        data = self.factory.data
        if data:
            return data.pop(0)
        return None

class PacketDataServerFactory(protocol.ServerFactory):
    protocol = PacketDataServer

    def __init__(self, data):
        self.data = data

class PacketDataClient(basic.Int16StringReceiver):
    def stringReceived(self, data):
        handle_packet(Ether(data))
        self.sendString(PACKET_DATA_PROTOCOL_CLIENT_CONFIRM)

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

def run(address, port, connections, file_name):
    data = rdpcap(file_name)

    factory = PacketDataServerFactory(data)
    reactor.listenTCP(port, factory)

    dfr = defer.Deferred()
    dfr.addCallback(_clients_done)
    factory = PacketDataClientFactory(connections, dfr)
    for _ in xrange(0, connections):
        reactor.connectTCP(address, port, factory)

    reactor.run()
