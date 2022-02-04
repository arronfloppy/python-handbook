""" We can say they work like tuples, but they are not
ordered, and they are mutable. Or we can say they
work like dictionaries, but they don't have keys.
They also have an immutable version, called
frozenset . """

""" You can create a set using this syntax: """
names = {"Roger", "Syd"}

# You can intersect two sets:
set1 = {"Roger", "Syd"}
set2 = {"Roger"}
intersect = set1 & set2 #{'Roger'}
# You can create a union of two sets:
set1 = {"Roger", "Syd"}
set2 = {"Luna"}
union = set1 | set2
#{'Syd', 'Luna', 'Roger'}

# You can get the difference between two sets:

set1 = {"Roger", "Syd"}
set2 = {"Roger"}
difference = set1 - set2 #{'Syd'}
# You can check if a set is a superset of another (and of
# course if a set is a subset of another)
set1 = {"Roger", "Syd"}
set2 = {"Roger"}
isSuperset = set1 > set2
# TRUE

""" You can count the items in a set with the len()
global function: """
names = {"Roger", "Syd"}
len(names) # 2
""" You can get a list from the items in a set by passing
the set to the list() constructor: """
names = {"Roger", "Syd"}
list(names) #['Syd', 'Roger']
""" You can check if an item is contained into a set with
the in operator: """
print("Roger" in names)
# True
