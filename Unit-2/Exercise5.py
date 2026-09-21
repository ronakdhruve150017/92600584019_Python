# Program to demonstrate break, continue, and pass

print("Using break:")
for i in range(1, 10):
    if i == 5:
        break
    print(i)

print("\nUsing continue:")
for i in range(1, 10):
    if i == 5:
        continue
    print(i)

print("\nUsing pass:")
for i in range(1, 10):
    if i == 3:
        pass
    print(i)
