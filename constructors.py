class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, I am {self.name}")


x = Person("John")
print(x.name)
x.talk()