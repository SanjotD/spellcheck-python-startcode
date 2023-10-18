# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import math


def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    # Print first 50 values of each list to verify contents
    print(dictionary[0:50])
    print(aliceWords[0:50])

    # Menu
    loop = True
    while loop:
        userSelect = menuSelect()

        if userSelect == "1":
            checkLin(dictionary)
        elif userSelect == "2":
            checkBin(dictionary)
        elif userSelect == "3":
            aliceLin(dictionary, aliceWords)
        elif userSelect == "4":
            aliceBin(dictionary, aliceWords)
        elif userSelect == "5":
            print("\n bye bye\n")
            loop = False
         
# end main()

def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()


# Linear and Binary Search Functions
    # Linear
def linearSearch(anArray, item):
    for i in range(len(anArray)):
        if (anArray[i] == item):
            return i
   
    return -1
    # Binary
def binarySearch(anArray, item):
    li = 0
    ui = len(anArray)-1

    while li <= ui:
        mi = math.floor((li + ui) // 2)
        if anArray[mi] == item:
            return mi
        elif item < anArray[mi]:
            ui = mi - 1
        else:
            li = mi + 1
    return -1

# Menu Functions 
def menuSelect():
    print("\n SPELL CHECK MAIN MENU")
    print("1. Spell Check a Word (Linear)")
    print("2. Spell Check a Word (Binary)")
    print("3. Spell Check Alice in Wonderland (Linear)")
    print("4. Spell Check Alice in Wonderland (Binary)")
    print("5. Exit")
    return input ("\nEnter Opt (#):")

    # Spell Check (Linear)
def checkLin(dictionary):
    userWord = input("\nPlease enter a word: ")
    print("Linear Search Starting...")
    userWord = userWord.lower()
    if (linearSearch(dictionary, userWord)) != -1:
        print(f"\n{userWord} is IN the dictionary at position {linearSearch(dictionary, userWord)}.")
    else:
        print(f"\n{userWord} is NOT IN the dictionary. ")
    # Spell Check (Binary)
def checkBin(dictionary):
    userWord = input("\nPlease enter a word: ")
    print("Binary Search Starting...")
    userWord = userWord.lower()
    if (binarySearch(dictionary, userWord)) != -1:
        print(f"\n{userWord} is IN the dictionary at position {binarySearch(dictionary, userWord)}.")
    else:
        print(f"\n{userWord} is NOT IN the dictionary. ")
    # Alice in Wonderland (Linear)
def aliceLin(dictionary, aliceWords):
    # loop, count for each -1
    print("Spell Check Alice in Wonderland (Linear)")
    notFoundCount = 0
    for i in range(len(aliceWords)):
        if (linearSearch(dictionary, aliceWords[i])) == -1:
            notFoundCount = notFoundCount + 1
    print(f"Search: {notFoundCount} ")
            
"""    else:
        print(f"is NOT IN the dictionary. ")"""
    # Alice in Wonderland (Binary)
def aliceBin(dictionary, aliceWords):
    print("Spell Check Alice in Wonderland (Binary)")


# Call main() to begin program
main()
