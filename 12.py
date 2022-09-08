import math as m

def triangleNum(index):
    num = 0
    for i in range(0, index + 1):
        num += i
    return num

# create a function that returns the factors of a number
def factors(num):
    factors = []
    for i in range(1, int(m.sqrt(num)) + 1):
        if num % i == 0:
            factors.append(i)
            factors.append(num // i)
    return factors

n = 1
tri_n = 1

while len(factors(tri_n)) < 500:
    n += 1
    tri_n = triangleNum(n)

print(f"The first triangle number to have over 500 factors is {tri_n} at index {n}")
