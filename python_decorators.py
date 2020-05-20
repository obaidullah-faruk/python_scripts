

def decorator_function(original_function):
    print("H! from me")
    def wrapper_function():
        print("H! from wrapper")
        return original_function()
    print("H! from decorator")
    return wrapper_function

@decorator_function
def display():
    print("Display functuon run.")

# display = decorator_function(display)
display()