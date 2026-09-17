 '''
Random Module --> it helps to generate random values
OTP generation,Story Generation,Games (Rock Paper Scissiors)
'''
import random,time
'''
#random number generation --> OTP
a=random.randint(1000,9999)
#print(a)
for i in range(5):
    time.sleep(2)
    print(random.randint(1000,9999))

#playing a game (Rock peper Scissors)
#Two players-->game-->

player1=input("Enter one of these --> Rock,paper,Scissors").lower().strip()
player2=random.choice(["Rock","paper","Scissors"]).lower()
#print(player1)
#print(player2)
if player1=="rock" and player2=="paper":
    print("player2 won")
elif player1=="paper" and player2=="scissors":
    print("player2 won")    
elif player1=="scissor" and player2=="rock":
    print("player2 won")
elif player1==player2:
    print("tie")
else:
    print("player1 won")

#get the score for each user and declare the winner
#play the game for 10 times

import random

player1_score = 0
player2_score = 0

choices = ["rock", "paper", "scissors"]

for round in range(1, 11):
    print("\nRound", round)

    player1 = input("Player 1, choose rock/paper/scissors: ").lower()
    player2 = random.choice(choices)

    

    print("Player 2 chose:", player2)

    if player1 == player2:
        print("It's a Draw!")

    elif (player1 == "rock" and player2 == "scissors") or \
         (player1 == "paper" and player2 == "rock") or \
         (player1 == "scissors" and player2 == "paper"):

        print("Player 1 Wins!")
        player1_score += 1

    else:
        print("Player 2 Wins!")
        player2_score += 1

print("\n========== FINAL SCORE ==========")
print("Player 1 Score:", player1_score)
print("Player 2 Score:", player2_score)

if player1_score > player2_score:
    print("Player 1 is the Winner!")
elif player2_score > player1_score:
    print("Player 2 is the Winner!")
else:
    print("The Game is a Draw!")



import segno
print(dir(segno))
from segno import helpers
qr=helpers.make_mecard(name="Raavi Rohith",
                       email="raavi.rohit08@gmail.com",
                       phone="+91 6301690685",
                       url=("https://www.linkedin.com/in/raavi-rohith-44464b370/"))
print(qr)
qr.save("mycard.png",scale=10)

#Now its your turn-->explore module
'''
#Build a virtual Assistant using Python -->virtual Environment
#speak,Resond back, Greet you,make a conversation,open Browser,
#locate Google maps,tell a story,play a game
#pop --> 
















                            
