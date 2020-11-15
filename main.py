# https://flask.palletsprojects.com/en/1.1.x/api/
import data
from flask import Flask, render_template, request, redirect
from data import board

import chessData
from chessData import board, movelist, sets, allBoard

#create a Flask instance
app = Flask(__name__)

#InfoDb = []

#connects default URL of server to a python function
@app.route('/')
def home():
    #function uses Flask import (Jinga) to render HTML
    #data is passed as a parameter
    return render_template("home.html")#home has to be under templates

@app.route("/project/chessJs")#for the dragable chess file
def chessJS():
  return render_template("chessJs.html")

@app.route("/project/chessPush")#for the print chess board from dictonaries
def chessPush():
    return render_template("chessPush.html", displayBoard=board)

@app.route("/project/index")#for the dragable chess file
def index():
    return render_template("index.html", display="")

@app.route("/project/add", methods=['GET','POST'],)#for the dragable chess file
def addition():
    if request.method == 'POST':
        form = request.form
        numberOne = int(form['numOne'])
        numberTwo = int(form['numTwo'])
        calc = numberOne + numberTwo
        return render_template("index.html", your_list = data.answersdata(calc))#data.playlist()

    return redirect("/index")


@app.route("/project/yourName", methods=['GET','POST'],)#for the dragable chess file
def yourName():
    if request.method == 'POST':
        form = request.form
        name = int(form['name'])
        return render_template("index.html", name = name)
    return redirect("/nameBack")


@app.route("/project/journals")#for storing all the links to the webpage
def journals():
  return render_template("journals.html")#,repl="repl of website", website ="link to personal website")#allows to define the text that is hyperlinked on the the personal journals

#--------------------------------------------------- here is where the chess with POST starts
@app.route("/project/chessMenu/") # this gets the user to the chess board
def chessMenu():
    return render_template("chessMenu.html")

@app.route("/project/chessDictTable/") # this gets the user to the chess board
def chessDictTable_route():
    return render_template("chessDictTable.html")

@app.route("/createBoardTable", methods=['GET','POST']) #this is is where the website directs to when clicking the submit button
def createBoardTable():
    if request.method == 'POST': #if the meathod is post
        form = request.form
        movelist.clear()#resets the stored moves when create board is selected
        return render_template("chessDictTable.html", rowList=board,  displayClicked="  ", allBoard=allBoard)
        #board1=board1, board2=board2, board3=board3, board4=board4, board5=board5, board6=board6, board7=board7, board8=board8
    return redirect("/project/chessDictTable/") #redirects to format into the chess board

"""@app.route("/firstValue", methods=['GET','POST'])
def returnClicked():
    if request.method == 'POST':
        form = request.form
        #input = str(form['value'])
        return render_template("chessDictTable.html", rowList=board,  displayClicked="you clicked something", allBoard=allBoard)
    return redirect("/project/chessDictTable/")"""

@app.route("/a8", methods=['GET','POST'])#--------------------------------------------------------------------------------------------------------------------------------------------------------------this is where it starts
def a8():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="a8", allBoard=allBoard, movelist=chessData.movesdata("a8"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/a7", methods=['GET','POST'])
def a7():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="a7", allBoard=allBoard, movelist=chessData.movesdata("a7"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/a6", methods=['GET','POST'])
def a6():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="a6", allBoard=allBoard, movelist=chessData.movesdata("a6"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/a5", methods=['GET','POST'])
def a5():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="a5", allBoard=allBoard, movelist=chessData.movesdata("a5"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/a4", methods=['GET','POST'])
def a4():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="a4", allBoard=allBoard, movelist=chessData.movesdata("a4"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/a3", methods=['GET','POST'])
def a3():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="a3", allBoard=allBoard, movelist=chessData.movesdata("a3"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/a2", methods=['GET','POST'])
def a2():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="a2", allBoard=allBoard, movelist=chessData.movesdata("a2"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/a1", methods=['GET','POST'])
def a1():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="a1", allBoard=allBoard, movelist=chessData.movesdata("a1"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/b8", methods=['GET','POST'])
def b8():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="b8", allBoard=allBoard, movelist=chessData.movesdata("b8"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/b7", methods=['GET','POST'])
def b7():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="b7", allBoard=allBoard, movelist=chessData.movesdata("b7"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/b6", methods=['GET','POST'])
def b6():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="b6", allBoard=allBoard, movelist=chessData.movesdata("b6"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/b5", methods=['GET','POST'])
def b5():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="b5", allBoard=allBoard, movelist=chessData.movesdata("b5"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/b4", methods=['GET','POST'])
def b4():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="b4", allBoard=allBoard, movelist=chessData.movesdata("b4"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/b3", methods=['GET','POST'])
def b3():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="b3", allBoard=allBoard, movelist=chessData.movesdata("b3"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/b2", methods=['GET','POST'])
def b2():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="b2", allBoard=allBoard, movelist=chessData.movesdata("b2"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/b1", methods=['GET','POST'])
def b1():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="b1", allBoard=allBoard, movelist=chessData.movesdata("b1"), movesets=sets)
    return redirect("/project/chessDictTable/")

@app.route("/c8", methods=['GET','POST'])
def c8():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="c8", allBoard=allBoard, movelist=chessData.movesdata("c8"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/c7", methods=['GET','POST'])
def c7():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="c7", allBoard=allBoard, movelist=chessData.movesdata("c7"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/c6", methods=['GET','POST'])
def c6():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="c6", allBoard=allBoard, movelist=chessData.movesdata("c6"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/c5", methods=['GET','POST'])
def c5():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="c5", allBoard=allBoard, movelist=chessData.movesdata("c5"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/c4", methods=['GET','POST'])
def c4():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="c4", allBoard=allBoard, movelist=chessData.movesdata("c4"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/c3", methods=['GET','POST'])
def c3():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="c3", allBoard=allBoard, movelist=chessData.movesdata("c3"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/c2", methods=['GET','POST'])
def c2():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="c2", allBoard=allBoard, movelist=chessData.movesdata("c2"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/c1", methods=['GET','POST'])
def c1():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="c1", allBoard=allBoard, movelist=chessData.movesdata("c1"), movesets=sets)
    return redirect("/project/chessDictTable/")

@app.route("/d8", methods=['GET','POST'])
def d8():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="d8", allBoard=allBoard, movelist=chessData.movesdata("d8"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/d7", methods=['GET','POST'])
def d7():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="d7", allBoard=allBoard, movelist=chessData.movesdata("d7"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/d6", methods=['GET','POST'])
def d6():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="d6", allBoard=allBoard, movelist=chessData.movesdata("d6"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/d5", methods=['GET','POST'])
def d5():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="d5", allBoard=allBoard, movelist=chessData.movesdata("d5"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/d4", methods=['GET','POST'])
def d4():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="d4", allBoard=allBoard, movelist=chessData.movesdata("d4"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/d3", methods=['GET','POST'])
def d3():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="d3", allBoard=allBoard, movelist=chessData.movesdata("d3"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/d2", methods=['GET','POST'])
def d2():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="d2", allBoard=allBoard, movelist=chessData.movesdata("d2"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/d1", methods=['GET','POST'])
def d1():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="d1", allBoard=allBoard, movelist=chessData.movesdata("d1"), movesets=sets)
    return redirect("/project/chessDictTable/")

@app.route("/e8", methods=['GET','POST'])
def e8():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="e8", allBoard=allBoard, movelist=chessData.movesdata("e8"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/e7", methods=['GET','POST'])
def e7():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="e7", allBoard=allBoard, movelist=chessData.movesdata("e7"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/e6", methods=['GET','POST'])
def e6():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="e6", allBoard=allBoard, movelist=chessData.movesdata("e6"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/e5", methods=['GET','POST'])
def e5():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="e5", allBoard=allBoard, movelist=chessData.movesdata("e5"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/e4", methods=['GET','POST'])
def e4():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="e4", allBoard=allBoard, movelist=chessData.movesdata("e4"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/e3", methods=['GET','POST'])
def e3():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="e3", allBoard=allBoard, movelist=chessData.movesdata("e3"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/e2", methods=['GET','POST'])
def e2():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="e2", allBoard=allBoard, movelist=chessData.movesdata("e2"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/e1", methods=['GET','POST'])
def e1():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="e1", allBoard=allBoard, movelist=chessData.movesdata("e1"), movesets=sets)
    return redirect("/project/chessDictTable/")

@app.route("/f8", methods=['GET','POST'])
def f8():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="f8", allBoard=allBoard, movelist=chessData.movesdata("f8"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/f7", methods=['GET','POST'])
def f7():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="f7", allBoard=allBoard, movelist=chessData.movesdata("f7"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/f6", methods=['GET','POST'])
def f6():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="f6", allBoard=allBoard, movelist=chessData.movesdata("f6"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/f5", methods=['GET','POST'])
def f5():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="f5", allBoard=allBoard, movelist=chessData.movesdata("f5"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/f4", methods=['GET','POST'])
def f4():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="f4", allBoard=allBoard, movelist=chessData.movesdata("f4"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/f3", methods=['GET','POST'])
def f3():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="f3", allBoard=allBoard, movelist=chessData.movesdata("f3"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/f2", methods=['GET','POST'])
def f2():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="f2", allBoard=allBoard, movelist=chessData.movesdata("f2"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/f1", methods=['GET','POST'])
def f1():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="f1", allBoard=allBoard, movelist=chessData.movesdata("f1"), movesets=sets)
    return redirect("/project/chessDictTable/")

@app.route("/g8", methods=['GET','POST'])
def g8():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="g8", allBoard=allBoard, movelist=chessData.movesdata("g8"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/g7", methods=['GET','POST'])
def g7():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="g7", allBoard=allBoard, movelist=chessData.movesdata("g7"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/g6", methods=['GET','POST'])
def g6():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="g6", allBoard=allBoard, movelist=chessData.movesdata("g6"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/g5", methods=['GET','POST'])
def g5():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="g5", allBoard=allBoard, movelist=chessData.movesdata("g5"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/g4", methods=['GET','POST'])
def g4():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="g4", allBoard=allBoard, movelist=chessData.movesdata("g4"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/g3", methods=['GET','POST'])
def g3():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="g3", allBoard=allBoard, movelist=chessData.movesdata("g3"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/g2", methods=['GET','POST'])
def g2():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="g2", allBoard=allBoard, movelist=chessData.movesdata("g2"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/g1", methods=['GET','POST'])
def g1():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="g1", allBoard=allBoard, movelist=chessData.movesdata("g1"), movesets=sets)
    return redirect("/project/chessDictTable/")

@app.route("/h8", methods=['GET','POST'])
def h8():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="h8", allBoard=allBoard, movelist=chessData.movesdata("h8"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/h7", methods=['GET','POST'])
def h7():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="h7", allBoard=allBoard, movelist=chessData.movesdata("h7"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/h6", methods=['GET','POST'])
def h6():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="h6", allBoard=allBoard, movelist=chessData.movesdata("h6"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/h5", methods=['GET','POST'])
def h5():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="h5", allBoard=allBoard, movelist=chessData.movesdata("h5"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/h4", methods=['GET','POST'])
def h4():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="h4", allBoard=allBoard, movelist=chessData.movesdata("h4"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/h3", methods=['GET','POST'])
def h3():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="h3", allBoard=allBoard, movelist=chessData.movesdata("h3"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/h2", methods=['GET','POST'])
def h2():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="h2", allBoard=allBoard, movelist=chessData.movesdata("h2"), movesets=sets)
    return redirect("/project/chessDictTable/")
@app.route("/h1", methods=['GET','POST'])
def h1():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="h1", allBoard=allBoard, movelist=chessData.movesdata("h1"), movesets=sets)
    return redirect("/project/chessDictTable/")

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True)