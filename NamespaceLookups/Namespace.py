# Global variable
x = 10

# Global function
def foo():
    print("Inside foo")

# Accessing the global namespace
global_namespace = globals()

# Printing the global namespace
print(global_namespace)

# Accessing global variables and functions using the global namespace
print(global_namespace['x'])  # Output: 10
global_namespace['foo']()     # Output: Inside foo

global_namespace['x'] = 33
print(global_namespace['x']) # Output: 33