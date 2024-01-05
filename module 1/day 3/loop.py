a = int(input("Enter the number"))
c = 0

for i in range(1,a+1):
    if a%i == 0:
       c=c+1

if c == 2:
    print("Prime Number")
else:
    print("Not a prime number")
