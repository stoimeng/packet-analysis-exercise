#!/usr/bin/env python

import sys
from collections import Counter
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
		domain = packet[DNSQR].qname
		DNS_QUERY_DOMAINS[domain] += 1

def handle_packet(packet):
	handle_google_connection_init(packet)
	handle_dns_query_a(packet)

def analyze_file(file_path):
	packets = rdpcap(file_path)
	for packet in packets:
		handle_packet(packet)

	print GOOGLE_CONNECTION_INIT_SOURCE_PORTS
	print DNS_QUERY_DOMAINS

def analyze_live(interface):
	sniff(iface=interface, prn=lambda p: handle_packet(p))

if __name__ == '__main__':
	analyze_file(sys.argv[1])
