""" In Python we have 2 kinds of loops: while loops and
for loops """


# while loops

""" while loops are defined using the while keyword,
and they repeat their block until the condition is
evaluated as False """

condition = True
while condition is True:
    print("The condition is True")
    # break the infinite loop
    break


condition = True
while condition:
    print("The condition is True")
    condition = False

print("After the loop")


count = 0
while count < 10:
    print("The condition is True")
    count = count + 1
print("After the loop")


# for loops
# iterate lists
items = [1, 2, 3, 4]
for item in items:
    print(item)


# iterate with range
for item in range(4):
    print(item)


""" range(4) creates a sequence that starts from 0 and
contains 4 items: [0, 1, 2, 3] . """

""" To get the index, you should wrap the sequence into
the enumerate() function """


items = [1, 2, 3, 4]
for index, item in enumerate(items):
    print(index, item)


# Break and continue

""" Both while and for loops can be interrupted inside
the block, using two special keywords: break and
continue .
continue stops the current iteration and tells Python
to execute the next one.
break stops the loop altogether, and goes on with the
next instruction after the loop end.
The first example here prints 1, 3, 4 . The second
example prints 1 : """


items = [1, 2, 3, 4]
for item in items:
    if item == 2:
        continue
    print(item)

items = [1, 2, 3, 4]
for item in items:
    if item == 2:
        break
    print(item)
