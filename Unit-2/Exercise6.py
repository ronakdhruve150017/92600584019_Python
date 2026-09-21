# Program to iterate over lists, strings, and dictionaries

# List
numbers = [10, 20, 30, 40, 50]

print("List:")
for num in numbers:
    print(num)

# String
name = "Python"

print("\nString:")
for ch in name:
    print(ch)

# Dictionary
student = {
    "name": "Rahul",
    "age": 22,
    "course": "MCA"
}

print("\nDictionary:")
for key, value in student.items():
    print(key, ":", value)
