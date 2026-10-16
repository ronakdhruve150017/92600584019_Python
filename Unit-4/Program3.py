class Student:
    college = "MU College"  # Class variable

    def __init__(self, name, age):
        self.name = name      # Instance variable
        self.age = age        # Instance variable

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("College:", Student.college)

# Creating objects
s1 = Student("Ronak", 20)
s2 = Student("Dhruval", 21)

# Displaying details
s1.display()
print()
s2.display()
