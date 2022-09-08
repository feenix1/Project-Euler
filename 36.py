# find if integer is a palindrome in base 10 and base 2
def isPalindrome(n):
    if n < 0:
        return False
    else:
        return str(n) == str(n)[::-1] and bin(n)[2:] == bin(n)[2:][::-1]

palindromeList = []

for num in range(1, 1000000):
    if isPalindrome(num):
        palindromeList.append(num)

print(palindromeList)
print(sum(palindromeList))