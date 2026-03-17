temperature = int(input("What is the temperature outside? "))
if temperature > 30:
    print("It's hot outside!")
elif temperature > 20:
    print("It's warm outside!")
elif temperature > 10:
    print("It's cool outside!")
else:
    print("It's cold outside!")
print("Have a nice day!")

# ternary operator (conditional expression)
is_raining = True
weather = "rainy" if is_raining else "sunny"
print(f"The weather is {weather}.")

age = 22
if 18 <= age < 65: #chaining comparison operators; equivalent to (age >= 18) and (age < 65)
    print("You are an adult.")