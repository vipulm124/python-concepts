import time
import asyncio

class TokenBucket:
    def __init__(self, capacity, refill_rate_per_second):
        self.capacity = capacity
        self.refill_rate_per_second = refill_rate_per_second
        self.token = capacity
        self.last_refill_time = time.time()
    

    async def _refill(self):
        now = time.time()
        elapsed_time = now - self.last_refill_time
        tokens_to_add = elapsed_time * self.refill_rate_per_second
        self.token = int(self.token + tokens_to_add)

    async def allow_request(self, request_count):
        await self._refill()
        if self.token >= 1:
            self.token = self.token - 1
            print(f"Request {request_count} Allowed. Current token count: {self.token}")
            return True
        else:
            print(f"Request {request_count} Denied - No tokens. Current token count: {self.token}")
            return False
    


async def main_coroutine_handler():
    tokenBucket  = TokenBucket(4, 1)

    tasks = []
    for i in range(10):
        coro =tokenBucket.allow_request(i)
        tasks.append(coro)
    results = await asyncio.gather(*tasks)
    print(results)


asyncio.run(main_coroutine_handler())

    # if tokenBucket.allow_request():
    #     print(f"Request {i+1}: Allowed")
    # else:
    #     print(f"Request {i+1}: Denied - No tokens")
    # time.sleep(1.5)
        
