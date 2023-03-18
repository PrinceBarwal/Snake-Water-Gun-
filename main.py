# Snake Water Gun game in python


import random


def gameWin(comp , you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True
        

randNo = random.randint(1,3)

if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
else:
    comp = 'g'

you = input("Your's turn : Snake(s) Water(w) and Gun(g) : ")

print(f"Computer choose {comp}")
print(f"You choose {you}")


win = gameWin(comp , you)

if win == None:
    print("Game is tie")
elif win == True:
    print("You Win!")
else:
    print("You Loose!")