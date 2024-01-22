from flask import Flask,request,render_template
app=Flask(__name__)
books=[
        {"id":1,"title":"java", "author":"Author 1"}, 
        {"id":2,"title":"python", "author":"Author 2"},
        {"id":3,"title":"andriod", "author":"Author 3"}
]

@app.route("/books",methods=["GET"])
def get_books():
    return books

@app.route("/books/<int:book_id>",methods=["GET"])
def get_book(book_id):
    for book in books:
        if book["id"]==book_id:
            return book
    return {"error":"Book not found"}

@app.route("/new_book",methods=["GET","POST"])
def create_book():
    if request.method=="POST":
        add_book={
                "id":len(books)+1, 
                "title":request.form["b_title"], 
                "author":request.form["b_author"]}
        books.append(add_book)
        return books
    else:
        return render_template("task.html")
    
# @app.route("/update/<updatevalue>",methods=["GET","PUT","POST"])
# def updatedata(updatevalue):
#     if request.method=="POST":
#         books[int(updatevalue)]=request.form["updated_note"]
#         return books
#     else:
#         value=books[int(updatevalue)]
#         return render_template("updatedtask.html",value=value)
@app.route("/update/<updatevalue>",methods=["GET","POST","PUT"])
def updatedata(updatevalue):
    if request.method=="POST":
        update_book={
                "id":int(request.form["b_no"]),
                "title":request.form["b_title"], 
                "author":request.form["b_author"]}
        books[int(updatevalue)]=update_book
        return books
    else:
        value=books[int(updatevalue)]
        return render_template("updatedtask.html",value=value)
    
@app.route("/deletebook/<int:id_no>")
def deletevalue(id_no):
    for book in books:
        if book["id"]==id_no:
            books.remove(book)
            return books
        else:
            return "Not able to deletevalue"



# @app.route("/books/<int:book_id>",method="PUT")
# def update_book(book_id):
#     for book in books:
#         if book["id"]==book_id:
#             book["title"]=request.form["title"]
#             book["author"]=request.form["author"]
#             return book
#     return {"book not found"}



    
if __name__=="__main__":
    app.run(debug=True)





