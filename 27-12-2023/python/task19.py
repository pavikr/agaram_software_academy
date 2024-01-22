mark1=int(input("Enter your physics mark:"))
mark2=int(input("Enter your chemistry mark:"))
mark3=int(input("Enter your maths mark:"))
mark4=int(input("Enter your biology mark:"))
mark5=int(input("Enter your computer mark:"))
percentage=(mark1+mark2+mark3+mark4+mark5)/500*100
if percentage>=90:
    print("grade A")
elif percentage>=80 and percentage<90:
    print("grade B")
elif percentage>=70 and percentage<80:
    print("grade C")
elif percentage>=60 and percentage<70:
    print("grade D")
elif percentage>=40 and percentage<60:
    print("grade E")
elif percentage<40:
    print("grade F")
else:
    print("invalid input")
   

