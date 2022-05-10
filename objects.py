""" Everything in Python is an object.
Even values of basic primitive types (integer, string,
float..) are objects. Lists are objects, tuples,
dictionaries, everything.
Objects have attributes and methods that can be
accessed using the dot syntax """


""" age now has access to the properties and methods
defined for all int objects """
age = 8


print(age.real)
# 8
print(age.imag)
# 0
print(age.bit_length())
# 4
# the bit_length() method returns the number of bits

""" A variable holding a list value has access to a different
set of methods: """


items = [1, 2]
items.append(3)
items.pop()

""" The id() global function provided by Python lets you
inspect the location in memory for a particular object. """


print(id(age))
# Ex: 140170065725376

""" If you assign a different value to the variable, its
address will change, because the content of the
variable has been replaced with another value stored
in another location in memory: """


age = 8
print(id(age))
# Ex: 140535918671808

age = 9
print(id(age))
# Ex: 140535918671


""" But if you modify the object using its methods, the
address stays the same: """


items = [1, 2]
print(id(items))
# 140093713593920
items.append(3)
print(items)
# [1, 2, 3]
print(id(items))
# 140093713593920


""" The address only changes if you reassign a variable to
another value.
Some objects are mutable, some are immutable. This
depends on the object itself. If the object provides
methods to change its content, then it's mutable.
Otherwise it's immutable. Most types defined by
Python are immutable. For example an int is
immutable. There are no methods to change its value.
If you increment the value using """


age = 8
print(id(age))
age = age + 1
print(id(age))
# or


age += 1
print(id(age))

# age points to a different memeory location
