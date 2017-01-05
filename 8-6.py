def isprime(num):
    if num == 1:
        return False
    count = num/2
    while count > 1:
        if num % count == 0:
            return False
        count -= 1
    return True

#print isprime(5)
#print isprime(10)
#print isprime(2)
#print isprime(1)

def getfactors(num):
    allFactors = []
    for i in range(1, num+1):
        if num % i == 0:
            allFactors.append(i)
    return allFactors

#print getfactors(10)

def primeFactorization(num):
    factorization = []
    primeFactors = []
    allFactors = getfactors(num)
    for i in allFactors:
        if isprime(i):
            primeFactors.append(i)
    for j in primeFactors:
        while num % j == 0:
            factorization.append(j)
            num /= j
    return factorization
        
print primeFactorization(20)
