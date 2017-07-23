# NAMESPACES AND SCOPES

# 1. FACTORIAL FUNCTION 
# 1.1 ITERATIVELY

def fact(num):
    result = 1
    if num>1:
        for f in range(2, num+1):
            result *= f
    return result


print(fact(4))


# 1.2 RECURSIVELY
def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)
# factorial(3) cannot be returned until factorial(2) is returned - underlying principle of recursive functions

print(factorial(4))


# 1. FIBONACCI FUNCTION 
# 1.1 ITERATIVELY
def fibo(n):
    if n == 0:
        result = 0
    if n == 1:
        result = 1
    else:
        a = 0
        b = 1
        for f in range(1, n):
            result = a+b
            b=a
            a=result
    return result




def fib(n):
    """ F(n) = F(n - 1) + F(n - 2) """
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)



print(fibo(4))
print(fib(4))


'''
The Fibonacci Sequence is the series of numbers:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

The next number is found by adding up the two numbers before it.

The 2 is found by adding the two numbers before it (1+1)
The 3 is found by adding the two numbers before it (1+2),
And the 5 is (2+3),
and so on!

'''