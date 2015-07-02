#!/usr/bin/env python

import sys
from collections import Counter

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import *

__all__ = ['init', 'handle_packet', 'print_summary']

TCP_FLAG_SYN = 2
TCP_PORT_HTTP = 80
DNS_QUERY = 0
DNS_QUESTION_TYPE = 1

INSPECT_GOOGLE_IP = True
GOOGLE_IP_ADDRESSES = []
GOOGLE_CONNECTION_INIT_SOURCE_PORTS = set()
DNS_QUERY_DOMAINS = Counter()

def is_google_connection_init(packet):
    if packet.haslayer(TCP):
        ip = packet[IP]
        tcp = ip[TCP]
        if (
                tcp.flags == TCP_FLAG_SYN and
                tcp.dport == TCP_PORT_HTTP and
                ip.dst in GOOGLE_IP_ADDRESSES
                ):
            return True

        return False

def handle_google_connection_init(packet):
    if is_google_connection_init(packet):
        GOOGLE_CONNECTION_INIT_SOURCE_PORTS.add(packet[TCP].sport)

def is_dns_query_a(packet):
    if (
            packet.haslayer(DNSQR) and
            packet[DNSQR].qtype == DNS_QUESTION_TYPE and
            packet[DNS].qr == DNS_QUERY
            ):
        return True

    return False

def handle_dns_query_a(packet):
    if is_dns_query_a(packet):
        # get the domain name without trailing dot
        domain = packet[DNSQR].qname[:-1]
        DNS_QUERY_DOMAINS[domain] += 1

def handle_packet(packet):
    handle_google_connection_init(packet)
    handle_dns_query_a(packet)

def print_google_connection_init_summary():
    message = 'List of TCP source ports from connections initiated to www.google.com:80'
    print message
    print '=' * len(message)

    for port in sorted(GOOGLE_CONNECTION_INIT_SOURCE_PORTS):
        print port

    print

def print_dns_query_a_summary():
    message = 'Domain name distribution in DNS resolution queries'
    print message
    print '=' * len(message)

    message_format = '{:20} | {:<5} | {}'

    message = message_format.format('name', 'count', 'percentage of total')
    print message
    print '-' * len(message)

    # for records, tweak the format to use percentage directive
    message_format = message_format[:-1] + ':.2%}'

    total = sum(DNS_QUERY_DOMAINS.values())
    for name, count in DNS_QUERY_DOMAINS.most_common():
        print message_format.format(name, count, float(count) / float(total))

    print

def init(google_ips, inspect_google_ip):
    global GOOGLE_IP_ADDRESSES
    global INSPECT_GOOGLE_IP

    if not google_ips is None:
        GOOGLE_IP_ADDRESSES = google_ips

    INSPECT_GOOGLE_IP = inspect_google_ip

def print_summary():
    print_google_connection_init_summary()
    print_dns_query_a_summary()
