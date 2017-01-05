def fib1(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib1(n-1)+fib1(n-2)

print fib1(10)

def fib2(n):
    aux = []
    for i in range(n+1):
        aux.append(-1)
    return fib2Aux(n, aux)

def fib2Aux(n, aux):
    if aux[n] > 0:
        return aux[n]
    if n == 1:
        aux[n] = 1
    elif n == 2:
        aux[n] = 1
    else:
        aux[n] = fib2Aux(n-1, aux) + fib2Aux(n-2, aux)
    return aux[n]

print fib2(10)

def fib3(n):
    aux = []
    for i in range(n+1):
        aux.append(-1)
    aux[1] = 1
    aux[2] = 1
    for j in range(3, n+1):
        aux[j] = aux[j-1] + aux[j-2]
    return aux[n]

print fib3(10)

def fib4(n):
    return fib4Aux(n, 0, 1)

def fib4Aux(n, a, b):
    if n == 1:
        return b
    else:
        return fib4Aux(n-1, b, a+b)

print fib4(10)
