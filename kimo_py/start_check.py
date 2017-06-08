#!/usr/bin/env python3.6
import urllib.request
import time

ip = '192.168.0.103'
ip = '172.20.10.9'

if __name__ == '__main__':
    req = urllib.request.Request("http://{}:10001/REST/check".format(ip))
    while True:
        urllib.request.urlopen(req)
        time.sleep(600)
