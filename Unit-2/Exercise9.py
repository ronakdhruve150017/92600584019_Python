# Program to demonstrate iterables and iterators

numbers = [10, 20, 30, 40, 50]

# List is an iterable
print("Iterable:", numbers)

# Convert iterable into an iterator
iterator = iter(numbers)

print("Iterator values:")
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
