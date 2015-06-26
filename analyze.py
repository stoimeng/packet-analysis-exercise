#!/usr/bin/env python

import sys
from collections import Counter

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import *

GOOGLE_IP_ADDRESSES = ['64.233.169.105', '64.233.169.106', '64.233.169.147', '64.233.169.99', '64.233.169.103', '64.233.169.104']
GOOGLE_CONNECTION_INIT_SOURCE_PORTS = set()
DNS_QUERY_DOMAINS = Counter()

def is_google_connection_init(packet):
	if packet.haslayer(TCP):
		ip = packet[IP]
		tcp = ip[TCP]
		if tcp.flags == 2 and tcp.dport == 80 and ip.dst in GOOGLE_IP_ADDRESSES:
			return True

	return False

def handle_google_connection_init(packet):
	if is_google_connection_init(packet):
		GOOGLE_CONNECTION_INIT_SOURCE_PORTS.add(packet[TCP].sport)

def is_dns_query_a(packet):
	if packet.haslayer(DNSQR) and packet[DNSQR].qtype == 1 and packet[DNS].qr == 0:
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

	message_format = '{:20} | {:5} | {}'

	message = message_format.format('name', 'count', 'percentage of total')
	print message
	print '-' * len(message)

	# for records, tweak the format to use percentage directive
	message_format = message_format[:-1] + ':.2%}'

	total = sum(DNS_QUERY_DOMAINS.values())
	for name, count in DNS_QUERY_DOMAINS.most_common():
		print message_format.format(name, count, float(count) / float(total))

	print

def print_summary():
	print_google_connection_init_summary()
	print_dns_query_a_summary()

def analyze_file(file_path):
	packets = rdpcap(file_path)
	for packet in packets:
		handle_packet(packet)

	print_summary()

def analyze_live(interface):
	sniff(iface=interface, prn=lambda p: handle_packet(p))

if __name__ == '__main__':
	analyze_file(sys.argv[1])
