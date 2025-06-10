import random
import time
turn = 0

class Player:
    # initialise player
    def __init__(self,num):
        self.num = num
        self.pos = 0
        self.coin = random.randint(0,1)
        self.dice = random.randint(1,6)
        print("Player", num, "'s go")

    # move player
    def move(self,direction,squares):
        if direction == 0: # moves forwards if 0, back if 1
            self.pos += squares
        else:
            self.pos -= squares
        return self.pos

    # tosses coin
    def tossCoin(self):
        if self.coin == 0:
            print("You have landed heads")
        else:
            print("You have landed tails")
        return self.coin

    # rolls die
    def rollDice(self):
        print("You have rolled", self.dice)
        return self.dice

print("Welcome to my Snake n Ladder's game")
time.sleep(1)
print("-----------------------------------")
print("You and your player will take turns tossing a coin and rolling a die")
time.sleep(2)
print("If the player tosses heads they will move forward, tails backwards")
time.sleep(2)
print("The number you roll is the number of squares you will move")
time.sleep(2)
print("The winner is the first to make it to the final square")
time.sleep(1)
print("-----------------------------------")

while turn<10:
    turn += 1
    if turn%2 == 1:
    # player  1 turn
        player = Player(1)
        coinToss = player.tossCoin()
        diceRoll = player.rollDice()
        print(player.move(coinToss,diceRoll))
        print(player.tossCoin())
        print(player.rollDice())
        print(self.pos)
        
    else:
    # player 2 turn
        player = Player(2)
        print(player.tossCoin())
        print(player.rollDice())
        print(self.pos)
   

#player1 = Player(1)
#print(player1.move('f',10))
#player2 = Player(2)
