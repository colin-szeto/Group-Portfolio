#this is the file that you will be editing to edit the display on the buttons
from movepiece import len2, len3, len4, len5, len6, len7
"""from piecedefinitions import *
from zwhitepersp import *
from zblackpersp import *
from checkfunctions import *
from protectionfunctions import *"""

board = {
    "a8": "BR1n", "b8": "BN1", "c8": "BB1", "d8": "BQ1", "e8": "BK1n", "f8": "BB2", "g8": "BN2", "h8": "BR2n",
    "a7": "bp1", "b7": "bp2", "c7": "bp3", "d7": "bp4", "e7": "bp5", "f7": "bp6", "g7": "bp7", "h7": "bp8",
    "a6": "  ", "b6": "  ", "c6": "  ", "d6": "  ", "e6": "  ", "f6": "  ", "g6": "  ", "h6": "  ",
    "a5": "  ", "b5": "  ", "c5": "  ", "d5": "  ", "e5": "  ", "f5": "  ", "g5": "  ", "h5": "  ",
    "a4": "  ", "b4": "  ", "c4": "  ", "d4": "  ", "e4": "  ", "f4": "  ", "g4": "  ", "h4": "  ",
    "a3": "  ", "b3": "  ", "c3": "  ", "d3": "  ", "e3": "  ", "f3": "  ", "g3": "  ", "h3": "  ",
    "a2": "wp1", "b2": "wp2", "c2": "wp3", "d2": "wp4", "e2": "wp5", "f2": "wp6", "g2": "wp7", "h2": "wp8",
    "a1": "WR1n", "b1": "WN1", "c1": "WB1", "d1": "WQ1", "e1": "WK1n", "f1": "WB2", "g1": "WN2", "h1": "WR2n"}

keysBoard, valuesBoard = zip(*board.items()) # isolates the board keys and board values

"""imagesList = []
def sliceColors(values):#creates the list to translate into pieces
    a = 0
    for x in values:
        input = str(values[a])
        final = input[0]
        imagesList.append(final.upper())
        a = a + 1
    return imagesList

color = sliceColors(valuesBoard)"""

# the row dictonaries that the board is split out too
board1 = {} #rank 1 (row 1) (closest to white)
board2 = {}
board3 = {}
board4 = {}
board5 = {}
board6 = {}
board7 = {}
board8 = {} #rank 8 (row 8) (farthest from white)

listBoard = ["", board1, board2, board3, board4, board5, board6, board7, board8] # inluded "" to artificialy overcome the 0 index
dictionarything = {"BR": "♜", "BN": "♞", "BB": "♝", "BQ": "♛", "BK": "♚", "bp": "♟︎️︎", "WR": "♖", "WN": "♘", "WB": "♗", "WQ": "♕", "WK": "♔", "wp": "♙"}

# spliting the dictonary into 8 dictonaries, if the second value within the cell "a8" is 8 then update the row of the board with that value
for square,piece in board.items():
    if piece != "  ":
        # if the values is not empty then replace the cell value with the unicode of the value
        listBoard[int(square[1])].update({square:dictionarything[piece[0:2]]})
    else:
        """if the values of the dictonary are empty, we replace it with a string emptySpace, 
        this allows for us in the jinja template replace the value emptySpace with &nbsp;&nbsp;&nbsp;&nbsp; 
        or whitespace only interpreted by html"""
        listBoard[int(square[1])].update({square:"emptySpace"})

# placing all of the ranks (rows) allows the jinja template to show each dictonary as the row of the tbale
allBoard = [board8, board7, board6, board5, board4, board3, board2, board1]

#keeping track of the moves
movelist = []

# this takes the routes that are selected by the buttons an appends them to moveList
def movesdata(toAppend):
    movelist.append(toAppend)
    sets = [movelist[x:x+2] for x in range(0, len(movelist), 2)]
    return sets
"""=================below has been added 11/17/20"""

def actualMove(currentMove):
    actMove = round(currentMove/2)
    return actMove

def previousMove(acutalMove):
    if acutalMove%2 != 0:
        print("previously: white's move")
    else:
        print("previously: black's move") #this is the player that is wi
# initializing N
N = 2
res = movelist[-N:]

#print("move number: "+ str(acutalMove(currentMove)))

def sample(currentMove,res):
    b = currentMove%2
    if b != 0:
        #this means the only the first value of the move has been selected
        message = "cannot sample the values yet"
    else:
        #this means that the move piece code will run
        usermove = ' '.join(res)#this is the string that is passed into movePiece
        message = "last two moves were"+ " " + usermove
        """try:
            move1 = {2: len2, 3: len3, 4: len4, 5: len5, 6: len6, 7: len7}
            move1[len(usermove)](usermove, board)#, storeboard, whitemove, whitecolor, blackcolor
        except Exception as e:
            message = "Please enter valid move." + e
            #movepiece(board, storeboard, whitemove, whitecolor, blackcolor)"""
    return message

""""
finalString = ' '.join(res)
"""

"""
inital goals:
    1.logic for communicating to movepiece
        when a new list of two values are created then pass onto move pieve
        when the values are invalid (can't move there), delete last list (representhing the last beginning and end square) 
            also communicate with the user through template that move was invalid
        when the values are correct 
            update the dictonary
    
    2.resign button 
    
    3.winscreens to rediect user to the key of replay function
    menu with html, flesh out the chessDict before creating the board
"""
