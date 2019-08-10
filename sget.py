#!/usr/bin/env python3

import requests
import sys

def fetch(url):
    sys.stdout.write(f'Fetch {url} ... ')
    return requests.get(url).text

def main(targets):
    pages = {}
    for url in targets:
        html = fetch(url)
        sys.stdout.write('done\n')
        pages[url] = html
    sum = 0
    for url in sorted(pages):
        size = len(pages[url])
        print(url, size)
        sum += size
    print('Total', sum)

if __name__ == '__main__':
    main(sys.argv[1:])