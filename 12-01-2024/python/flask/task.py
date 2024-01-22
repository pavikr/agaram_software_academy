from flask import Flask,request
app=Flask(__name__)

list=[]
@app.route("/active",methods=["GET"])
def active():
    return list

if __name__=="__main__":
    app.run(debug=True)