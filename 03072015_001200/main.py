#!/usr/bin/env python
if 64 - 64: i11iIiiIii
import sys
import argparse
from packet_data import run
from packet_analysis import init , print_summary
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
o0OO00 = 8000
oo = 10
if 27 - 27: oO0OooOoO * o0Oo
def i1IiI1I11 ( ) :
 IIiIiII11i = argparse . ArgumentParser ( description = 'Packet analysis challenge solution.' )
 o0oOOo0O0Ooo = IIiIiII11i . add_argument_group ( 'File required argument group' )
 o0oOOo0O0Ooo . add_argument ( '-f' , metavar = 'CAPTURE_FILE' , required = True ,
 help = 'A file containing traffic captured in PCAP format' )
 IIiIiII11i . add_argument ( '-d' , dest = 'inspect_google_ip' , action = 'store_false' ,
 help = 'Do not inspect packets for www.google.com IP addresses' )
 IIiIiII11i . set_defaults ( inspect_google_ip = True )
 IIiIiII11i . add_argument ( '-p' , metavar = 'PORT' , type = int , default = o0OO00 ,
 help = 'A local port to open for packet data client/server communication' )
 IIiIiII11i . add_argument ( '-c' , metavar = 'COUNT' , type = int ,
 default = oo ,
 help = 'Count of packet data client connections' )
 IIiIiII11i . add_argument ( '-g' , metavar = 'IP' , nargs = '+' ,
 help = 'IP addresses of www.google.com' )
 return IIiIiII11i . parse_args ( )
 if 2 - 2: o0 * i1 * ii1IiI1i % OOooOOo / I11i / Ii1I
def IiiIII111iI ( ) :
 IiII = i1IiI1I11 ( )
 if 28 - 28: Ii11111i * iiI1i1
 init ( IiII . g , IiII . inspect_google_ip )
 run ( 'localhost' , IiII . p , IiII . c , IiII . f )
 print_summary ( )
 if 46 - 46: Ooo0OO0oOO * Ii * Oo0o
if __name__ == '__main__' :
 IiiIII111iI ( )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
