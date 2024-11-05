import asyncio

async def worker():
    print('Worker coroutine started')
    await asyncio.sleep(10)
    print('Worker coroutine ended')

loop = asyncio.get_event_loop()
loop.run_until_complete(worker())
loop.close()

print('Main program continues')