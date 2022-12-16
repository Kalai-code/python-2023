inputStr = "Hello World"

# print the string
print("The string is:",inputStr)

# print the length of the string
print("The Length of the string is:",len(inputStr))

# print the last character of the string
print("The last character of the string is:", inputStr[-1])

# print each character in the string
print("The characters in the string are:")
for ch in inputStr:
    print(ch)

# convert string into list
print("Print string to list:",list(inputStr))

# split the string with space
print("Split the string with space:",inputStr.split())

# find index of a character
print("Find the index of a character", inputStr.index('e'))

# count the number of occurrence of a character
print("Number of occurances of a character:", inputStr.count('l'))

# find character at an index
print("The character at the index:", inputStr[2])

# slicing the string
print("Slicing the string:", inputStr[3:])

#reverse a string
print("Reversing a string", inputStr[::-1])

# print substring of a given string
print("Substring of a given string", inputStr[2:6])