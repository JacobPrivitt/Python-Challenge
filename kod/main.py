# Knights of Dunvale
# By Preston and Jacob
print("Old Woman: Hello there, Welcome to Dunvale!")
print("Old Woman: What is your name traveler?")
name = input("What is your name?")
print("Old Woman: Well hello there, " + name + ".")
print("Old Woman: You will need a sword and shield in this treacherous land")
print("New Items \n Sword +1 \n Shield +1")
player_items = "sword", "shield"
print("Old Woman: To start your quest, go right.")

while True:
    i = input("To turn right type 'right'.").lower()
    if i == "right":
        print("So it begins.")
        break
    else:
        print("Ok the directions weren't that hard, like just type right.")

print("You walk through some hanging ivy, you stand on the edge of a cliff that over looks a "
      "vast mountain range. On the top \n of the tallest and farthest mountain you see a great castle "
      "will a beam of light shooting out of the top. There is no \n way do go right or left only down.")

while True:
    ii = input("Where too?").lower()
    if ii == "down":
        print("You slide down the cliff and land in a pile of leaves.")
        break
    else:
        print("Can't go that way.")

print("The opposite cliff face stands in front of you, your only options are to go right or left. \n left you see"
      "a small river going downstream will green shrubs and grass surrounding the river.\n "
      "to the right you see dry dirt and sand, leading to a dense forest.")

while True:
    iii = input("Which way?").lower()
    if iii == "left":
        print("TBC")
        break
    elif iii == "right":
        print("TBC")
        break
    else:
        print("TBC")