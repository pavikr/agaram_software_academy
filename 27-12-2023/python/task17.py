a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
d=b**2-4*a*c
e=d**0.5
r1=(-b+e)/2*a
r2=(-b-e)/2*a
if(d<0):
    print("The roots are imaginery  ",r1,r2)
elif(d>0):
     print("The roots are real and distinct ",r1,r2)
elif(d==0):
     print("The roots are real and equal ",r1,r2)