import sys
x = 0
sys.setrecursionlimit(3000)
def f(n):
    if n <= 5:
        return n
    if n > 5 and n % 8 == 0:
        return  n + f(n/2 -3)
    if n > 5 and n % 8 != 0:
        return f(n + 4) + n

print(f(8))
    
