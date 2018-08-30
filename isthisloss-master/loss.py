#Jacob Privitt
#Is this loss?

def intro():
    print('''
    Is this loss?
    ''')
    q1()

def q3():
    iii = input("\nIs there one person standoing and another laying in the last fram or bottom right? Yes or no.    ")
    if iii == "yes":
        print("Congratz, it's loss!")
    elif iii == "no":
        print("\nIt's probably not loss. Sorry!")
    else:
        print(iii)

def q2():
    ii = input("\nIs there two people or things in the next two frames? Yes or no.   ").lower()
    if ii == "yes":
        q3()
    elif ii == "no":
        print("\nIt's probably not loss. Sorry!")
    else:
        print(ii)

def q1():
    i = input("\nIs there one person or thing in the top right? Yes or no.  ").lower()
    if i == "yes":
        q2()
    elif i == "no":
        print("\nIt's probably not loss. Sorry!")
    else:
        print(i)



intro()

