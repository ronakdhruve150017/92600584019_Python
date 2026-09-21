# Program to demonstrate generator function and yield

def generate_numbers(n):
    for i in range(1, n + 1):
        yield i

print("Generated sequence:")

for num in generate_numbers(10):
    print(num)
