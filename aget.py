#!/usr/bin/env python3

import aiohttp
import asyncio
import sys

async def fetch(session, url):
    async with session.get(url) as response:
        sys.stdout.write(f'Fetch {url} ... ')
        return await response.text()

async def yield_targets(targets):
    for t in targets:
        yield t

async def main(targets):
    pages = {}
    async with aiohttp.ClientSession() as session:
        async for url in yield_targets(targets):
            html = await fetch(session, url)
            sys.stdout.write('done\n')
            pages[url] = html
    sum = 0
    for url in sorted(pages):
        size = len(pages[url])
        print(url, size)
        sum += size
    print('Total', sum)

if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())f
    asyncio.run(main(sys.argv[1:]))
