from flask import Flask,request,render_template
app=Flask(__name__)

list=[]
@app.route("/active",methods=["GET","POST"])
def active():
    if request.method=="POST":
        list.append(request.form["item_name"])
    return render_template("task.html",itemList=list)



if __name__=="__main__":
    app.run(debug=True)