import asyncio
from functools import wraps

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def async_sample_decorator(func):
    @wraps(func)
    async def async_my_wrapper():
        print("I'm going to execute this function now")
        if asyncio.iscoroutinefunction(func):
            result = await func()
        else:
            result = func()
        print("I'm done executing this function")
        return result

    return async_my_wrapper

@async_sample_decorator
async def sample() -> User:
    print("I'm inside the function now")
    new_user = User("Vipul", 34)
    print(f"I have created a user obj, will return it now: {new_user.name}")
    return new_user


@async_sample_decorator
def sample2() -> User:
    print("I'm inside the function now")
    new_user = User("Malhotra", 34)
    print(f"I have created a user obj, will return it now: {new_user.name}")
    return new_user


async def main():
    new_user = await sample()
    print(f"Name: {new_user.name}. Age: {new_user.age}")

    new_user2 = await sample2()
    print(f"Name: {new_user2.name}. Age: {new_user2.age}")

asyncio.run(main())