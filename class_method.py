
from unicodedata import name


class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("I am Dog self: " + self.name)

class Dog_1(Dog):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("I am Dog_1: " + self.name)

class Dog_jack(Dog):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def jack_dog(self):
        print("This is Jack Dog: " + self.name)

    def jack_race(self):
        print("I am jack running " + self.color)

class Dog_Rohan(Dog_jack):
    def __init__(self, name, color):
        super().__init__(name, color)

    def name(self):
        print("I am name " + self.name)


dog1 = Dog("DOG1")
dog2 = Dog_1("DOG2")
dog3 = Dog_jack("Dog3", "Blue")
dog4 = Dog_Rohan("DOG4", "Black")

dog1.speak()
dog2.speak()
dog3.speak()

dog4.jack_race()