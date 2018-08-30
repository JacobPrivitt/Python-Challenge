#read by line

def readingLines():
    count = 0

    try:
        with open('people.txt') as file_object:
            contents = file_object.readlines()
            for line in contents:
                count += 1
                print("Line " + str(count) + ": " + line)
    except OSError as booboo:
         
          print("We had a booboo!!")
          print(booboo)
        

def readingLinesAndSearch():

    try:
        with open('people.txt') as file_object:
            contents = file_object.readlines()
            for line in contents:
                if line.rstrip() == "ethan":
                    print("We found ethan!\n")
                else:
                    print(line)

    except OSError as snafu:

        print("We had a bit of a snafu!!")
        print(snafu)
        
readingLinesAndSearch()
