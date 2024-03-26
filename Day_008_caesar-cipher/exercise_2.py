#Check to see if a number is a prime number

n = int(input("Please enter a number to check if it is a prime number: "))

#calculation
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
       if number % i == 0:
           is_prime = False
    if is_prime:
        print("This number is a prime number.")
    else:
        print("This number is not a prime number.")

prime_checker(number = n)