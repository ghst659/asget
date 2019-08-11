#!/usr/bin/env python3

import requests
import sys

def fetch(url):
    sys.stdout.write(f'Fetch {url} ... ')
    html = requests.get(url).text
    sys.stdout.write('done\n')
    return (url, html)

def report(pages):
    sum = 0
    for url in sorted(pages):
        size = len(pages[url])
        print(url, size)
        sum += size
    print('Total', sum)
