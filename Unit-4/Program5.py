class A:
    def show(self):
        print("Class A")

class B(A):
    pass

b = B()
b.show()


# Multilevel Inheritance
class C:
    def display(self):
        print("Class C")

class D(C):
    pass

class E(D):
    pass

e = E()
e.display()


# Multiple Inheritance
class F:
    def one(self):
        print("Class F")

class G:
    def two(self):
        print("Class G")

class H(F, G):
    pass

h = H()
h.one()
h.two()
