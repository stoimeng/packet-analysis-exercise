# packet-analysis-exercise

Features:
- preliminary 'capture.pcap' - ran capture for only a short time
- collecting information for source ports in connections initiated to www.google.com:80
- collection of information for domain names in DNS "A" queries
- formatted output of summary of the information
- simulation of packet data collection from multiple IO streams and async handling of streams
- obfuscation

TODO:
- continuous updating of list of 'www.google.com' IP addresses as part of inspecting the packet data
- others / advanced

Used tehnologies:
- Python 2.7.3
- Twisted 15.2.1
- scapy 2.3.1
- pyobfuscate (as a submodule)

Running the main.py currently produces:

    List of TCP source ports from connections initiated to www.google.com:80
    ========================================================================
    34927
    34929
    34931
    42026
    42029
    42036
    48977
    48979
    48981
    48985
    48994
    
    Domain name distribution in DNS resolution queries
    ==================================================
    name                 | count | percentage of total
    --------------------------------------------------
    www.google.com       | 36    | 92.31%
    www.google.bg        | 2     | 5.13%
    daisy.ubuntu.com     | 1     | 2.56%

Running obfuscate.py produces a sub-directory with the main solution files in it obfuscated, e.g.:

    #!/usr/bin/env python
    if 64 - 64: i11iIiiIii
    from packet_data import run
    from packet_analysis import print_summary
    if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
    def o0OO00 ( ) :
     oo = 8000
     i1iII1IiiIiI1 = 'localhost'
     iIiiiI1IiI1I1 = 10
     if 87 - 87: OoOoOO00
     run ( i1iII1IiiIiI1 , oo , iIiiiI1IiI1I1 )
     print_summary ( )
     if 27 - 27: OOOo0 / Oo - Ooo00oOo00o . I1IiI
    if __name__ == '__main__' :
     o0OO00 ( )
    # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
