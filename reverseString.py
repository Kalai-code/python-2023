"""
code to reverse string without using built-in function
"""

def reverseString(inputStr):
    if len(inputStr) > 0:
        reversedStr = ""
        for ch in inputStr:
            reversedStr = ch + reversedStr
        print("Output is:",reversedStr)
    else:
        print("Please enter a valid string")


reverseString("Hello")