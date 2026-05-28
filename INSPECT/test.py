# ...existing code...
import asyncio
import threading
import time


def sync_function():
    for i in range(5):
        print(f"[{time.time():.3f}] Sync iteration {i}")
        time.sleep(0.3)


async def async_function():
    for i in range(5):
        print(f"[{time.time():.3f}] Async function :{i}")
        await asyncio.sleep(2)


def _run_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


def start_async_in_background(coro):
    loop = asyncio.new_event_loop()
    t = threading.Thread(target=_run_loop, args=(loop,), daemon=True)
    t.start()
    future = asyncio.run_coroutine_threadsafe(coro, loop)

    # stop the loop once the coroutine is done
    def _stop(_):
        loop.call_soon_threadsafe(loop.stop)
    future.add_done_callback(_stop)

    return future, t


if __name__ == "__main__":
    start = time.time()
    future, thread = start_async_in_background(async_function())

    # This runs synchronously and will NOT wait for async_function to finish
    sync_function()
    print(f"[{time.time():.3f}] sync_function finished (did not wait for async).")

    # Optionally wait for async to finish before exiting (cleanup)
    future.result()  # blocks until async_function completes
    print(f"[{time.time():.3f}] async_function finished.")
# ...existing code...