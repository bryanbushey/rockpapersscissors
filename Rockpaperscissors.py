import random
moves = ['rock','paper','scissors']
def main():
    keepGoingMain = 1
    while keepGoingMain == 1:
        computerMove = moves[random.randint(0,2)] #computer makes its own move on rage from 0 to 2
        playerMove = getPlayerMove()
        print('You chose:',playerMove,'\nPC chose:',computerMove)
        if(playerMove == computerMove):
            print('You both chose',playerMove,'play again!\n--------------------------\n')
        elif(playerMove == 'paper') and (computerMove == 'rock'):
            print('You Win!')
            break
        elif(playerMove == 'rock') and (computerMove == 'scissors'):
            print('You Win!')
            break
        elif(playerMove == 'scissors') and (computerMove == 'paper'):
            print('You Win!')
            break
        else:
            print("You lose! You suck.")
            break

def getPlayerMove():
    #creates escape route
    while keepGoing == 1:
        playerMove = input('Enter Rock, Paper, or Scissors: ').lower() #makes all inputs lower case
        for i in range(0,3): #makes a loop with i incrementing every loop
            if playerMove == moves[i]: #checks the address of the moves list with the players input
                keepGoing = 0 #zero escapses the while loop
    return(playerMove)

def startPlaying():
    while True:
        try:
            playTime = int(input("How many games do you want to play?\nEnter Here:"))
            if not (type(playTime) is int):
                raise ValueError()
        except ValueError:
            print("Invalid Option. Numbers only\n-----------------")
        else:
            break

    for i in range(1,playTime+1):
        main()
        print('--------------------------')
    print('Thank you for playing!')

startPlaying()
