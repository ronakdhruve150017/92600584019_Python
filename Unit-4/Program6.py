class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

# Method overriding
a = A()
b = B()

a.show()
b.show()

# Polymorphism
for obj in (a, b):
    obj.show()
