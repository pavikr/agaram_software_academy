a=int(input("Enter the first value:"))
b=int(input("Enter the second value:"))
c=int(input("Enter the first value:"))
if ((a+b>c)==(a+c>b)==(b+c>a)):
    print("The given triangle is valid")
else:
    print("The given triangle is invalid")
