""" In addition to using the Python-provided types, we can
declare our own classes, and from classes we can
instantiate objects.
An object is an instance of a class. A class is the type
of an object. """


class Dog:
    # the Dog class
    def bark(self):
        print('WOF!')


""" self as the argument of the method points to
the current object instance, and must be specified
when defining a method. """


""" We create an instance of a class, an object, using this
syntax: """


roger = Dog()


""" Now roger is a new object of type Dog. """

print(type(roger))

""" A special type of method, __init__() is called
constructor, and we can use it to initialize one or more
properties when we create a new object from that
class: """


class Dog:
    # the Dog class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print('WOF!')


roger = Dog('Roger', 8)
print(roger.name)
# 'Roger'
print(roger.age)
# 8
roger.bark()
# 'WOF!'

""" One important features of classes is inheritance. """


class Animal:
    def walk(self):
        print('Walking..')


""" and the Dog class can inherit from Animal: """


class Dog(Animal):
    def bark(self):
        print('WOF!')


roger = Dog()
roger.walk()
# 'Walking..'
roger.bark()
# 'WOF!'
