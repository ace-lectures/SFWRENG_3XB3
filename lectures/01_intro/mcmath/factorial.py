from functools import wraps, reduce
from operator import mul
from tail_recursive import tail_recursive

## Domain Checker (using Python Decorators)

def ensure_domain(function):
    @wraps(function)
    def checker(*args):
        if args[0] < 0:
            raise ValueError("Arg must be >= 0")
        return function(*args)
    return checker

## Classical imperative programming

@ensure_domain
def fac_while(n: int) -> int:
    """https://www.geeksforgeeks.org/python-program-for-factorial-of-a-number/"""
    if n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact

@ensure_domain
def fac_for(n: int) -> int:
    """https://www.geeksforgeeks.org/python-program-for-factorial-of-a-number/"""
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

@ensure_domain
def fac_oneline(n:int) -> int:
    """https://stackoverflow.com/questions/51777932/writing-a-factorial-function-in-one-line-in-python"""
    return reduce(mul, range(1, n + 1), 1)


## Classical Recursive programming

@ensure_domain
def fac_rec(n:int) -> int:
    if n <= 1:
        return 1
    else:
        return n * fac_rec(n - 1)

@ensure_domain
def fac_rec_oneline(n: int) -> int:
    return n * fac_rec(n - 1) if n > 1 else 1

## Recursive programming, tail recursive calls

@ensure_domain
def fac_acc(n: int, acc: int = 1) -> int:
    if n <= 1:
        return acc
    else:
        return fac_acc(n - 1, n * acc)

@ensure_domain
def fac_acc_oneline(n: int, acc: int = 1) -> int:
    return fac_acc_oneline(n - 1, n * acc) if n > 1 else acc

## Forcing tail recursion in python

@tail_recursive
@ensure_domain
def fac_tailrec(n: int) -> int:
    if n <= 1:
        return n
    return n * fac_tailrec.tail_call(n - 1)


@tail_recursive
@ensure_domain
def fac_tailrec_oneline(n: int) -> int:
    return n * fac_tailrec_oneline.tail_call(n - 1) if n > 1 else 1