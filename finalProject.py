# PathfinderHelper

# The intention of this program is to assist dungeon masters in creating
# an new file for homebrewed magical items

magicMenu = {
    1: "Weapons",
    2: "Items",
    3: "Armour",
    4: "Quit"
}

def finalizedItem(choice, name, range, damage, specialEffect):
    if choice == 1:
        return print("Weapon: ", name,".", " Range: ", range, ".", " Damage: ", damage, ".", " Special Effects: ", specialEffect)
    elif choice == 2:
        return print("Item: ", name,".", " Special Effects: ", specialEffect)
    elif choice == 3:
        return print("Weapon: ", name,".", " Range: ", range, ".", " Damage: ", damage, ".", " Special Effects: ", specialEffect)

def printDictionary(dict):                                               # Print Function
    for option in dict:
        print(option, dict[option])

printDictionary(magicMenu)
choice = input("[1-4]What kind of magic items are you creating?: ")

while choice < 4 or choice > 0:
    input('ERROR: only accepts 1-4. Try again: ')

if choice == 1:
    name = input("What is the name of your Weapon?: ")
    range = input("What is the range of your weapon?: ")
    damage = input("What is the damage for this weapon?: ")
    specialEffect = input("What are your weapons special effects?: ")

elif choice == 2:
    name = input("What is the name of the item?: "),
    specialEffect = input("What are your items special effects?: ")

elif choice == 3:
    name = input("What is the name of your armour?: ")
    range = input("What is the type of your armour?: ")
    damage = input("What is the armour class for this armour?: ")
    specialEffect = input("What is your armours special effects?: ")

elif choice == 4:
    exit()

aFile = open(r"C:\magicItems.txt", "x")
aFile.write(finalizedItem(choice))
