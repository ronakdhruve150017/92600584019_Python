class Student:
    college = "MU College"

    def show(self):       # Instance method
        print("Hello Ronak")

    @classmethod
    def college_name(cls):  # Class method
        print(cls.college)

    @staticmethod
    def msg():            # Static method
        print("Welcome to Goa Singham")

s = Student()

s.show()
Student.college_name()
Student.msg()
