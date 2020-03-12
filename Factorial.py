n=int(input("Enter the number to calculate factorial : "))
fact=1
for i in range(1,n):
    fact=fact*(i+1)
print(fact)