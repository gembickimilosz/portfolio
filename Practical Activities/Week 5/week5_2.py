class Customer:
    def __init__(self, name):
        self.name = name

    def role_info(self):
        print(f"I am a customer named {self.name}.")

    def interact(self):
        print("Can you help me find the cereal aisle?")


class Employee:
    def __init__(self, name):
        self.name = name

    def role_info(self):
        print(f"I am an employee named {self.name}.")

    def interact(self):
        print("Let me check the stock levels for aisle 5.")


# Create instances of different roles
customer1 = Customer("Alice")
employee1 = Employee("Bob")

# The robot interacts with both, using polymorphism
for person in (customer1, employee1):
    person.role_info()
    person.interact()
    print("---")