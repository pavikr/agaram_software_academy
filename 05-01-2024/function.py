# resume={}
# getname=input("Enter your name:")
# resume["name"]=getname
# e_mail_address=input("Enter your email address:")
# resume["email_address"]=e_mail_address
# objectives=input("Enter your objectives:")
# resume["objectives"]=objectives
# declaration=input("update declaration:")
# resume["declaration"]=declaration
# education=int(input("How many education did you have?"))
# resume["education"]=[]
# for each in range(1,education):
#         instution_name=input("Enter your instution name:")
#         course=input("Enter your course name:")
#         percentage=int(input("Enter your pecentage:"))
#         year=int(input("Enter your passed out year:"))
# resume["education"].append({"instution_name":instution_name,
#                             "course":course,
#                             "percentage":percentage,
#                             "year":year
#                         })
# project=int(input("How many project did you have?"))
# resume["project"]=[]
# for each in range(project):
#     name=input("project name")
#     duration=input("duration")
# resume["project"].append({"name":name,
#                           "duration":duration})


# print(resume)

# resume={}
# education=int(input("NO of education:"))
# resume["education"]=[]


# def add(education,list):
#     for each in range(education):
#         coursename=input("Enter your coursename:")
#         instution_name=input("Enter your instution name")
#         list.append({"coursename":coursename,
#                             "instution_name":instution_name
#                             })






# add (education,resume["education"])


# print(resume)


# def add(list):
#         print(list)
# for each in range(0,education):
#         coursename=input("Enter your coursename:")
#         instution_name=input("Enter your instution name")
# resume["education"].append({"coursename":coursename,
#                             "instution_name":instution_name
#                             })

# add(resume["education"])
# updatedresume=add(resume["education"])
# print(updatedresume)
                


resume={}
# getname=input("Name:")
# resume["name"]=getname
# email_address=input("emailaddress:")
# resume["email_address"]=email_address
# objectives=input("Objectives")
# resume["objectives:"]=objectives
# declaration=input("Enter your declaration:")
# resume["declaration"]=declaration
# education=int(input("How many education did you want?"))
# resume["education"]=[]
# for each in range(education):
#     instution_name=input("instution name:")
#     coursename=input("coursename:")
#     percentage=int(input("percentage:"))
# resume["education"].append({
#                             "instution_name":instution_name,
#                             "coursename":coursename,
#                             "percentage":percentage})
# project=int(input("How many project did you have?"))
# resume["project"]=[]
# for each in range(project):
#     name=input("project name")
#     duration=input("duration")
# resume["project"].append({"name":name,
#                           "duration":duration})
# technical_qualification=int(input("How many skill did you have?"))
# resume["technical_qualification"]=[]
# for each in range(technical_qualification):
#     skill=input("Enter your skills:")
#     resume["technical_qualification"].append(skill)
# experience=int(input("How many experience did you have?"))
# resume["experience"]=[]
# for each in range(experience):
#     company_name=input("Enter your company name:")
#     year=input("enter year:")
#     position=input("Enter your position:")
#     year_of_experience=int(input("Enter your experience:"))
# resume["experience"].append({"company_name":company_name,
#                              "year":year,
#                              "position":position,
#                              "year_of_experience":year})
# personaldetails=input("how many personal details add?")                            
resume["personaldetails"]={}
# for each in range(personaldetails):                           
date_of_birth=input("Enter your date_of_birth:")
father_name=input("Enter your father's name:")
resume["personaldetails"]["date_of_birth"]=date_of_birth
resume["personaldetails"][father_name]=father_name
languages_known=int(input("How many languages did you have know?"))
resume["personaldetails"]["languages_known"]=[]
for each in range(languages_known):
    languages_known=input("languages:")
    resume["personaldetails"]["languages_known"].append(languages_known)                   
address=input("Enter your address:")
resume["personaldetails"]["address"]=address
hobbies=int(input("How many hobbies did you have?"))
resume["personaldetails"]["hobbies"]=[]
for each in range(hobbies):
    hobbies=input("Enter your hobbies:")
    resume["personaldetails"]["hobbies"].append(hobbies)
strength=input("Enter your strength:")
resume["personaldetails"]["strength"]=strength
                             

print(resume)






# def add(education,list):
#     for each in range(education):
#         instution_name=input("instution name:")
#         coursename=input("coursename:")
#         percentage=int(input("percentage:"))
#         list.append({
#                     "instution_name":instution_name,
#                      "coursename":coursename,
#                      "percentage":percentage
#         })
# add(education,resume["education"])
# print(resume)

# def add(project,list):
#     for each in range(project):

#         name=input("project name")
#         duration=input("duration")
# resume["project"].append({"name":name,
#                           "duration":duration})




# add(project,resume["project"])
# print(resume)