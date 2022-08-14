# Q2/Write a program to find all prime numbers up to a given range of numbers?

def findPrime(num):
    flag = False
    if num > 1:
        for i in range(2, num):
            if (num%i) == 0:
                flag = True
                break
    else:
        flag = True
    return num if not flag else -1

def findPrimeOfRange(start_range, end_range):
    prime = []
    for num in range(start_range, end_range+1):
        primeResult = findPrime(num)
        if primeResult != -1:
            prime.append( findPrime(num) )
    return prime

def main():
    # start_rng = int(input('Enter start value : '))
    # end_rng = int(input('Enter end value : '))

    start_rng = 1
    end_rng = 10

    primeRange = findPrimeOfRange(start_rng,end_rng)

    print('The prime numbers between',start_rng,'and',end_rng,'are :', primeRange)

if __name__ == '__main__':
    main()
