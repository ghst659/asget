#!/usr/bin/env python3

import sys

import get

def main(targets):
    pages = dict(get.fetch(url) for url in targets)
    get.report(pages)

if __name__ == '__main__':
    main(sys.argv[1:])
