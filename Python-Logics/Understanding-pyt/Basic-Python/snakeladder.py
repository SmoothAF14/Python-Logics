import random
pos = 0
pos2 =0
while pos != 100 and pos2 != 100 : 
    dice = random.randint(1,6)
    dice2 = random.randint(1,6)
    act = random.randint(1,3)
    act2 = random.randint(1,3)
    if act == 1:
        print("No Play for Player 1")
    if act2==1:
        print("No Play for Player 2")
    elif act == 2:
        pos+=dice
        if pos>100:
            pos-=dice
        print("Ladder for Player 1")
        print("Current Position of player 1: ",pos)
    elif act2==2:
        pos2+=dice2
        if pos2>100:
            pos2-=dice2
        print("Ladder for Player 2")
        print("Current Position of player 2: ",pos2)
    else:
        if(pos2-dice2)>=0:
            pos2-=dice2
            print("Snake or Player 2")
            print("Current Position of player 2: ",pos2)
        else:
            pos2 = 0
            print("Snake for Player 2")
            print("Current Position of player 2: ",pos2)
        if(pos-dice)>=0:
            pos-=dice
            print("Snake for Player 1")
            print("Current Position of player 1: ",pos)
        else:
            pos = 0
            print("Snake for Player 1")
            print("Current Position of player 1: ",pos)

if(pos2==100):
    print("Player 2 wins")
else:
    print("Player 1 wins")





