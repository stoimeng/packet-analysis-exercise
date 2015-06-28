#!/usr/bin/env python

from packet_data import run
from packet_analysis import print_summary

def main():
    port = 8000
    address = 'localhost'
    connections = 10

    run(address, port, connections)
    print_summary()

if __name__ == '__main__':
    main()
