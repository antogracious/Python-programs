a=input("Which operation do you need +, -, *, / :")
b=float(input("Enter the first number :"))
c=float(input("Enter the second number :"))
if a=='+':
    d=b+c
    print(b,a,c,'=',d)
elif a=='-':
    d=b-c
    print(b,a,c,'=',d)
elif a=='*':
    d=b*c
    print(b,a,c,'=',d)
elif a=='/':
    d=b/c
    print(b,a,c,'=',d)
else:
    print("No valid operation selected")