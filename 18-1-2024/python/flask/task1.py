from flask import Flask,request,render_template
app=Flask(__name__)
employee_details=[
                {"e_no":1,"e_name":"pavi","position":"Team Leader"},
                {"e_no":2,"e_name":"sasi","position":"Tester"},
                {"e_no":3,"e_name":"Sai","position":"HR"},
]


@app.route("/employee_details",methods=["GET"])
def get_employees():
    return employee_details

@app.route("/employee_details/<int:emp_no>",methods=["GET"])
def get_employee(emp_no):
    for e_details in employee_details:
        if e_details["e_no"]==emp_no:
            return e_details
    return "Error Not Found"

@app.route("/new_details",methods=["GET","POST"])
def new_employee():
    if request.method=="POST":
        add_employee={"e_no":len(employee_details)+1,
                      "e_name":request.form["emp_name"],
                      "position":request.form["emp_position"]}
        
        employee_details.append(add_employee)  
        return employee_details
    else:
        return render_template("task1.html")   
@app.route("/updation/<updatevalue>",methods=["GET","POST","PUT"])  
def newdata(updatevalue):
    if request.method=="POST":
        update_details={"e_no":int(request.form["emp_no"]),
                        "e_name":request.form["emp_name"],
                        "position":request.form["emp_position"]
                        }   
        employee_details[int(updatevalue)]=update_details
        return employee_details
    else:
        value=employee_details[int(updatevalue)]
        return render_template("update.html",value=value)

@app.route("/deletion/<int:em_no>")
def deldata(em_no):
    for i in employee_details:
        if i["e_no"]== em_no:
            employee_details.remove(i)
            return employee_details
        else:
            return "not found"

if __name__=="__main__":
    app.run(debug=True)