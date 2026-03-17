import math

x = 1 # integer
y = 3.14 # float
z = 2 + 3j # complex number

print(10 / 3) # division; returns a float
print(10 // 3) # floor division; returns an integer
print(10 % 3) # modulus; returns the remainder of the division
print(10 ** 3) # exponentiation; returns 10 raised to the power of 3

print(round(3.14159, 2)) # rounds the number to 2 decimal places
print(abs(-5)) # returns the absolute value of the number
print(pow(2, 3)) # returns 2 raised to the power of 3
print(max(1, 2, 3)) # returns the maximum value among the arguments
print(min(1, 2, 3)) # returns the minimum value among the arguments
print(sum([1, 2, 3])) # returns the sum of the numbers in the list
print(len(str(12345))) # converts the number to a string and returns its length (number of digits)

print(math.ceil(3.14)) # returns the smallest integer greater than or equal to 3.14 (which is 4)
print(math.sqrt(16)) # returns the square root of 16
print(math.sin(math.pi / 2)) # returns the sine of pi/2 radians (which is 1)
print(math.cos(0)) # returns the cosine of 0 radians (which is 1)
print(math.tan(math.pi / 4)) # returns the tangent of pi/4 radians (which is 1)
print(math.log(100, 10)) # returns the logarithm of 100 to the base 10 (which is 2)
print(math.factorial(5)) # returns the factorial of 5 (which is 120)

x = input("Enter x: ") # input() returns a string
print(type(x)) # prints the type of x (which is <class 'str'>)
x = int(x) # converts the string to an integer
print(type(x)) # prints the type of x (which is <class 'int'>)

# Falsy values in Python include: 0, 0.0, 0j, '', [], {}, set(), None, and False. All other values are considered truthy.