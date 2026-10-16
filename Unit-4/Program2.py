class Student:
    def __init__(self):
        print("Constructor called")

    def __del__(self):
        print("Destructor called")

# Creating an object
s = Student()

# Deleting the object
del s
