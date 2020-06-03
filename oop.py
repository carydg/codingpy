class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def info(self):
        print(f"I am {self.get_name()} and I am {self.get_age()} years old")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def get_color(self):
        return self.color

    def info(self):
        print(f"I am {self.get_name()}, {self.get_age()} years old and I am {self.get_color()}")

    def speak(self):
        print("meow!")

class Dog(Pet):
    def speak(self):
        print("bark!")

p = Pet("Alice", 10)
p.info()

c = Cat("Ben", 11, "Yellow")
c.info()
c.speak()

d = Dog("Cass", 12)
d.info()
d.speak()