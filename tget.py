#!/usr/bin/env python3

import concurrent.futures
import sys

import get

def main(targets):
    with concurrent.futures.ThreadPoolExecutor() as pool:
        futures = list(pool.submit(get.fetch, url) for url in targets)
    pages = dict(f.result() for f in futures)
    get.report(pages)

if __name__ == '__main__':
    main(sys.argv[1:])
