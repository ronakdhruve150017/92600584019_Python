# Program to demonstrate comprehensions

# List comprehension
squares = [x * x for x in range(1, 6)]
print("List comprehension:", squares)

# Dictionary comprehension
square_dict = {x: x * x for x in range(1, 6)}
print("Dictionary comprehension:", square_dict)

# Set comprehension
even_numbers = {x for x in range(1, 11) if x % 2 == 0}
print("Set comprehension:", even_numbers)
