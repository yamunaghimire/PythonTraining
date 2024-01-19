def multiplication_table(number):
    for i in range(1,11):
     result = number * i
     print(f"{number} * {i} = {result}") #f-string

#number = int(input("Enter a number"))
for i in range(10):
 multiplication_table(i)
