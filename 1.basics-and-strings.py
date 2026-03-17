print("Hello, World!")
# snake_case is a convention for variable names in Python
star_length = 30
print("*" * star_length)

# use triple quotes for multi-line strings
multi_line_string = """This is a multi-line string.
It can span multiple lines."""
print(multi_line_string)
print("*" * star_length)

print(len(multi_line_string))  # prints the length of the string
print(multi_line_string[0])  # prints the first character of the string
print(multi_line_string[-1])  # prints the last character of the string
print(multi_line_string[0:4])  # prints the first four characters of the string
print(multi_line_string[5:])  # prints the string from the 5th character to the end
print(multi_line_string[:5])  # prints the first five characters of the string
print(multi_line_string[:])  # prints a copy of the entire string
print(multi_line_string[::2])  # prints every second character
print(multi_line_string[::-1])  # prints the string in reverse

first_name = "John"
last_name = "Doe"
full_name = f"{first_name} {last_name}"  # formatted-string for string interpolation; {} can contain any valid Python expression
print(full_name)

# string methods
print(full_name.upper())  # converts the string to uppercase; does not modify the original string
print(full_name.lower())  # converts the string to lowercase; does not modify the original string
print(full_name.title())  # converts the first character of each word to uppercase; does not modify the original string
print(full_name.strip())  # removes leading and trailing whitespace; does not modify the original string
print(full_name.replace("John", "Jane"))  # replaces "John" with "Jane"; does not modify the original string
print(full_name.split())  # splits the string into a list of words; does not modify the original string
print(full_name.find("Doe"))  # returns the index of the first occurrence of "Doe"; returns -1 if not found
print(full_name.startswith("John"))  # returns True if the string starts with "John"; otherwise, returns False
print(full_name.endswith("Doe"))  # returns True if the string ends with "Doe"; otherwise, returns False
print(full_name.count("o"))  # returns the number of occurrences of "o" in the string
print("John" in full_name)  # returns True if "John" is a substring of full_name; otherwise, returns False
print("John" not in full_name)  # returns True if "John" is not a substring of full_name; otherwise, returns False
print(full_name.isalpha())  # returns True if all characters in the string are alphabetic; otherwise, returns False
print(full_name.isdigit())  # returns True if all characters in the string are digits; otherwise, returns False
print(full_name.isalnum())  # returns True if all characters in the string are alphanumeric; otherwise, returns False