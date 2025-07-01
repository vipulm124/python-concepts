def bar():
    # Local variable
    y = 20
    
    # Accessing the local namespace
    local_namespace = locals()
    
    # Printing the local namespace
    print(local_namespace) # Ouput: {'y': 20}
    
    # Accessing local variables using the local namespace
    print(local_namespace['y'])  # Output: 20

# Calling the function
bar()