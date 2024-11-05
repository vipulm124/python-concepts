import asyncio

async def background_task():
    for i in range(10):
        print(f"Background task : {i}")
        await asyncio.sleep(1)

async def main():
    task = asyncio.create_task(background_task())

    await task

asyncio.run(main())