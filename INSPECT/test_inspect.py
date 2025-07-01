import asyncio
import inspect

def sync_function():
    for i in range(5):
        print(f"Sync iteration {i}")

async def async_function():
    for i in range(5):
        print(f"Async function :{i}")
        await asyncio.sleep(2)


async def is_async_function(func):
    """execute the input function"""
    if inspect.iscoroutinefunction(func):
        await func()
    else:
        func()



async def main():
    print("Testing sync function")
    await is_async_function(sync_function)

    print("Testing async function")
    await is_async_function(async_function)

  


if __name__ == "__main__":
    asyncio.run(main())

    # main()
