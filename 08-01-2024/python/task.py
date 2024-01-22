# mark=int(input("Enter your mark:"))
# if(mark>35):
#     print("pass")
# else:
#     print("fail")
# 
# input=int(input("Enter your number:"))
# if(input%3==0 and input%5==0):
#     print("It is divisible by both 3 and 5")
# else:
#     print("Not divisible by 3 and 5")
# a=int(input("Enter your number:"))
# if(a%2==0):
#     print("even")
# else:
#     print("odd")

# score=int(input("Enter your mark out of 100:"))
# if(score<35):
#     print("poor student")
# elif(score>35 and score<75):
#     print("avreage student")
# elif(score==75):
#     print("good student")

# a=int(input("Enter first input:"))
# b=int(input("Enter second input:"))
# choice=input("Whether to add/sub/mul/div:")
# if(choice=="add"):
#     print(a+b)
# elif(choice=="sub"):
#     print(a-b)
# elif(choice=="mul"):
#     print(a*b)
# elif(choice=="div"):
#     print(a/b)
# else:
#     print("invalid choice")
# percentage=int(input("Enter your percentage:"))
# if(percentage==75):
#     name=input("Enter your name:")
#     age=int(input("age:"))
#     location=input("Enter your location:")
#     print("selected")
# else:
#     print("not selected")
# salary=int(input("Enter salary:"))
# age=int(input("Enter your age:"))
# if(salary>20000 or age<=25):
#     loanamount=int(input("Enter your loan amount"))
#     if(loanamount>50000):
#         print("Maximum loan amount is 50000")
#     else:
#         print("invald amount")
#     print("You are eligible for loan")
# else:
#     print("you are not eligible for loan")
# print("marks out of 100")
# subject1=int(input("tamil:"))
# subject2=int(input("English:"))
# subject3=int(input("maths:"))
# subject4=int(input("science:"))
# subject5=int(input("social:"))
# total=subject1+subject2+subject3+subject4+subject5
# average=total/5
# if(average>35):
#     print(average,"add additional courses")
# else:
#     print(average,"not add additional courses")
# for i in "orange":
#     print(i)
# for i in range(1,11):
#     print(i,"x3=",i*3)
# for i in range(8,15):
#     print(i)
# a=int(input("num1:"))
# b=int(input("num2:"))
# for i in range(a+1,b):
#     print(i)
# for i in range(1,3):
#     print("week",i)
#     for i in range(1,8):
#         print("day",i)
for i in range(1,5):
    print()
    for j in range(1,i+1):
        print("*",end="")