unit=int(input("Enter total unit consumed:"))
if(unit<=50):
    amount=(unit*0.50)
    print("The bill amount is:",amount)
elif(unit<=150):
    amount=(50*0.50+(unit-50)*0.75)
    print("The bill amount is:",amount)
elif(unit<=250):
    amount=(50*0.50+(150-50)*0.75+(unit-150)*1.20)
    print("The bill amount is:",amount)
else:
    amount=50*0.50+(150-50)*0.75+(250-150)*1.20+(unit-250)*1.50
    surcharge=amount*0.20
    total=amount+surcharge
    print("Total electricity bill of Rs:",total)
    


