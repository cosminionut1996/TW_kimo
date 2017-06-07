#!/usr/bin/env python3.6
import urllib.request
import time

if __name__ == '__main__':
    req = urllib.request.Request("http://192.168.0.103:10001/REST/check")
    while True:
        urllib.request.urlopen(req)
        time.sleep(60)
