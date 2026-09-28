import os
import sys

print("========================================")
print("   FILE AND DIRECTORY OPERATIONS")
print("========================================")

# Display current working directory
print("\nCurrent Working Directory:")
print(os.getcwd())

# Display command-line arguments
print("\nCommand Line Arguments:")
print(sys.argv)

# Create a directory
dirname = "MyFolder"

if not os.path.exists(dirname):
    os.mkdir(dirname)
    print("\nDirectory created:", dirname)
else:
    print("\nDirectory already exists:", dirname)

# Create a file inside the directory
filename = os.path.join(dirname, "sample.txt")

with open(filename, "w") as file:
    file.write("Hello, this is a sample file.\n")
    file.write("This file is created using Python.")

print("File created:", filename)

# Check whether file exists
if os.path.exists(filename):
    print("File exists:", filename)

# Display file size
print("File size:", os.path.getsize(filename), "bytes")

# Read the file
with open(filename, "r") as file:
    print("\nFile Content:")
    print(file.read())

# Rename the file
new_filename = os.path.join(dirname, "new_sample.txt")

os.rename(filename, new_filename)
print("File renamed to:", new_filename)

# List files and directories
print("\nContents of current directory:")
for item in os.listdir():
    print(item)

# Delete the file
os.remove(new_filename)
print("\nFile deleted:", new_filename)

# Remove the directory
os.rmdir(dirname)
print("Directory deleted:", dirname)

print("\n========================================")
print("Program completed successfully.")
print("========================================")

# Exit the program
sys.exit()
