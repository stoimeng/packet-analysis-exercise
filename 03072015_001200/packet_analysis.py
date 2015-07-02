#!/usr/bin/env python
if 64 - 64: i11iIiiIii
import sys
from collections import Counter
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
import logging
logging . getLogger ( "scapy.runtime" ) . setLevel ( logging . ERROR )
if 73 - 73: II111iiii
from scapy . all import *
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
__all__ = [ 'init' , 'handle_packet' , 'print_summary' ]
if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
IiiIII111iI = 2
IiII = 80
iI1Ii11111iIi = 0
i1i1II = 1
O0oo0OO0 = 1
I1i1iiI1 = 1
if 24 - 24: oOOOO0o0o
Ii1iI = "www.google.com."
if 100 - 100: i11Ii11I1Ii1i . ooO - OOoO / oOOOO0o0o * OoO0O00 . II111iiii
Ii1IIii11 = True
Oooo0000 = set ( )
i11 = set ( )
I11 = Counter ( )
if 98 - 98: i11iIiiIii * I1IiiI % oOOOO0o0o * oOOOO0o0o * II111iiii
def o0o0Oo0oooo0 ( packet ) :
 if (
 packet . haslayer ( DNSRR ) and
 packet [ DNS ] . qr == i1i1II
 ) :
  return True
  if 97 - 97: Oo0Ooo - OOoO
 return False
 if 54 - 54: OOoO . OOoO / iIii1I11I1II1 / I11i + oO0o / o0oOOo0O0Ooo
def I1i1I ( packet ) :
 if o0o0Oo0oooo0 ( packet ) and packet [ DNS ] . ancount > 0 :
  for OOoOoo00oo in packet [ DNS ] . an :
   if OOoOoo00oo . type == I1i1iiI1 and OOoOoo00oo . rrname == Ii1iI :
    Oooo0000 . add ( OOoOoo00oo . rdata )
    if 41 - 41: iIii1I11I1II1 / ooO + OOooOOo
def OOooO ( packet ) :
 if packet . haslayer ( TCP ) :
  OOoO00o = packet [ IP ]
  II111iiiiII = OOoO00o [ TCP ]
  if (
 II111iiiiII . flags == IiiIII111iI and
 II111iiiiII . dport == IiII and
 OOoO00o . dst in Oooo0000
 ) :
   return True
   if 63 - 63: OoOoOO00 % i1IIi
  return False
  if 66 - 66: Ii1I
def oo0Ooo0 ( packet ) :
 if OOooO ( packet ) :
  i11 . add ( packet [ TCP ] . sport )
  if 46 - 46: OOoO % OOoO - oO0o * o0oOOo0O0Ooo % oOOOO0o0o
def OOooO0OOoo ( packet ) :
 if (
 packet . haslayer ( DNSQR ) and
 packet [ DNSQR ] . qtype == O0oo0OO0 and
 packet [ DNS ] . qr == iI1Ii11111iIi
 ) :
  return True
  if 29 - 29: o0oOOo0O0Ooo / iIii1I11I1II1
 return False
 if 24 - 24: O0 % o0oOOo0O0Ooo + i1IIi + ooO + I1ii11iIi11i
def OOoO000O0OO ( packet ) :
 if OOooO0OOoo ( packet ) :
  if 23 - 23: i11iIiiIii + I1IiiI
  oOo = packet [ DNSQR ] . qname [ : - 1 ]
  I11 [ oOo ] += 1
  if 63 - 63: Oo0Ooo
def handle_packet ( packet ) :
 if Ii1IIii11 :
  I1i1I ( packet )
 oo0Ooo0 ( packet )
 OOoO000O0OO ( packet )
 if 57 - 57: oO0o
def iI ( ) :
 iI11iiiI1II = 'List of TCP source ports from connections initiated to www.google.com:80'
 print iI11iiiI1II
 print '=' * len ( iI11iiiI1II )
 if 79 - 79: ooO % i11iIiiIii / iIii1I11I1II1 . OOooOOo
 for o0oO0o00oo in sorted ( i11 ) :
  print o0oO0o00oo
  if 32 - 32: Oo0Ooo * O0 % oO0o % Ii1I . i11Ii11I1Ii1i
 print
 if 61 - 61: OOoO
def oOOO00o ( ) :
 iI11iiiI1II = 'Domain name distribution in DNS resolution queries'
 print iI11iiiI1II
 print '=' * len ( iI11iiiI1II )
 if 97 - 97: I11i % I11i + II111iiii * oOOOO0o0o
 o0o00o0 = '{:20} | {:<5} | {}'
 if 25 - 25: Oo0Ooo - i11Ii11I1Ii1i . OoooooooOO
 iI11iiiI1II = o0o00o0 . format ( 'name' , 'count' , 'percentage of total' )
 print iI11iiiI1II
 print '-' * len ( iI11iiiI1II )
 if 22 - 22: i11Ii11I1Ii1i + II111iiii % ooO . I11i . OoOoOO00
 if 76 - 76: OoOoOO00 - O0 % OOooOOo / I1ii11iIi11i / OoOoOO00
 o0o00o0 = o0o00o0 [ : - 1 ] + ':.2%}'
 if 54 - 54: I1IiiI % II111iiii % II111iiii
 iI1 = sum ( I11 . values ( ) )
 for i11Iiii , iII1i1I1II in I11 . most_common ( ) :
  print o0o00o0 . format ( i11Iiii , iII1i1I1II , float ( iII1i1I1II ) / float ( iI1 ) )
  if 45 - 45: ooO . OoOoOO00
 print
 if 83 - 83: oO0o . iIii1I11I1II1 . I1ii11iIi11i
def init ( google_ips , inspect_google_ip ) :
 global Oooo0000
 global Ii1IIii11
 if 31 - 31: Ii1I . Ii1I - o0oOOo0O0Ooo / OoO0O00 + OOoO * I1IiiI
 if not google_ips is None :
  Oooo0000 = set ( google_ips )
  if 63 - 63: ooO % i1IIi / OoooooooOO - OoooooooOO
 Ii1IIii11 = inspect_google_ip
 if 8 - 8: OoOoOO00
def print_summary ( ) :
 iI ( )
 oOOO00o ( )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
