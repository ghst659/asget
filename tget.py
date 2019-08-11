#!/usr/bin/env python3

import concurrent.futures
import requests
import sys

def fetch(url):
    sys.stdout.write(f'Fetch {url} ... ')
    return requests.get(url).text

def fetcher(pages, url):
    html = fetch(url)
    sys.stdout.write('done\n')
    pages[url] = html

def main(targets):
    pages = {}
    futures = {}
    with concurrent.futures.ThreadPoolExecutor() as pool:
        for url in targets:
            futures[url] = pool.submit(fetcher, pages, url)
    sum = 0
    for url in sorted(pages):
        size = len(pages[url])
        print(url, size)
        sum += size
    print('Total', sum)

if __name__ == '__main__':
    main(sys.argv[1:])
