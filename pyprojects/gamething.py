#Simple Game

import time

#define functions

def displayLesson():
    time.sleep(1)
    print('''
This is a multiline text string
I can write across lines. Pretty crazy.
Remember to use triple quotes.

The progam has ended...''')

def useTime():
    print("Shut down requested.")
    time.sleep(1)
    print("3 seconds to shutdown...")
    time.sleep(2)
    print("Going offline...")

def flowControl():
    answer = input("Do you want to leran about multiline text strings, enter yes or y?")
    if answer == ("yes" or "y"):
        displayLesson()
    else:
        useTime()
        print("End program")

#execute program:
flowControl()
