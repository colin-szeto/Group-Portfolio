import data
# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template, request, redirect
#create a Flask instance
app = Flask(__name__)

#InfoDb = []

#connects default URL of server to a python function
@app.route('/')
def home():
    #function uses Flask import (Jinga) to render HTML
    #data is passed as a parameter
    return render_template("home.html")#home has to be under templates

@app.route("/chessJs")#for the dragable chess file
def chessJS():

  return render_template("chessJs.html")

@app.route("/index")#for the dragable chess file
def index():
    return render_template("index.html", display="")

@app.route("/add", methods=['GET','POST'],)#for the dragable chess file
def addition():
    if request.method == 'POST':
        form = request.form
        numberOne = int(form['numOne'])
        numberTwo = int(form['numTwo'])
        calc = numberOne + numberTwo
        return render_template("index.html", your_list = data.answersdata(calc))#data.playlist()

    return redirect("/index")

@app.route("/journals")#for storing all the links to the webpage
def journals():
  return render_template("journals.html",repl="repl of website", website ="link to personal website")#allows to define the text that is hyperlinked on the the personal journals

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True)