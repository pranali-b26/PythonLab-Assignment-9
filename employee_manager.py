class Employee:
    def __init__(self, name, age, salary, address):
        self.name = name
        self.age = age
        self.salary = salary
        self.address = address

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Address:", self.address)


class Manager(Employee):
    pass   # Inherits everything from Employee


# Main program
managers = []

for i in range(2):   # change to 10 in exam
    print("\nEnter details of Manager", i+1)
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    salary = float(input("Enter salary: "))
    address = input("Enter address: ")

    m = Manager(name, age, salary, address)
    managers.append(m)

print("\nManager Details:")
for m in managers:
    m.display()