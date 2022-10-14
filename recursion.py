#one-branch: n! = n*(n-1)*(n-2)*...*1
#all about sub-problems...
#suppose we want to compute 5!:
def factorial(self, n: int) -> int:
    if (n<=1): return 1
    return n*factorial(n-1)
def factorial_while(self, n: int) -> int:
    res = 1
    while n>1:
        res *= n
        n -= 1
    return res

def fib(self, n: int) -> int: #O(2^n)
    if (n<=1): return n
    return fib(n-1)+fib(n-2)

#70 Climbing Stairs (DP), 2^n-2: n =5 yields 8 ways
def climbing(self, n: int) -> int:
    one, two = 1, 1
    for i in range(n-1):
        temp = one
        one += two
        two = temp
    return one