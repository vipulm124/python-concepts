from functools import wraps

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# our decorator
def sample_decorator(func):
    @wraps(func)
    # decorator wrapper function, which will print statement before and after the execution of func
    def my_wrapper():
        print("I'm going to execute this function now")
        result = func()
        print("I'm done executing this function")
        return result

    return my_wrapper

# calling decorators
@sample_decorator
def sample() -> User:
    print("I'm inside the function now")
    new_user = User("Vipul", 34)
    print(f"I have created a user obj, will return it now: {new_user.name}")
    return new_user


new_user = sample()
print(f"Name: {new_user.name}. Age: {new_user.age}")