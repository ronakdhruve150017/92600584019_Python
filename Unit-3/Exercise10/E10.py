import re

# Open and read the text file
with open("data.txt", "r") as file:
    text = file.read()

# Extract names
names = re.findall(r"Student Name:\s*(.*)", text)

# Extract email addresses
emails = re.findall(r"[\w\.-]+@[\w\.-]+\.\w+", text)

# Extract 10-digit phone numbers
phones = re.findall(r"\b\d{10}\b", text)

# Display extracted information
print("----- EXTRACTED INFORMATION -----")

print("\nStudent Names:")
for name in names:
    print(name)

print("\nEmail Addresses:")
for email in emails:
    print(email)

print("\nPhone Numbers:")
for phone in phones:
    print(phone)
