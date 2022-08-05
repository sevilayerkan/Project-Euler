#Author: @sevilayerkan
#Date: 2022-07-25

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

#Check given number is prime
def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

#Find the nth prime number
def nthPrime(n):
    i = 1
    count = 0
    while count < n:
        i += 1
        if isPrime(i):
            count += 1
    return i

#Main function 
if __name__ == "__main__":
    print(nthPrime(10001))

