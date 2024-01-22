students=["pavi","sasi","anitha","mano","venkat"]
for student in students:
    print(student)

name="preethi"
for each in "preethi":   
    print(each)
for each in range(10):
    print(each)
for each in range(len(students)):
    print(students[each])
for each in range(2,4):
    print(each)
for each in range(2,20,5):
    print(each)

for each in range(10):
    print(each)
    if(each==7):
        print(" is my lucky number")

for each in range(5):
    if(each%2==0):
        print(each,"even number")
    else:
        print(each,"odd number")

for each in range(100):
    if(each%3==0):
        print(each,"each is divisible by 3")

for each in range(100):
    if(each%3==0 and each%9==0):
        print(each,"It is divisible by 3 and 9")

for each in range(100):
    if(each%7==0 or each%13==0):
        print(each,"It is diviible by 7 or 13")

for each in range(100):
    if(each>90):
        print(each,"biggest numbers")
    else:
        print(each,"smallest numbers")

list=[15,10,20,90,80]
largest_number=0
for each in list:
    if each>largest_number:
        largest_number=each
print("largest number is",largest_number)


for each in range(1,100):
    largest_number=0
if each>largest_number:
    largest_number=each
    print(largest_number)

range_input=int(input("Enter an input:"))
largest_number=0
for each in range(1,range_input):
    if each>largest_number:
         largest_number=each
print(largest_number)





    

        


