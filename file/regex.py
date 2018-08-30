#RegEx
import re

def regExMagic(pattern, string):

    objectMatch = re.search(pattern, string)
    return objectMatch


def readingLinesWithRegEx():

    try:
        with open('people.txt') as file_object:
            contents = file_object.readlines()
            print('\n')
            for line in contents:
                pattern = 'ethan'
                if str(regExMagic(pattern, line)) == "None":
                    print(line)
                else:
                    print("--> We the text: " + pattern + ", in this location!\n")

    except OSError as booboo:
        print("We had a booboo.")


readingLinesWithRegEx()
