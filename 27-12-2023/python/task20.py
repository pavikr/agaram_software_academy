basic=float(input("Enter basic salary:"))
if(basic<=10000):
    hra=float(basic*0.20)
    da=float(basic*0.8)
    grosspay=float(basic+hra+da)
    print("gross salary is",grosspay)
elif(basic>10000 and basic<=20000):
    hra=float(basic*0.25)
    da=float(basic*0.9)
    grosspay=float(basic+hra+da)
    print("gross salary is",grosspay)
elif(basic>20000):
    hra=float(basic*0.30)
    da=float(basic*0.85)
    grosspay=float(basic+hra+da)
    print("gross salary is",grosspay)
else:
    print("Invalid amount")








