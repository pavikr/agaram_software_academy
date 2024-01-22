a=int(input("Enter an amount:"))
print("press1 for 500  press2 for 200  press3 for 100 press4 for 50 press5 for 20 press6 for 10")
option=int(input("Enter your option:"))
if option==1:
    result=a/500
    print("no of 500 notes:",result)
elif option==2:
    result=a/200
    print("no of 200 notes:",result)
elif option==3:
    result=a/100
    print("no of 100 notes:",result)
elif option==4:
    result=a/50
    print("no of 50 notes:",result)
elif option==5:
    result=a/20
    print("no of 20 notes:",result)
elif option==6:
    result=a/10
    print("no of 10 notes:",result)
else:
    print("Invalid option")







