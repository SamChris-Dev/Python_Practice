# class Person:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello, my name is {self.name}!")


# person1 = Person("Alice")
# person1.greet()  # Output: Hello, my name is Alice!

class Person:
    def __init__(self, name, age, height):
        self.name = name  # Instance variable
        self.age = age
        self.height = height


# Create objects with different instance variables
person1 = Person("Alice", 30, 6.4)
person2 = Person("Bob", 25, 6.2)
person3 = Person("Samwel", 32, 6.7)

print(person1.name)  # Output: Alice
print(person1.age)  # Output: 30
print(person1.height)
print(person2.name)  # Output: Bob
print(person2.age)  # Output: 25
print(person2.height)
print(person3.name)
print(person3.height)
print(person3.age)

# Accessing __dict__ (not recommended for regular use)
print(person1.__dict__)  # Output: {'name': 'Alice', 'age': 30}
print(person3.__dict__)
