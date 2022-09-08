import os
import math as m
import datetime as dt

# =========================
# Project Euler: Problem 24
# =========================
#
# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically,
# we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are: 
#
# 012 021 102 120 201 210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
#
# ====================================================================================================
#
# What steps do we need to take to solve this problem?
#
# 1. We need to find all the permutations of the digits 0-9 and store them in a list
# 2. We need to sort the list in lexicographic order
# 3. We need to find the millionth element in the list
#
# ====================================================================================================

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def perf(func, *args):
    start = dt.datetime.now()
    output = func(*args)
    return output, dt.datetime.now() - start


# create a list of all the permutations of the digits 0-9


answer = "placeholder"

# ==================================================

if answer != 2783915460:
    print("Incorrect answer, try again")
else:
    print("Correct answer")