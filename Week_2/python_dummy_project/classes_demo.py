# Classes, inheritance and basic magic (dunder) methods.

class Animal:
    """Base (parent) class."""

    def __init__(self, name, age):       # magic method: constructor
        self.name = name
        self.age = age

    def speak(self):
        return f"{self.name} makes a sound"

    def __str__(self):                   # magic method: print(obj)
        return f"{self.__class__.__name__}(name={self.name}, age={self.age})"

    def __repr__(self):                  # magic method: debugging representation
        return f"{self.__class__.__name__}({self.name!r}, {self.age!r})"

    def __eq__(self, other):             # magic method: ==
        return self.name == other.name and self.age == other.age

    def __len__(self):                   # magic method: len(obj)
        return len(self.name)

    def __add__(self, other):            # magic method: +
        return f"{self.name} & {other.name}"


class Dog(Animal):
    """Child class: inherits everything from Animal."""

    def __init__(self, name, age, breed):
        super().__init__(name, age)      # call the parent's constructor
        self.breed = breed

    def speak(self):                     # method overriding
        return f"{self.name} says Woof!"


class Cat(Animal):
    """Another child class overriding speak()."""

    def speak(self):
        return f"{self.name} says Meow!"


if __name__ == "__main__":
    d = Dog("Bruno", 3, "Labrador")
    c = Cat("Misty", 2)

    print(d)                             # __str__
    print(repr(c))                       # __repr__
    print(d.speak())                     # overridden method
    print(c.speak())
    print(len(d))                        # __len__
    print(d + c)                         # __add__
    print(d == Dog("Bruno", 3, "Lab"))   # __eq__
    print(isinstance(d, Animal))         # True: a Dog is an Animal
