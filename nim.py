'''
Game: NIM
Author: Zakariah Siyaji
Date: 09/10/2018
IDE: Visual Studios

Create the following game: https://plus.maths.org/content/play-win-nim

1) The game should display the current player (i.e. Player 1 or Player 2)
2) The game is only won after all of the match sticks are destroyed
3) Match sticks are indicated by pipes: | 
4) Removed match sticks are indicated by astericks: *
5) Must take user input on size of heaps

Sample output:
-------------------------------------------------------
Welcome to the NIM Game!
how many rows do you want: 6
|
| |
| | |
| | | |
| | | | |
| | | | | |
Enter the number of positions you would like to remove: 
-------------------------------------------------------
'''

gameArray = []
print(" Welcome to the NIM Game!")
row = int(input("how many rows do you want: "))
sticks = "| "


def createGame(array):
    for i in range(0, row):
        for j in range(0, i+1):
            array.append(sticks)

def readGame(array):
    for i in range(0, row):
        for j in range(0, i+1):
            print(array[i], end="")
        print('\r') 

def updateGame(array, amountOfPositions):
    positionsArray = []
    for i in range(0,amountOfPositions):
        if i == 0:
            val = int(input("Input the positions you would like to remove: "))
        elif i < amountOfPositions-1:
            val = int(input("Input the next position: "))
        else:
            val = int(input("Input the final position: "))
        positionsArray.append(val)
  
    for j in range(0,len(positionsArray)):
        array.insert(positionsArray[j], "* ")
        array.pop(positionsArray[j]+1)

def gameComplete(array):
    gameComplete = True
    count = 0
    for i in range(0,len(array)):
        if (array[i] == sticks):
            count += 1
    if(count > 0 ):
        gameComplete = False 
    return gameComplete

createGame(gameArray)
while(gameComplete(gameArray) == False):
    count = 1
    readGame(gameArray)
    amountOfPositions = int(input("Enter the number of positions you would like to remove: "))
    updateGame(gameArray, amountOfPositions)
    count += 1
    if (count % 2 == 0):
        print("Player two's turn")
    else:
        print("Player one's turn")





























