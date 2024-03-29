from collections import *

""" They allow you to create immutable groups of objects.
This means that once a tuple is created, it can't be
modified. You can't add or remove items.
 """

""" They are created in a way similar to lists, but using
parentheses instead of square brackets: """

names = ("Roger", "Syd", "David")
print(names)
print(type(names))

""" A tuple is ordered, like a list, so you can get its values
referencing an index value: """

names[0]
# "Roger"
names[1]
# "Syd"

print(names.index("Roger"))
# 0
print(names.index("Syd"))
# 1

print(names[-1])
# David

print(len(names))
# 3

print("Roger" in names)
# True

print(names[0:2])
# ('Roger', 'Syd')
print(names[1:])
# ('Syd','David')


""" You can create a sorted version of a tuple using the
sorted() global function: """

namesSorted = sorted(names)
print(names)
print(namesSorted)

""" You can create a new tuple from existing tuples using
the + operator: """
newTuple = names + ("Vanille", "Tina")
print(newTuple)

""" empty tuple """
t2 = ()
print(type(t2))


Stats = namedtuple("Stats", ["cells","domains"])
stats = Stats(10,100)
print(stats)
