# The function def countWords(string) that returns a count of all words in the string string.
# Words are separated by spaces. For example, countWords("Mary had a little lamb") should return 5.
"""
Created on Wed Feb  8 16:07:47 2023

@author: dewitt
"""


def main():
    inputStr = input("Enter a string: ")
    inputStrWordCount = countWords(inputStr)
    print("The string contains", inputStrWordCount, "words")


def countWords(string):
    # Remove any leading or trailing spaces to make counting easier.
    string = string.strip()

    # Handle the empty string as a special case.
    if string == "":
        count = 0
        return count

    # Count the spaces to count the number of words.
    count = 1
    for ch in string:
        if ch == " ":
            count = count + 1
    return count


main()
