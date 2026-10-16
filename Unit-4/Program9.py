f = open("demo.txt", "w")
f.write("Hello Python\n")
f.close()

# Append data
f = open("demo.txt", "a")
f.write("Welcome to file handling")
f.close()

# Read data
f = open("demo.txt", "r")
print(f.read())
f.close()
