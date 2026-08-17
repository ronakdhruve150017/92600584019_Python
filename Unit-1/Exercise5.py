print(">>>using indexing, slicing and list comprehension")

print(">>>Creating a list")
numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

print(">>>Indexing")
print("First element:", numbers[0])
print("Third element:", numbers[2])
print("Last element:", numbers[-1])

print(">>>Slicing")
print("First three elements:", numbers[:3])
print("Elements from index 2:", numbers[2:])
print("Middle elements:", numbers[1:4])
print("Reverse List:", numbers[::-1])

print(">>>List manipulation")
numbers.append(60)
print("\nAfter append:", numbers)

numbers.remove(30)
print("After remove:", numbers)

print(">>>List Comprehension")
squares = [x * x for x in numbers]
print("\nSquare List:", squares)

even = [x for x in numbers if x % 2 == 0]
print("Even Numbers:", even)
