# Program to find the sum of digits of a number

n=int(input("Enter a number: "))
sum=0

while n > 0:
    r=n%10
    sum=sum+r
    n =int(n/10)

print("Sum of digits =", sum)
