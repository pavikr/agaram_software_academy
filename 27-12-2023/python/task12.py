month=int(input("Enter month number:"))
if month==2:
    print("The number of days is 28 days")
elif (month==1 or month==3 or month==5 or month==7 or month==10 or month==12):
    print("The number of days is 31")
else:
    print("The number of days is 30 days")