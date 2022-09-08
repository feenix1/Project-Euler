# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p ≤ 1000, is the number of solutions maximised?

maxP = 0
maxSolutions = 0

for p in range(3,1001):
    solutions = 0
    
    for a in range(1, p // 3):
        for b in range(a, p // 2):        
            c = p - a - b

            if a**2 + b**2 == c**2:
                solutions += 1
    
    if solutions > maxSolutions:
        maxSolutions = solutions
        maxP = p

print(f"Highest solution count is {maxSolutions} with perimeter value {maxP}")