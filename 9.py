# find if a value is a pythagorean triplet
def is_triplet(a, b, c):
    if a**2 + b**2 == c**2 and a < b < c:
        return True
    else:
        return False

solved = 0
# this is the worst way to do this

for a in range(0, 1000):
    if solved == 1:
        break
    for b in range(a + 1, 1000):
        if solved == 1:
            break
        for c in range(b + 1, 1000):
            if solved == 1:
                break
            if a + b + c == 1000:
                if is_triplet(a, b, c):
                    print(a, b, c)
                    print(a*b*c)
                    solved = 1
                    break