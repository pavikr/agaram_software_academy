my_resume={
          "name":"C.Pavithra",
           "e_mail_address":"pavidhaks@gmail.com",
           "objectives":"I am excited to apply the position of developer interested to working with team mates",
           "education":[
                    { 
                      "course":"BE_computerscience_and_engineering:8.25",
                      "instution name":"anna university thovalai",
                      "year":"2012_2016"
                    },
                    {
                      "course":"higher_secondary_eduction",
                      "instution name":"ghss_thovalai",
                      "year":2012
                    }],
        "experience":[
                   {
                    "company_name":"tcs_technology",
                    "year":"2017-2019",
                    "position":"tester",
                    "year_of_experience":2
                   }, 
                   {
                    "company_name":"Lava_technology",
                     "year":"2020-2023",
                     "position":"developer",
                     "year_of_experience":3
                   },
                    ],

        "technical_qualification":["java","html","mysql","networking"],

        "project": [
                    {"name":"Net banking",
                    "duration":"8 months",
                    "organization":"frame work,citi",
                    "team_size":5,
                    "description": "The main objective of this project is to create a internet banking website by which the bank customers can make transactions like Balance In Statement View,bill pay form the convenience of their homes.Normally the customers wouldhave to make a trip to the bank to do these transactions but with the avent of internet banking the ease of account operation for  customers has gone up.All the customer require is a PC with an internet connection and internet banking login id and password to use this facility",
                    "role":["Worked as a Team leader","performed coding using java",".net","html","I am responsible for some part of coding and database work"],
                    "technology":["java","Mysql database"],
                    "operating_system":"windows 10"}, 

                    {"name":"school management system",
                    "duration":"6 months",
                    "organization":"reeta,citi",
                    "team_size":5,
                    "description":"it is used to store all the school related records,related inforation to students and teachers.",
                    "role":"performed coding using mysql,database work",
                    "technology":["java","Mysql","database"],
                    "operating_system":"windows 10"},
                    ],
        "personal_details":{"date_of_birth":"16_02_1995",
                            "father_name":"chandran",
                            "languages_known":["tamil","english","malayalam"],
                            "address":"7/63,main_road,thovalai",
                            "hobbies":["singing","book reading","garderning"],
                            "strengths":["Hard working","Honest","Leadership quality","Confident"],
                             },              
       
        "declaration":"i here by inform that all information true to the best of my knowledge"}

# print(my_resume["project"][0])     
# print(my_resume["personal_details"]["languages_known"]) 
# print(my_resume["education"][1])                            
# a=my_resume["education"]
# education=a.append({"course":"ME_computerscience_and_engineering:8.25",
#                       "instution name":"anna university thovalai",
#                       "year":"2016_2018"})
# print(a)
# b=my_resume["project"]
# project=b.append({"name":"library management system",
#                     "duration":"10 months",
#                     "organization":"reeta,citi",
#                     "team_size":4,
#                     "description":"it is used to collect all the records from books,related inforation to students and teachers.",
#                     "role":"performed coding using mysql,database work",
#                     "technology":["php","Mysql","database"],
#                     "operating_system":"windows 10"},)
# print(b)

# for resume in my_resume["education"]:
#     if resume["course"]=="higher_secondary_eduction":
#           resume["course"]="12th"

# print(my_resume["education"])

# a=input("if you add any project?yes/no:")
# if a=="yes":
#      name=input("Enter your project name:")
#      duration=input("Enter your project duration:")
#      organization=input("Enter your organization name:")
#      team_size=int(input("Enter your team size"))
#      description=input("enter your project description:")
#      role=input("enter your role of your project:")
#      technology=input("what technologies are used?")
#      operating_system=input("Enter your project operating system")
#      b={}
#      b["name"]=name
#      b["duration"]=duration
#      b["organization"]=organization
#      b["team_size"]=team_size
#      b["description"]=description
#      b["role"]=role
#      b["technology"]=technology
#      b[ "operating_system"]=operating_system
#      my_resume["project"].append(b)




#      print(my_resume["project"])
# else:
#     print("Invalid")
# my_resume["project"].append({
#                             "name":name,
#                             "duration":duration,
#                             "organization":organization,
#                             "team_size":team_size,
#                             "description":description,
#                             "role":role,
#                             "technology":technology,
#                             "operating_systemr":operating_system
#                             })
# print(my_resume["project"])
# def print_my_name():
#   a=my_resume["education"]
#   if len(a)<2:
#       a.append({"course":"ME_computerscience_and_engineering:8.25",
#                       "instution name":"anna university thovalai",
#                       "year":"2016_2018"})
#   print(a)

# print_my_name()

# def add():
#    print(first_no+second_no)
# a=int(input("enter your first no:"))
# b=int(input("enter your second no:"))
  
# add(a,b)
         

# def add(a,b,c):
#    my_resume["education"].append({"course":a,
#                                   "instution-name":b,
#                                   "year":c

#                                   })
#    print(my_resume["education"])
# course=input("Enter your course name:")
# instution_name=input("Enter your instution name")
# year=int(input("passed out year:"))
# add(course,instution_name,year)
            
     

# def add(a,b,c):
#    my_resume["education"].remove({"course":a,
#                                   "instution-name":b,
#                                   "year":c

#                                   })
#    print(my_resume["education"])
# course=input("Enter your course name:")
# instution_name=input("Enter your instution name")
# year=int(input("passed out year:"))
# add(course,instution_name,year)
# 

# def addname():
#     return [1,2,3]
# name=addname()
# print(name)
def add(list):
    # print(list)
    askuser=input("do you want to add information:")
    if askuser=="yes":
      course=input("Enter your course name:")
      instution_name=input("Enter your instution name")
      year=int(input("passed out year:"))
      list.append({"course":course,
                   "instution_name":instution_name,
                   "year":year
                  })
      return list
updatedlist=add(my_resume["education"])
my_resume["education"]=updatedlist
print(my_resume["education"])
    




            
               
