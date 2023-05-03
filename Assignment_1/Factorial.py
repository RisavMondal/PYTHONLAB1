print("ARNAV GHOSH Class Roll:- 55")

n = int(input("Enter a number: "))
fact = 1

if(n == 0 or n ==1):
    print("Factorial of number:" ,1)
else:
    for i in range(1,n+1):
        fact = fact * i
print(fact)