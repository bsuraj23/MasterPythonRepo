class Employee:
    company_name = "ETC Solutions"   # Class (static) variable

    def __init__(self, name):
        self.name = name             # Instance variable

    def show_details(self):
        print(f"Name: {self.name}, Company: {self.company_name}")

    @staticmethod
    def show_company_info():
        print(f"[Static Method] Company: {Employee.company_name}")


# Create 2 objects
emp1 = Employee("Ajay")
emp2 = Employee("Amit")

# Accessing class variable from objects
emp1.show_details()     # ETC Solutions
emp2.show_details()     # ETC Solutions

# Update class variable from class itself
Employee.company_name = "New ETC"

# Both objects reflect updated class variable
emp1.show_details()     # New ETC
emp2.show_details()     # New ETC

# Shadowing: create instance variable 'company_name' for emp1 only
emp1.company_name = "Custom Co"

# Now emp1 has its own company_name, emp2 still uses class variable
print("\nAfter shadowing:")
emp1.show_details()     # Custom Co
emp2.show_details()     # New ETC

# Static method call
Employee.show_company_info()  # New ETC
emp1.show_company_info()      # Also valid
