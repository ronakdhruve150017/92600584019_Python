import shutil
import os

print("========================================")
print("   COPY, MOVE AND DELETE FILES")
print("========================================")

# Create a source file
source_file = "source.txt"

with open(source_file, "w") as file:
    file.write("This is the source file.")
    
print("\nSource file created:", source_file)

# 1. Copy the file
copy_file = "copy.txt"

shutil.copy(source_file, copy_file)

print("File copied successfully.")
print("Source File :", source_file)
print("Copied File :", copy_file)

# 2. Create a directory for moving the file
destination_dir = "Destination"

if not os.path.exists(destination_dir):
    os.mkdir(destination_dir)

# 3. Move the copied file
moved_file = shutil.move(copy_file, destination_dir)

print("\nFile moved successfully.")
print("Moved File:", moved_file)

# 4. Delete the moved file
if os.path.exists(moved_file):
    os.remove(moved_file)
    print("File deleted successfully.")

# 5. Delete the source file
if os.path.exists(source_file):
    os.remove(source_file)
    print("Source file deleted successfully.")

# 6. Delete the empty directory
if os.path.exists(destination_dir):
    os.rmdir(destination_dir)
    print("Destination directory deleted successfully.")

print("\n========================================")
print("Program completed successfully.")
print("========================================")
