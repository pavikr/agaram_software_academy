# from flask import Flask
# from flask import render_template
# app=Flask(__name__)
# @app.route("/welcome")
# def list():
#     return"hello"
# @app.route("/hi")
# def add():
#     return"welcome"
# @app.route("/user/<name>")
# def printusername(name):
#     return name




from flask import Flask
from flask import render_template
app=Flask(__name__)
@app.route("/input/<name>")
def renderHTML(name):
    return render_template("home.html",name="a")



from flask import Flask
from flask import render_template
app=Flask(__name__)
@app.route("/input")
def renderHTML():
    users=["anu","pavi","sai","parvathi"]
    return render_template("home.html",name=users)
