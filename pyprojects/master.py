import turtle
t = turtle.Pen()

t.color('blue','green')
t.begin_fill()

count = 0

for x in range(1,9):
    t.forward(300)
    t.left(225)
    count = count+1
    print("COunt is: " + str(count))

    if count > 7:
        print("The star pattern is complete!")
        break

t.end_fill()
print("A star is born")


name = "Jacob"
age = 18

print(name + str(age))


t = turtle.Pen()
for x in range(1,9):
    t.forward(50)
    t.left(90)
    t.forward(100)


for x in range(1,9):
    t.forward(100)
    t.left(225)


for i in range(5):
    print(i)
print("End of the first loop")
    

name = "Jacob"
for x in name:
    print(x)
print("\nEnd of the loop")

for i in range(1,5):
    print(i)


#create password
while True:
    i = input("click 1 to sign up, click 2 to sign in.")
    if i == 1:
        ii = input("Create password")
        break
    elif i == 2:
        iii = input("Input Password")
        break
    else:
        print("That's not an option")




nameFirst = "Jacob"
nameLast = "Privitt"
age = "18"

print(nameFirst, nameLast, age)

