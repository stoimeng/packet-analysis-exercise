#!/usr/bin/env python
if 64 - 64: i11iIiiIii
import logging
logging . getLogger ( "scapy.runtime" ) . setLevel ( logging . ERROR )
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
from scapy . all import rdpcap , Ether
from twisted . internet import reactor , protocol , defer
from twisted . protocols import basic
from packet_analysis import handle_packet , print_summary
if 73 - 73: II111iiii
__all__ = [ 'run' ]
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
I1IiI = 'OK'
if 73 - 73: OOooOOo / ii11ii1ii
class O00ooOO ( basic . Int16StringReceiver ) :
 def connectionMade ( self ) :
  if not self . _sendPacket ( ) :
   self . transport . loseConnection ( )
   if 47 - 47: oO0ooO % iI1Ii11111iIi + ii1II11I1ii1I + oO0o0ooO0 - iiIIIII1i1iI
 def stringReceived ( self , data ) :
  if data != I1IiI :
   print 'WARNING: protocol violation by client.'
   self . transport . loseConnection ( )
  elif not self . _sendPacket ( ) :
   self . transport . loseConnection ( )
   if 68 - 68: o00ooo0 / oO0o0ooO0
 def _sendPacket ( self ) :
  o00 = self . _getPacket ( )
  if o00 is None :
   return False
   if 62 - 62: i11iIiiIii - II111iiii % iiIIIII1i1iI - iIii1I11I1II1 . I1ii11iIi11i . II111iiii
  OOoO = str ( o00 )
  self . sendString ( OOoO )
  return True
  if 91 - 91: OoO0O00 . i11iIiiIii / OOooOOo % oO0ooO / OoO0O00 - i11iIiiIii
 def _getPacket ( self ) :
  II1Iiii1111i = self . factory . data
  if II1Iiii1111i :
   return II1Iiii1111i . pop ( 0 )
  return None
  if 25 - 25: iI1Ii11111iIi
class oo00000o0 ( protocol . ServerFactory ) :
 protocol = O00ooOO
 if 34 - 34: oO0o0ooO0 % II111iiii % iIii1I11I1II1 % oO0o0ooO0 * ii1II11I1ii1I / OoOoOO00
 def __init__ ( self , data ) :
  self . data = data
  if 31 - 31: i11iIiiIii / I1IiiI / o00ooo0 * OOooOOo / Oo0Ooo
class Oo0o0ooO0oOOO ( basic . Int16StringReceiver ) :
 def stringReceived ( self , data ) :
  handle_packet ( Ether ( data ) )
  self . sendString ( I1IiI )
  if 58 - 58: i11iIiiIii % iiIIIII1i1iI
class O0OoOoo00o ( protocol . ClientFactory ) :
 protocol = Oo0o0ooO0oOOO
 if 31 - 31: II111iiii + OoO0O00 . iiIIIII1i1iI
 def __init__ ( self , count , dfr ) :
  self . _connectionCount = 0
  self . _protocolCount = count
  self . _dfr = dfr
  if 68 - 68: I1IiiI - i11iIiiIii - OoO0O00 / ii11ii1ii - OoO0O00 + i1IIi
 def buildProtocol ( self , addr ) :
  if self . _protocolCount == 0 :
   return None
  else :
   self . _protocolCount -= 1
   if 48 - 48: OoooooooOO % o0oOOo0O0Ooo . I1IiiI - iI1Ii11111iIi % i1IIi % OoooooooOO
  return protocol . ClientFactory . buildProtocol ( self , addr )
  if 3 - 3: ii1II11I1ii1I + O0
 def startedConnecting ( self , connector ) :
  self . _connectionCount += 1
  if 42 - 42: ii11ii1ii / i1IIi + i11iIiiIii - iI1Ii11111iIi
 def clientConnectionFailed ( self , connector , reason ) :
  print 'WARNING: count not connect to data provider.'
  self . _connectionDecrement ( )
  if 78 - 78: OoO0O00
 def clientConnectionLost ( self , connector , reason ) :
  self . _connectionDecrement ( )
  if 18 - 18: O0 - ii1II11I1ii1I / ii1II11I1ii1I + o00ooo0 % o00ooo0 - oO0o0ooO0
 def _connectionDecrement ( self ) :
  self . _connectionCount -= 1
  if self . _connectionCount == 0 and self . _protocolCount == 0 :
   self . _dfr . callback ( None )
   if 62 - 62: ii1II11I1ii1I - oO0o0ooO0 - OoOoOO00 % i1IIi / OOooOOo
def OoooooOoo ( result ) :
 reactor . stop ( )
 if 70 - 70: OoO0O00 . OoO0O00 - OoO0O00 / I1ii11iIi11i * ii11ii1ii
def run ( address , port , connections , file_name ) :
 II1Iiii1111i = rdpcap ( file_name )
 if 86 - 86: i11iIiiIii + iI1Ii11111iIi + o00ooo0 * oO0ooO + o0oOOo0O0Ooo
 oOoO = oo00000o0 ( II1Iiii1111i )
 reactor . listenTCP ( port , oOoO )
 if 68 - 68: OoOoOO00 . OOooOOo . i11iIiiIii
 II = defer . Deferred ( )
 II . addCallback ( OoooooOoo )
 oOoO = O0OoOoo00o ( connections , II )
 for iI in xrange ( 0 , connections ) :
  reactor . connectTCP ( address , port , oOoO )
  if 22 - 22: Oo0Ooo % iI1Ii11111iIi
 reactor . run ( )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
