import asyncio


async def background_task():
    for i in range(10):
        print(f"Background task : {i}")
        await asyncio.sleep(0.5)


async def front_task():
    letters = "ABCDEFGHIJ"
    for letter in letters:
        print(f"Fron Task: {letter}")
        await asyncio.sleep(1)


async def main():
    background_task_future = asyncio.create_task(background_task())
    front_task_future = asyncio.create_task(front_task())


    await asyncio.gather(background_task_future, front_task_future)

asyncio.run(main())
