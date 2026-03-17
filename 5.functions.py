def greet(name):
    print(f"Hello, {name}!")


greet("Alice")

# 2 types of functions: 
# 1. one which just performs a specific task
# 2. one which also returns a value

def get_greeting(name):
    return f"Hello, {name}!"

greeting = get_greeting("Bob")
# print(greeting)
file = open("greeting.txt", "w")
file.write(greeting)
file.close()

print(greet("Charlie"))  # This will print the greeting and then print None, since greet() does not return a value.

def increment(number, by=1):
    return number + by


# by is an optional parameter with a default value of 1. optional parameters are defined at the end of the parameter list.
print(increment(5))  # This will return 6, since the default value of 'by' is 1.
print(increment(5, by=2))  # This will return 7, since

# This will print the tuple of numbers passed to the function.
# tuples (similar to lists) are immutable, so we cannot modify the numbers inside the function, but we can perform operations on them or return a new tuple if needed.
def multiply(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

print(multiply(2, 3, 4))  # This will print 24