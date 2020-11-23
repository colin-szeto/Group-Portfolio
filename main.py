# https://flask.palletsprojects.com/en/1.1.x/api/
import data
from flask import Flask, render_template, request, redirect
import chessData
from chessData import board, movelist, allBoard

#create a Flask instance
app = Flask(__name__)

#InfoDb = []

#connects default URL of server to a python function
@app.route('/')
def home():
    return render_template("home.html",github="github", website ="link website")#home has to be under templates

@app.route("/project/chessJs")#for the dragable chess file
def chessJS():
  return render_template("chessJs.html")

@app.route("/project/chessPush")#for the print chess board from dictonaries
def chessPush():
    return render_template("chessPush.html", displayBoard=board)

@app.route("/project/calc")#for the dragable chess file
def calc():
    return render_template("calc.html", display="")

@app.route("/add", methods=['GET','POST'],)
def addition():
    if request.method == 'POST':
        form = request.form
        numberOne = int(form['numOne'])
        numberTwo = int(form['numTwo'])
        return render_template("calc.html", your_list=data.answersdata(numberOne,numberTwo))#data.playlist()

    return redirect("/calc")

""""@app.route("/add", methods=['GET','POST'],) #this is the correct way to do it
def addition():
    if request.method == 'POST':
        form = request.form
        numberOne = int(form['numOne'])
        numberTwo = int(form['numTwo'])
        calc = numberOne + numberTwo #takes the user input and contatinates it together
        return render_template("calc.html", your_list=data.answersdata(calc))#data.playlist()

    return redirect("/calc")"""

@app.route("/project/yourName", methods=['GET','POST'],)#for the dragable chess file
def yourName():
    if request.method == 'POST':
        form = request.form
        name = int(form['name'])
        return render_template("calc.html", name = name)
    return redirect("/nameBack")


@app.route("/project/journals")#for storing all the links to the webpage
def journals():
  return render_template("journals2.html",repl="personal repl", website ="link website")#allows to define the text that is hyperlinked on the the personal journals

#--------------------------------------------------- here is where the chess with POST starts
@app.route("/project/chessMenu/") # this gets the user to the chess board
def chessMenu():
    return render_template("chessMenu.html")

@app.route("/project/chessDictTable/") # this gets the user to the chess board
def chessDictTable_route():
    return render_template("chessDictTable.html", allBoard=chessData.split_board(board))

@app.route("/createBoardTable", methods=['GET','POST']) #this is is where the website directs to when clicking the submit button
def createBoardTable():
    if request.method == 'POST': #if the meathod is post
        form = request.form
        movelist.clear()#resets the stored moves when create board is selected
        return render_template("chessDictTable.html", displayClicked="  ", allBoard=chessData.split_board(board))
        #board1=board1, board2=board2, board3=board3, board4=board4, board5=board5, board6=board6, board7=board7, board8=board8
    return redirect("/project/chessDictTable/") #redirects to format into the chess board

"""@app.route("/firstValue", methods=['GET','POST'])
def returnClicked():
    if request.method == 'POST':
        form = request.form
        #input = str(form['value'])
        return render_template("chessDictTable.html", displayClicked="you clicked something", allBoard=allBoard)
    return redirect("/project/chessDictTable/")"""

@app.route("/a8", methods=['GET','POST'])#--------------------------------------------------------------------------------------------------------------------------------------------------------------this is where it starts
def a8():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="a8", allBoard=chessData.split_board(board), movelist=chessData.movesdata("a8"), message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/a7", methods=['GET','POST'])
def a7():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="a7", allBoard=chessData.split_board(board), movelist=chessData.movesdata("a7"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))

@app.route("/a6", methods=['GET','POST'])
def a6():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="a6", allBoard=chessData.split_board(board), movelist=chessData.movesdata("a6"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/a5", methods=['GET','POST'])
def a5():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="a5", allBoard=chessData.split_board(board), movelist=chessData.movesdata("a5"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/a4", methods=['GET','POST'])
def a4():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="a4", allBoard=chessData.split_board(board), movelist=chessData.movesdata("a4"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/a3", methods=['GET','POST'])
def a3():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="a3", allBoard=chessData.split_board(board), movelist=chessData.movesdata("a3"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/a2", methods=['GET','POST'])
def a2():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="a2", allBoard=chessData.split_board(board), movelist=chessData.movesdata("a2"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/a1", methods=['GET','POST'])
def a1():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="a1", allBoard=chessData.split_board(board), movelist=chessData.movesdata("a1"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/b8", methods=['GET','POST'])
def b8():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="b8", allBoard=chessData.split_board(board), movelist=chessData.movesdata("b8"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/b7", methods=['GET','POST'])
def b7():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="b7", allBoard=chessData.split_board(board), movelist=chessData.movesdata("b7"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/b6", methods=['GET','POST'])
def b6():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="b6", allBoard=chessData.split_board(board), movelist=chessData.movesdata("b6"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/b5", methods=['GET','POST'])
def b5():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="b5", allBoard=chessData.split_board(board), movelist=chessData.movesdata("b5"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/b4", methods=['GET','POST'])
def b4():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="b4", allBoard=chessData.split_board(board), movelist=chessData.movesdata("b4"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/b3", methods=['GET','POST'])
def b3():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="b3", allBoard=chessData.split_board(board), movelist=chessData.movesdata("b3"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/b2", methods=['GET','POST'])
def b2():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="b2", allBoard=chessData.split_board(board), movelist=chessData.movesdata("b2"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/b1", methods=['GET','POST'])
def b1():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="b1", allBoard=chessData.split_board(board), movelist=chessData.movesdata("b1"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))

@app.route("/c8", methods=['GET','POST'])
def c8():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="c8", allBoard=chessData.split_board(board), movelist=chessData.movesdata("c8"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/c7", methods=['GET','POST'])
def c7():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="c7", allBoard=chessData.split_board(board), movelist=chessData.movesdata("c7"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/c6", methods=['GET','POST'])
def c6():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="c6", allBoard=chessData.split_board(board), movelist=chessData.movesdata("c6"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/c5", methods=['GET','POST'])
def c5():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="c5", allBoard=chessData.split_board(board), movelist=chessData.movesdata("c5"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/c4", methods=['GET','POST'])
def c4():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="c4", allBoard=chessData.split_board(board), movelist=chessData.movesdata("c4"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/c3", methods=['GET','POST'])
def c3():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="c3", allBoard=chessData.split_board(board), movelist=chessData.movesdata("c3"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/c2", methods=['GET','POST'])
def c2():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="c2", allBoard=chessData.split_board(board), movelist=chessData.movesdata("c2"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/c1", methods=['GET','POST'])
def c1():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="c1", allBoard=chessData.split_board(board), movelist=chessData.movesdata("c1"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))

@app.route("/d8", methods=['GET','POST'])
def d8():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="d8", allBoard=chessData.split_board(board), movelist=chessData.movesdata("d8"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/d7", methods=['GET','POST'])
def d7():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="d7", allBoard=chessData.split_board(board), movelist=chessData.movesdata("d7"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/d6", methods=['GET','POST'])
def d6():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="d6", allBoard=chessData.split_board(board), movelist=chessData.movesdata("d6"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/d5", methods=['GET','POST'])
def d5():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="d5", allBoard=chessData.split_board(board), movelist=chessData.movesdata("d5"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/d4", methods=['GET','POST'])
def d4():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="d4", allBoard=chessData.split_board(board), movelist=chessData.movesdata("d4"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/d3", methods=['GET','POST'])
def d3():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="d3", allBoard=chessData.split_board(board), movelist=chessData.movesdata("d3"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/d2", methods=['GET','POST'])
def d2():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="d2", allBoard=chessData.split_board(board), movelist=chessData.movesdata("d2"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/d1", methods=['GET','POST'])
def d1():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="d1", allBoard=chessData.split_board(board), movelist=chessData.movesdata("d1"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))

@app.route("/e8", methods=['GET','POST'])
def e8():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="e8", allBoard=chessData.split_board(board), movelist=chessData.movesdata("e8"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/e7", methods=['GET','POST'])
def e7():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="e7", allBoard=chessData.split_board(board), movelist=chessData.movesdata("e7"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/e6", methods=['GET','POST'])
def e6():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="e6", allBoard=chessData.split_board(board), movelist=chessData.movesdata("e6"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/e5", methods=['GET','POST'])
def e5():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="e5", allBoard=chessData.split_board(board), movelist=chessData.movesdata("e5"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/e4", methods=['GET','POST'])
def e4():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="e4", allBoard=chessData.split_board(board), movelist=chessData.movesdata("e4"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/e3", methods=['GET','POST'])
def e3():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="e3", allBoard=chessData.split_board(board), movelist=chessData.movesdata("e3"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/e2", methods=['GET','POST'])
def e2():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="e2", allBoard=chessData.split_board(board), movelist=chessData.movesdata("e2"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/e1", methods=['GET','POST'])
def e1():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="e1", allBoard=chessData.split_board(board), movelist=chessData.movesdata("e1"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))

@app.route("/f8", methods=['GET','POST'])
def f8():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="f8", allBoard=chessData.split_board(board), movelist=chessData.movesdata("f8"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/f7", methods=['GET','POST'])
def f7():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="f7", allBoard=chessData.split_board(board), movelist=chessData.movesdata("f7"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/f6", methods=['GET','POST'])
def f6():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="f6", allBoard=chessData.split_board(board), movelist=chessData.movesdata("f6"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/f5", methods=['GET','POST'])
def f5():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="f5", allBoard=chessData.split_board(board), movelist=chessData.movesdata("f5"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/f4", methods=['GET','POST'])
def f4():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="f4", allBoard=chessData.split_board(board), movelist=chessData.movesdata("f4"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/f3", methods=['GET','POST'])
def f3():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="f3", allBoard=chessData.split_board(board), movelist=chessData.movesdata("f3"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/f2", methods=['GET','POST'])
def f2():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="f2", allBoard=chessData.split_board(board), movelist=chessData.movesdata("f2"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/f1", methods=['GET','POST'])
def f1():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="f1", allBoard=chessData.split_board(board), movelist=chessData.movesdata("f1"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))

@app.route("/g8", methods=['GET','POST'])
def g8():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="g8", allBoard=chessData.split_board(board), movelist=chessData.movesdata("g8"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/g7", methods=['GET','POST'])
def g7():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="g7", allBoard=chessData.split_board(board), movelist=chessData.movesdata("g7"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/g6", methods=['GET','POST'])
def g6():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="g6", allBoard=chessData.split_board(board), movelist=chessData.movesdata("g6"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/g5", methods=['GET','POST'])
def g5():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="g5", allBoard=chessData.split_board(board), movelist=chessData.movesdata("g5"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/g4", methods=['GET','POST'])
def g4():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="g4", allBoard=chessData.split_board(board), movelist=chessData.movesdata("g4"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/g3", methods=['GET','POST'])
def g3():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="g3", allBoard=chessData.split_board(board), movelist=chessData.movesdata("g3"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/g2", methods=['GET','POST'])
def g2():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="g2", allBoard=chessData.split_board(board), movelist=chessData.movesdata("g2"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/g1", methods=['GET','POST'])
def g1():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="g1", allBoard=chessData.split_board(board), movelist=chessData.movesdata("g1"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))

@app.route("/h8", methods=['GET','POST'])
def h8():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="h8", allBoard=chessData.split_board(board), movelist=chessData.movesdata("h8"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/h7", methods=['GET','POST'])
def h7():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="h7", allBoard=chessData.split_board(board), movelist=chessData.movesdata("h7"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/h6", methods=['GET','POST'])
def h6():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="h6", allBoard=chessData.split_board(board), movelist=chessData.movesdata("h6"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/h5", methods=['GET','POST'])
def h5():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="h5", allBoard=chessData.split_board(board), movelist=chessData.movesdata("h5"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/h4", methods=['GET','POST'])
def h4():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="h4", allBoard=chessData.split_board(board), movelist=chessData.movesdata("h4"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/h3", methods=['GET','POST'])
def h3():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="h3", allBoard=chessData.split_board(board), movelist=chessData.movesdata("h3"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/h2", methods=['GET','POST'])
def h2():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="h2", allBoard=chessData.split_board(board), movelist=chessData.movesdata("h2"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
@app.route("/h1", methods=['GET','POST'])
def h1():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="h1", allBoard=chessData.split_board(board), movelist=chessData.movesdata("h1"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True)