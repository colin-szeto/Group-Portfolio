#this is the file that you will be editing to edit the display on the buttons

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

# this formats the output of sets into an array of arrays for formating to send to the user
sets = [movelist[x:x+2] for x in range(0, len(movelist), 2)]
