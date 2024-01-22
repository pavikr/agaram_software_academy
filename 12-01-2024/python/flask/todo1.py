from flask import Flask,render_template,request
app=Flask(__name__)
list=[]


@app.route("/todo",methods=["GET","POST"])
def todo():
    
    if request.method=="POST":
        list.append(request.form["item_name"])
    return render_template("index.html",itemList=list)


@app.route("/deltodo/<delval>",methods=["GET","POST"])
def delItem(delval):
    list.remove(delval)
    
    return render_template("index.html",itemList=list)


@app.route("/updatetodo/<v_index>",methods=["GET","POST","PUT"])
def updatetodo(v_index):
    if request.method=="POST":
        list[int(v_index)]=request.form["updated_item"]
        return render_template("index.html",itemList=list)
    else:
        value=list[int(v_index)]
        return render_template("update.html",value=value)






if __name__=="__main__":
    app.run(debug=True)