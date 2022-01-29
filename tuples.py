""" They allow you to create immutable groups of objects.
This means that once a tuple is created, it can't be
modified. You can't add or remove items.
 """

""" They are created in a way similar to lists, but using
parentheses instead of square brackets: """

names = ("Roger", "Syd", "David")

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

names[0:2]
# ('Roger', 'Syd')
names[1:]
# ('Syd',)


""" You can create a sorted version of a tuple using the
sorted() global function: """

namesSorted = sorted(names)
print(names)
print(namesSorted)

""" You can create a new tuple from existing tuples using
the + operator: """
newTuple = names + ("Vanille", "Tina")
print(newTuple)
