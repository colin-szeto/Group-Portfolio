# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template
#create a Flask instance
app = Flask(__name__)

# Data setup (Listy)
ProjectName = "Project Name"
ProjectPlan = "Project Plan"
Repl = "Repl"
Resources = "Resources"
InfoDb = []
# First Project
InfoDb.append({ProjectName: "Hello Series Project", ProjectPlan: "http://nighthawkcoders.cf/courses/python/", Repl: "https://repl.it/@jmort1021/Python-Hello-Series#README.mn", Resources: "https://padlet.com/jmortensen7/csp2021" })
# Second Project
InfoDb.append({ProjectName: "Flask Project", ProjectPlan: "http://nighthawkcoders.cf/courses/python/", Repl: "https://repl.it/@jmort1021/Web-Portfolio-Series#main.py", Resources: "https://padlet.com/jmortensen7/csptime1_2" })
InfoDb.append({ProjectName: "Future Project", ProjectPlan: "http://nighthawkcoders.cf/courses/python/", Repl: "https://repl.it/@jmort1021/Web-Portfolio-Series#main.py", Resources: "https://padlet.com/jmortensen7/csptime1_2" })

#connects default URL of server to a python function
@app.route('/')
def home():
    #function uses Flask import (Jinga) to render HTML
    #data is passed as a parameter
    return render_template("home.html", data=InfoDb)

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port='3000', host='0.0.0.0')