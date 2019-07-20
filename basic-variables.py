#! /usr/bin/python3

stringVar = "This is a string."

integerVar = 84

floatVar = 3.38

listVar = [1, 2, 3, 4, 5]

dictionaryVar = {'name': 'John', 'age': 27}

"""
Example comment. Changing John's age.
"""
dictionaryVar['age'] = 34

"""
Changing again.
"""
dictionaryVar.update({'age': 31})

print ("String: " + stringVar)

print ("Integer: " + str(integerVar))

print ("Float: " + str(floatVar))

print ("List: " + str(listVar))

print ("List first element: " + str(listVar[0]))

print ("Dictionary: " + str(dictionaryVar))

print ("Dictionary element 'name': " + dictionaryVar['name'])

