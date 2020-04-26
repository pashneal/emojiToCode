 # -*- coding: utf-8 -*-
import random
import string
import sys
notPrintable = {'🔾', '🔿', '🕀', '🕁', '🕂', '🕃', '🕄', '🕅', '🕆', '🕇', '🕈', '🕨', '🕩', '🕪', '🕫', '🕬', '🕭', '🕮','📾'}
viableCharacters  = [chr(i) for i in range(0x1F300, 0x1F578) if chr(i)
                     not in notPrintable]
viableCharacters  += [chr(i) for i in range(0x1F5ff, 0x1F649) if chr(i) not                      in notPrintable]

print(viableCharacters)
englishSymbols = string.ascii_letters + string.digits
sentence = input("Enter Sentence to encode ")
filename = input("Enter filename to write to ")

f = input("Should capitals also be encoded? (y or n) ")
while f not in "yn":
    print("Please type y or n")
    f = (">> ")
if "n" == f[0]:
    englishSymbols =englishSymbols.replace(string.ascii_uppercase, "")

f = input("Should digits also be encoded? (y or n) ")
while f not in "yn":
    print("Please type y or n")
    f = (">> ")
if "n" == f[0]:
    englishSymbols =englishSymbols.replace(string.digits, "")


while True:
    mapping = {}
    for symbol in englishSymbols:
        mapping[symbol] = random.choice(viableCharacters) 
    finalString = ""
    for key in mapping:
        finalString += key + "\t" + mapping[key]
        finalString += "\n"
    finalString += "\n"
    finalString += sentence
    finalString += "\n"
    for letter in sentence:
        if letter in englishSymbols:
            letter = mapping[letter]
        finalString += letter
    print(finalString)

    fileToWrite = open(filename, "w")
    fileToWrite.write(finalString)
    fileToWrite.close()
    y = input("is this a good encoding? press y to exit")
    if (y == "y"):
        break

