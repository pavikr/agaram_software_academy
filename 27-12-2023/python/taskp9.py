ch=input("enter any input:")
if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
    print(ch,"is an alphabet")
elif(ch>='0' and ch<='9'):
    print(ch,"is a digit")
else:
    print(ch,"is a special characters")