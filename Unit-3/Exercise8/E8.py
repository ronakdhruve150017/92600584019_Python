import re

print("======================================")
print("   BASIC REGULAR EXPRESSION MATCHING")
print("======================================")

text = "My name is Ronak and my phone number is 9876543210."

# 1. Search for a word
pattern = r"Ronak"
result = re.search(pattern, text)

if result:
    print("\n1. Word found:", result.group())
else:
    print("\n1. Word not found")


# 2. Match a pattern at the beginning of the string
pattern = r"My"
result = re.match(pattern, text)

if result:
    print("2. Pattern matched at beginning:", result.group())
else:
    print("2. Pattern not found at beginning")


# 3. Find all numbers
pattern = r"\d+"
result = re.findall(pattern, text)

print("3. Numbers found:", result)


# 4. Find all words starting with 'R'
pattern = r"\bR\w+"
result = re.findall(pattern, text)

print("4. Words starting with R:", result)


# 5. Replace a word
pattern = r"Ronak"
result = re.sub(pattern, "Student", text)

print("5. After replacement:")
print(result)


# 6. Check phone number pattern
phone = "9876543210"
pattern = r"^\d{10}$"

if re.fullmatch(pattern, phone):
    print("6. Valid 10-digit phone number")
else:
    print("6. Invalid phone number")


print("\n======================================")
print("Program completed successfully.")
print("======================================")
