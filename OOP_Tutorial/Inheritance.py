class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name,age)
        self.color = color

    def speak(self):
        print(f"I am {self.name}, Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age}, and I am {self.color}")

class Dog(Pet):
    def speak(self):
        print("Bark")


p = Pet("Clark", 34)
p.show()
c = Cat("Clarky", 5, "White")
c.speak()
d = Dog("Chuck", 7)
d.speak()
c1 = Cat("Sharky", 3, "Black")
c1.show()