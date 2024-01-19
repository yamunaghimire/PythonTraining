def check_prime(number):
    counter = 0
    prime = False
    for i in range(1,number+1):
        if number % i == 0:
            counter = counter + 1
    
    if counter == 2:
        return True

    return prime

def multiplication_table(number):
    for i in range(1,11):
     result = number * i
     print(f"{number} * {i} = {result}") #f-string

#number = int(input("Enter a number"))
# for i in range(10):
#  multiplication_table(i)

    
#number = int(input("Enter a number to check prime"))
# for i in range(30):
# check_prime = check_prime(number)

if check_prime(number):
 multiplication_table(i)

    
