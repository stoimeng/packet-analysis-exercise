#!/usr/bin/env python

import sys
import argparse
from packet_data import run
from packet_analysis import init, print_summary

DEFAULT_PORT = 8000
DEFAULT_CONNECTIONS_COUNT = 10

def get_arguments():
    parser = argparse.ArgumentParser(description='Packet analysis challenge solution.')
    file_group = parser.add_argument_group('File required argument group')
    file_group.add_argument('-f', metavar='CAPTURE_FILE', required=True,
            help='A file containing traffic captured in PCAP format')
    parser.add_argument('-d', dest='inspect_google_ip', action='store_false',
            help='Do not inspect packets for www.google.com IP addresses')
    parser.set_defaults(inspect_google_ip=True)
    parser.add_argument('-p', metavar='PORT',  type=int, default=DEFAULT_PORT,
            help='A local port to open for packet data client/server communication')
    parser.add_argument('-c', metavar='COUNT',  type=int,
            default=DEFAULT_CONNECTIONS_COUNT,
            help='Count of packet data client connections')
    parser.add_argument('-g', metavar='IP', nargs='+',
            help='IP addresses of www.google.com')
    return parser.parse_args()

def main():
    args = get_arguments()

    init(args.g, args.inspect_google_ip)
    run('localhost', args.p, args.c, args.f)
    print_summary()

if __name__ == '__main__':
    main()
