import os
import random
from tabulate import tabulate
from IPython.display import clear_output

# ----------------------------------- Initialize -----------------------------------
random.seed(2)

# ................................ Players ...............................
playerNumber = 0
firstPlayerMarker = ""
secondPlayerMarker = ""

# .............................. Game table ..............................
systemPlayerChoices = [0, 1, 2, 3, 4, 5, 6, 7, 8]
gameTable = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# ------------------------------------ Functions -----------------------------------
def PlayerInput():

    global firstPlayerMarker
    global secondPlayerMarker
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    while firstPlayerMarker != "X" and firstPlayerMarker != "O":

        firstPlayerMarker = str(input("Player 1 , choose X or O: ")).upper()

        if firstPlayerMarker == "X":

            secondPlayerMarker = "O"

        elif firstPlayerMarker == "O":

            secondPlayerMarker = "X"
    
    print("Gamer 1 is: " + firstPlayerMarker + ", Gamer 2 is: " + secondPlayerMarker)

def PlayerChoise():

    text = "Player 1, Choose a position (1 ~ 9): "

    if playerNumber == 1:

        text = "Player 2, Choose a position (1 ~ 9): "

    pos = int(input(text))

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    while pos < 1 or pos > 9:
        pos = int(input(text))
        
    return (pos - 1) 

def PlaceMarker(board, marker, position):
    
    board[position] = marker

def PrintGameTable():
    """
    Function to print game table
    """
    clear_output(wait=True)
    
    # ~~~~~~~~~~ Clear command for vscode ~~~~~~~~~~
    os.system('cls')
    
    print(tabulate([
                   gameTable[6:9],
                   gameTable[3:6],
                   gameTable[0:3]
                   ], tablefmt="grid"))

def WinCheck(board, marker):
    
    # ~~~~~~~~~~ Check gamer status ~~~~~~~~~~
    if( board[0] == marker and board[1] == marker and board[2] == marker or
        board[3] == marker and board[4] == marker and board[5] == marker or
        board[6] == marker and board[7] == marker and board[8] == marker or
           
        board[0] == marker and board[3] == marker and board[6] == marker or
        board[1] == marker and board[4] == marker and board[7] == marker or
        board[2] == marker and board[5] == marker and board[8] == marker or
           
        board[0] == marker and board[4] == marker and board[8] == marker or
        board[2] == marker and board[4] == marker and board[6] == marker):

        # `````````` Return gamer status ``````````
        return True

    else:
        return False

def ChooseFirst():

    return random.randint(0, 1)

def SpaceCheck(board, position):

    if board[position] != " ":
        return False
    else:
        return True

def FullBoardCheck(board):

    if (board[0] != " " and board[1] != " " and board[2] != " " and
        board[3] != " " and board[4] != " " and board[5] != " " and
        board[6] != " " and board[7] != " " and board[8] != " "):

        return True
    
    else:
        return False

def Replay():

    global firstPlayerMarker
    global secondPlayerMarker

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    response = str(input("Play again? Enter yes or no? ")).lower()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    if response == "yes":

        return True

    elif response == "no":
        return False

# -------------------------------------- Main --------------------------------------
startGame = True

# ...............................................................
while True:

    if startGame == True:

        startGame = False
        gameTable[0:9] = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        systemPlayerChoices[0:9] = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        # ````````````````` Show start message ````````````````
        PrintGameTable()
        print('Welcome to tic tac toe')

        # ````````````````````` Reset data ````````````````````
        firstPlayerMarker = secondPlayerMarker = ""
        gameTable[0:9] = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

        # ````````````````````` Get param `````````````````````
        PlayerInput()
        playerNumber = ChooseFirst()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~ Play ~~~~~~~~~~~~~~~~~~~~~~~~~
    if playerNumber == 0:

        playerMarker = firstPlayerMarker
        playerWonMessage = "Player 1 has won!"

        # ```````````````````` Check marker ```````````````````
        choisedPosition = PlayerChoise()

        while SpaceCheck(gameTable, choisedPosition) == False:

            print("Select other cells!")
            choisedPosition = PlayerChoise()

    else:

        playerMarker = secondPlayerMarker
        playerWonMessage = "Player 2 has won!"

        # ```````````````````` Check marker ```````````````````
        choisedPosition = random.choice(systemPlayerChoices)

        while SpaceCheck(gameTable, choisedPosition) == False:

            choisedPosition = random.choice(systemPlayerChoices)

    # ~~~~~~~~~~~~~~~~~~~~ Remove choices ~~~~~~~~~~~~~~~~~~~~  
    systemPlayerChoices.remove(choisedPosition)

    # ~~~~~~~~~~~~~~~~~~~~~~ Add merker ~~~~~~~~~~~~~~~~~~~~~~
    PlaceMarker(gameTable, playerMarker, choisedPosition)
    PrintGameTable()

    # ~~~~~~~~~~~~~~~~~~~~ Check for win ~~~~~~~~~~~~~~~~~~~~~
    if WinCheck(gameTable, playerMarker) == True:

        print(playerWonMessage)
        print("End game.")

        startGame = Replay()

        if startGame == False:
            break

    # ~~~~~~~~~~~~~~~~~~~~~ Check table ~~~~~~~~~~~~~~~~~~~~~~
    elif FullBoardCheck(gameTable) == True:

        print("End game.")

        startGame = Replay()
            
        if startGame == False:
            break

    # ~~~~~~~~~~~~~~~~~~~~ Change player ~~~~~~~~~~~~~~~~~~~~~
    playerNumber = not playerNumber

# ---------------------------------- End of codes ----------------------------------