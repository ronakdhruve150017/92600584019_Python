class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(B):
    pass

c = C()
c.show()

print(C.mro())
print(c.__str__())
