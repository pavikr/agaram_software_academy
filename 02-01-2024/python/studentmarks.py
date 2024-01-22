students_marks=[
                {
                "name":"ani",
                "place":"nagercoil",
                "major":"maths",
                "marks":[
                    {
                     "subject_name":"Tamil",
                     "max_marks":200,
                     "marks_scored":190
                    },
                    { 
                     "subject_name":"English",
                     "max_marks":200,
                     "marks_scored":180
                    },
                    {
                     "subject_name":"maths",
                     "max_marks":200,
                     "marks_scored":200
                    },
                    {
                     "subject_name":"physics",
                     "max_marks":200,
                     "marks_scored":170
                    },
                    {
                     "subject_name":"chemistry",
                     "max_marks":200,
                     "marks_scored":185
                    },
                    {
                     "subject_name":"Biology",
                     "max_marks":200,
                     "marks_scored":199
                    }
                     ],
                "age":18,
                "hobbies":["reading newspaper","singing","playing","dancing","cooking"],
                "gender":"male",
                "Ncc":"true",
                "sports":["football","chess","caram","basket ball","cricket"],
                "annual_income":85000
                },
                {
                "name":"sasi",
                "place":"thovalai",
                "major":"maths",
                "marks":[
                    {
                     "subject_name":"Tamil",
                     "max_marks":200,
                     "marks_scored":200
                    },
                    { 
                     "subject_name":"English",
                     "max_marks":200,
                     "marks_scored":185
                    },
                    {
                     "subject_name":"maths",
                     "max_marks":200,
                     "marks_scored":196
                    },
                    {
                     "subject_name":"physics",
                     "max_marks":200,
                     "marks_scored":188
                    },
                    {
                     "subject_name":"chemistry",
                     "max_marks":200,
                     "marks_scored":195
                    },
                    {
                     "subject_name":"Biology",
                     "max_marks":200,
                     "marks_scored":200
                    }
                ],
                "age":19,
                "hobbies":["searching internet","gardening","reading books","collecting games from newspaper"],
                "gender":"female",
                "Ncc":"false",
                "sports":["football","chess","caram","volley ball","cricket"],
                "annual_income":99000
                },
                 {
                "name":"sai",
                "place":"velladam",
                "major":"maths",
                "marks":[
                    {
                     "subject_name":"Tamil",
                     "max_marks":200,
                     "marks_scored":195
                    },
                    { 
                     "subject_name":"English",
                    "max_marks":200,
                     "marks_scored":184
                    },
                    {
                     "subject_name":"maths",
                     "max_marks":200,
                     "marks_scored":195
                    },
                    {
                     "subject_name":"physics",
                     "max_marks":200,
                     "marks_scored":186
                    },
                    {
                     "subject_name":"chemistry",
                     "max_marks":200,
                     "marks_scored":198
                    },
                    {
                     "subject_name":"Biology",
                     "max_marks":200,
                     "marks_scored":191
                    }
                ],
                "age":19,
                "hobbies":["drawing","swimming","writing books","collecting leaders pics","mehandi designing"],
                "gender":"female",
                "Ncc":"true",
                "sports":["basket ball","chess","caram","volley ball","cricket","kabadi","silambam"],
                "annual_income":100000
                },
                 {
                "name":"keerthana",
                "place":"aral",
                "major":"maths",
                "marks":[
                    {
                     "subject_name":"Tamil",
                     "max_marks":200,
                     "marks_scored":190
                    },
                    { 
                     "subject_name":"English",
                    "max_marks":200,
                    "marks_scored":199
                    },
                    {
                     "subject_name":"maths",
                     "max_marks":200,
                     "marks_scored":195
                    },
                    {
                     "subject_name":"physics",
                     "max_marks":200,
                     "marks_scored":190
                    },
                    {
                     "subject_name":"chemistry",
                     "max_marks":200,
                     "marks_scored":194
                    },
                    {
                     "subject_name":"Biology",
                     "max_marks":200,
                     "marks_scored":177
                    }
                ],
                "age":19,
                "hobbies":["searching internet","gardening","reading books","collecting games from newspaper"],
                "gender":"female",
                "Ncc":"false",
                "sports":["football","chess","caram","volley ball","cricket"],
                "annual_income":97000
                },
                 {
                "name":"anu",
                "place":"thovalai",
                "major":"maths",
                "marks":[
                    {
                     "subject_name":"Tamil",
                     "max_marks":200,
                     "marks_scored":199
                    },
                    { 
                     "subject_name":"English",
                     "max_marks":200,
                     "marks_scored":187
                    },
                    {
                     "subject_name":"maths",
                     "max_marks":200,
                     "marks_scored":193
                    },
                    {
                     "subject_name":"physics",
                     "max_marks":200,
                     "marks_scored":185
                    },
                    {
                     "subject_name":"chemistry",
                     "max_marks":200,
                     "marks_scored":190
                    },
                    {
                     "subject_name":"Biology",
                     "max_marks":200,
                     "marks_scored":198
                    }
                ],
                "age":19,
                "hobbies":["poem writing","cion collecting","temple visiting","art with fruits"],
                "gender":"female",
                "Ncc":False,
                "sports":["football","chess","caram","volley ball","cricket"],
                "annual_income":110000
                },
             ]

# for student in students_marks:
#     total=0                                           
#     for m in student["marks"]:
#              total=total+m["marks_scored"]
#     print(student["name"],total,total/1200*100)
tamil_highest=0
student_name=""
for each in students_marks:
    # tamil_highest=0
    for max in each["marks"]:
        if (max ["subject_name"]=="Tamil") and (max["marks_scored"]>tamil_highest):
            tamil_highest=max["marks_scored"]
            student_name=each["name"]
print(student_name,tamil_highest)

english_highest=0      
for each in students_marks:
#     english_highest=0
    for m in each["marks"]:
        if (m["subject_name"]=="English") and (m["marks_scored"]>english_highest):
            english_highest=m["marks_scored"]
            student_name=each["name"]
print(student_name,english_highest)   

maths_highest=0
for each in students_marks:
#     highest=0
    for m in each["marks"]:
        if (m["subject_name"]=="maths")and ( m["marks_scored"]>maths_highest):
            maths_highest=m["marks_scored"]
            student_name=each["name"]
print(student_name,maths_highest) 

physics_highest=0      
for each in students_marks:
    # highest=0
    for m in each["marks"]:
        if (m["subject_name"]=="physics") and (m["marks_scored"]>physics_highest):
            physics_highest=m["marks_scored"]
            student_name=each["name"]
print(student_name,physics_highest)

highest=0
for each in students_marks:
    # highest=0
    for m in each["marks"]:
        if (m["subject_name"]=="chemistry") and (m["marks_scored"]>highest):
            highest=m["marks_scored"]
print(highest) 

# for each in students_marks:
#     highest=0
#     for m in each["marks"]:
#         if m["subject_name"]=="Biology":
#             m["marks_scored"]>highest
#             highest=m["marks_scored"]
# print(highest)           











    
                
                
                
                

                
                


                    
                    

                  
              
