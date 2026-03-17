# range() function is an iterable that generates a sequence of numbers, which can be used in for loops to iterate over a specific range of values.
# iterates over a sequence of numbers from 0 to 2
for number in range(3):
    print("Number:", number, number * '.')

# seperator
print("==" * 20)

# iterates over a sequence of numbers from 1 to 3
for number in range(1, 4):
    print("Number:", number, number * '.')

# seperator
print("==" * 20)

# iterates over a sequence of numbers from 1 to 9 with a step of 2
for number in range(1, 10, 2):
    print("Number:", number, number * '.')

# seperator
print("==" * 20)

# break out of the loop when number is 5
for number in range(1, 10):
    print("Number:", number, number * '.')
    if number == 5:
        print("Breaking out of the loop at number 5.")
        break

# seperator
print("==" * 20)

# for loop with else clause, which executes if the loop completes without encountering a break statement
flag = True
for number in range(1, 5):
    print("Number:", number, number * '.')
    if flag:
        print("Flag is True, breaking out of the loop.")
        break
else:
    print("Loop completed without break.")

# seperator
print("==" * 20)

# nested loops to print a pattern
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i: {i}, j: {j}")
    print("==" * 10)

# seperator
print("==" * 20)

# strings are also iterable, so we can use a for loop to iterate over each character in a string
for char in "Hello":
    print(char)

# seperator
print("==" * 20)

# lists are iterable, so we can use a for loop to iterate over each element in a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# seperator
print("==" * 20)

# while loop to print numbers from 1 to 5
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# seperator
print("==" * 20)

# real world example of a while loop to simulate a CLI
command = ""
while command.lower() != "exit":
    command = input("Enter a command (type 'exit' to quit): ")
    print(f"You entered: {command}")
