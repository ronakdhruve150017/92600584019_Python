f = open("demo.txt", "w+")
f.write("Hello Python")

print("Position:", f.tell())

f.seek(0)
print("Data:", f.read())

print("Position:", f.tell())

f.seek(6)
print("Data:", f.read())

f.close()
