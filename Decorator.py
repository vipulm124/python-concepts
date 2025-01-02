# Python decorator is used to add new functionality to an existing object without modifying its structure.
# the decorator gets a function as an input, and provides the feature to execute that function at will

def example_decorator(func):
    def wrapperFunction():
        print("Before function call")
        func()
        print("After function call")
    return wrapperFunction

@example_decorator
def say_hello():
    print("Hello")

say_hello()

