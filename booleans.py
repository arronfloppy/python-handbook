# Python provides the bool type, which can have two values:
# True and False (capitalized)
done = False
done = True

# used with conditional statements
done = True

if done:
    print("done is true")
else:
    print("done is false")


# When evaluating a value for True or False , if the
# value is not a bool we have some rules depending
# on the type we're checking:
# numbers are always True unless for the number 0
# strings are False only when empty
# lists, tuples, sets, dictionaries are False only when empty

# check if a value is boolean
done = True
type(done) == bool
# True

done = True
isinstance(done, bool)
# True

# The global any() function is also very useful when
# working with booleans, as it returns True if any of the
# values of the iterable (list, for example) passed as
# argument are True :
book_1_read = True
book_2_read = False
read_any_book = any([book_1_read, book_2_read])
print(read_any_book)
# True
