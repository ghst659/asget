#!/usr/bin/env python3

import aiohttp
import asyncio
import sys

import get

async def fetch(session, url):
    sys.stdout.write(f'Fetch {url} ... ')
    async with session.get(url) as response:
        html = await response.text()
    sys.stdout.write('done\n')
    return (url, html)

async def yield_targets(targets):
    for t in targets:
        yield t

async def main(targets):
    pages = {}
    async with aiohttp.ClientSession() as session:
        async for url in yield_targets(targets):
            url, html = await fetch(session, url)
            pages[url] = html
    get.report(pages)

if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())f
    asyncio.run(main(sys.argv[1:]))
