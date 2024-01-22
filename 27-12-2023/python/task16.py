a=int(input("Enter the first value:"))
b=int(input("Enter the second value:"))
c=int(input("Enter the third value:"))
if(a==b==c==a):
    print("The triangle is equilateral")
elif((a==b or b==c or c==a)):
    print("The triangle is isosceles")
else:
    print("The triangle is scalene")