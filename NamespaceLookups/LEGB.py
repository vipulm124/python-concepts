def outer():
    message = "Hello from outer"
    
    def inner():
        print(message)  # Accesses the enclosing scope
    
    inner()

outer()  # Output: Hello from outer