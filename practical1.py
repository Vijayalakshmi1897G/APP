#Required arguements
def student(name, age, division):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Division: {division}")
    
#Keyword arguements
def employee(name, salary):
    print(f"Name: {name}")
    print(f"Salary: {salary}")

#Default arguements
def hello(name):
    print(f"Hello, {name}!")

#Variable-length arguements
def favsubject(*subject):
    print("My favorite subjects are:")
    for sub in subject:
        print(sub)

#Input from user
student(input("Enter name: "), int(input("Enter age: ")), input("Enter division: "))
employee(salary=int(input("Enter salary: ")), name=input("Enter name: "))
hello(input("Enter name: "))
favsubject(input("Enter favorite subjects (comma-separated): ").split(","))