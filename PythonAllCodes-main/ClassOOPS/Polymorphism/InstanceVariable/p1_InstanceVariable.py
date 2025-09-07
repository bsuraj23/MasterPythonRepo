class Student:
    def __init__(self, name, grade):
        self.name = name        # instance variable
        self.grade = grade      # instance variable

    def show_details(self):
        print("Name:", self.name)
        print("Grade:", self.grade)

# Create 2 objects
s1 = Student("Suraj", "A++++++++")
s2 = Student("Amit", "B")

# Call methods
s1.show_details()
s2.show_details()
