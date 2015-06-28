# packet-analysis-exercise

Features:
- preliminary 'capture.pcap' - ran capture for only a short time
- collecting information for source ports in connections initiated to www.google.com:80
- collection information for domain names in DNS "A" queries
- formatted output of summary of the information
- simulation of packet data collection from multiple IO streams and async handling of streams

TODO:
- continuous updating of list of 'www.google.com' IP addresses as part of inspecting the packet data
- obfuscation
- others / advanced

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

