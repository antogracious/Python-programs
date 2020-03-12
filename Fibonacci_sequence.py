first_number=int(input("Enter the first number :"))
second_number=int(input("Enter the second number :"))
nterms=int(input("Enter the number of terms :"))
count=0
while(count < nterms):
    print(first_number)
    total_number=first_number+second_number
    first_number=second_number
    second_number=total_number
    count+=1
    
    