import re

print("========================================")
print("       REGULAR EXPRESSION FUNCTIONS")
print("========================================")

text = "Python is easy to learn. Python is powerful."

# 1. Using match()
pattern = r"Python"
result = re.match(pattern, text)

print("\n1. Using re.match()")

if result:
    print("Pattern matched:", result.group())
else:
    print("Pattern not found at the beginning.")


# 2. Using search()
pattern = r"easy"
result = re.search(pattern, text)

print("\n2. Using re.search()")

if result:
    print("Pattern found:", result.group())
    print("Starting position:", result.start())
else:
    print("Pattern not found.")


# 3. Using findall()
pattern = r"Python"
result = re.findall(pattern, text)

print("\n3. Using re.findall()")
print("All matching words:", result)
print("Number of matches:", len(result))


print("\n========================================")
print("Program completed successfully.")
print("========================================")
