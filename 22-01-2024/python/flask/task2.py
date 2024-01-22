from flask import Flask,request,render_template
app=Flask(__name__)
details=[
    {"name":"pavithra","age":24, "place":"thovalai"},
     {"name":"sasiithra","age":23, "place":"aral"},
     {"name":"athira","age":22, "place":"layam"}
]

@app.route("/details",methods=["GET"])
def get_details():
    return details

# @app.route("/new_details/<updatevalue>",methods=["GET","POST","PUT"])
# def new(updatevalue):
#     if request.method=="POST":
#         update_details={
#                         "name":request.form["student_name"],
#                         "age":int(request.form["student_age"]),
#                         "place":request.form["location"]
#                         }
        
#         details[int(updatevalue)]=update_details
#         return details
#     else:
#         value=details[int(updatevalue)]
#         return render_template("updation.html",value=value)
# @app.route("/deletion/<Name>")
# def delt(Name):
#     for detail in details:
#         if detail["name"]==Name:
#             details.remove(detail)
#             return details
#         else:
#             "not delete any value"
@app.route("/newdetails", methods=["GET","POST"])
def newdata():
    if request.method=="POST":
        add_details={"name":request.form["student_name"],
                    "age":int(request.form["student_age"]),
                    "place":request.form["location"]}
        details.append(add_details)
        return details
    else:
        return render_template("home.html")
    


@app.route("/new/<checkvalue>",methods=["GET"])
def data(checkvalue):
    for detail in details:
        if detail["name"]==checkvalue:
            return detail


if(__name__)=="__main__":
    app.run(debug=True)

