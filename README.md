# packet-analysis-exercise

Features:
- captured network traffic for 10+ minutes split into the multiple files - capture.pcapX
- continuous updating of list of 'www.google.com' IP addresses as part of inspecting the packet data
- collecting information for source ports in connections initiated to www.google.com:80
- collection of information for domain names in DNS "A" queries
- formatted output of summary of the information
- simulation of packet data collection from multiple IO streams and async handling of streams
- obfuscation
- obfuscated version of the scripts generated in the corresponding sub-directory
- specifying the various options from command line as well as documentation of the options through -h option

TODO:
- others / advanced

Used tehnologies:
- Python 2.7.3
- Twisted 15.2.1
- scapy 2.3.1
- pyobfuscate (as a submodule)

Knowns issues and limitations:
- running the scripts on the originally generated file (combination of all capture.pcapX files) takes a lot of memory - this is probably due to scapy initial loading of the file which cannot be done lazily by default
- obfuscation scripts can be run only from within the main solution directory (where the actual obfuscate.py is located)

The command line options can be seen as follows:

    $ python main.py -h
    usage: main.py [-h] -f CAPTURE_FILE [-d] [-p PORT] [-c COUNT] [-g IP [IP ...]]
    
    Packet analysis challenge solution.
    
    optional arguments:
      -h, --help       show this help message and exit
      -d               Do not inspect packets for www.google.com IP addresses
      -p PORT          A local port to open for packet data client/server
                       communication
      -c COUNT         Count of packet data client connections
      -g IP [IP ...]   IP addresses of www.google.com
    
    File required argument group:
      -f CAPTURE_FILE  A file containing traffic captured in PCAP format


The results produced by the scripts are as follows:

    $ python main.py -f capture.pcap4
    List of TCP source ports from connections initiated to www.google.com:80
    ========================================================================
    42588
    42589
    42590
    42591
    42593
    42595
    42597
    42599
    42601
    42603
    42605
    42608
    42610
    42612
    42614
    42616
    42618
    42622
    42625
    42627
    42629
    42630
    42633
    42635
    42638
    42641
    42644
    42646
    42648
    42650
    42652
    42654
    42658
    
    Domain name distribution in DNS resolution queries
    ==================================================
    name                 | count | percentage of total
    --------------------------------------------------
    www.google.com       | 40    | 45.45%
    www.google.bg        | 32    | 36.36%
    www.facebook.com     | 5     | 5.68%
    finance.google.com   | 3     | 3.41%
    bg.archive.ubuntu.com | 3     | 3.41%
    google.com           | 3     | 3.41%
    stackoverflow.com    | 1     | 1.14%
    tracker.zamunda.net  | 1     | 1.14%



Running the obfuscation can be done only from within the solution directory:

    $ python obfuscate.py 


The obfuscation produces a sub-directory with the main solution files in it obfuscated, e.g.:

    $ cat 03072015_001200/main.py 
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

