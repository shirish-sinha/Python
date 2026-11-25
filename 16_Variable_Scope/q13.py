for i in range(3):
    print(i)

print(i)
num = [ i for i in range(5)]

print(i)
# A normal for loop in Python does not create a separate scope, so its loop variable remains accessible after the loop finishes. However, in Python 3, list comprehensions have their own scope, so their iteration variable does not overwrite a variable with the same name outside the comprehension.