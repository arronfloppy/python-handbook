""" dictionaries allow you to create collections of key /
value pairs.
Here is a dictionary example with one key/value pair: """

dog = {'name': 'Roger'}
print(type(dog))

""" The key can be any immutable value like a string, a
number or a tuple. The value can be anything you
want. """

""" A dictionary can contain multiple key/value pairs: """
dog = {'name': 'Roger', 'age': 8}
print(dog['age'])
print(dog['name'])

dog['name'] = "Syd"
print(dog['name'])

""" And another way is using the get() method, which
has an option to add a default value: """
print(dog.get('name'))
# 'Roger'
print(dog.get('test', 'default'))
# 'default'

""" The pop() method retrieves the value of a key, and
subsequently deletes the item from the dictionary: """
dog.pop('name')
# 'Roger'

""" The popitem() method retrieves and removes the
last key/value pair inserted into the dictionary: """
print(dog.popitem())

""" You can check if a key is contained into a dictionary
with the in operator: """

print('name' in dog)
# True

# Get a list with the keys in a dictionary
print(list(dog.keys()))

""" Get the values using the values() method, and the
key/value pairs tuples using the items() method """

print(list(dog.values()))
# ['Roger', 8]
print(list(dog.items()))
# [('name', 'Roger'), ('age', 8)]

# Get a dictionary length using the len() global function,
print(len(dog))

# add a new key/value pair
dog['favorite food'] = 'Meat'

# To copy a dictionary, use the copy() method:
dogCopy = dog.copy()


