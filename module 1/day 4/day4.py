def check_prime(number):
    counter = 0
    prime = False
    for i in range(1,number+1):
        if number % i == 0:
            counter = counter + 1
    
    if counter == 2:
        return True

    return prime
    
number = int(input("Enter a number to check prime"))
check_prime = check_prime(number)

if check_prime:
    print("Prime Number")
else:
    print("Not a Prime Number")


