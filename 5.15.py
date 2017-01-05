"cal the gcd"
def gcd(m, n):
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    return gcd(n, m%n)

print gcd(1,3) == 1
print gcd(2,4) == 2
print gcd(4, 12) == 4
print gcd(21, 15) == 3


def lcm(m, n):
    return (m*n)/gcd(m, n)

print lcm(1,3) == 3
print lcm(12, 8) == 24
