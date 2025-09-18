"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable, List

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$



# TODO: Implement for Task 0.1.

def mul(x: float, y: float) -> float:
    return x * y

def id(x: float) -> float:
    return x

def add(x: float, y: float) -> float:
    return x + y

def neg(x: float) -> float:
    return -x

def lt(x: float, y: float) -> float:
    if x < y:
        return 1.0
    else:
        return 0.0


def eq(x: float, y: float) -> float:
    if x == y:
        return 1.0
    else:
        return 0.0

def max(x: float, y: float) -> float:
    if x > y:
        return x
    else:
        return y

def is_close(x: float, y: float) -> bool:
    return abs(x - y) < 1e-2

def sigmoid(x: float) -> float:
    if x >= 0.0:
        z = math.exp(-x)
        return 1.0 / (1.0 + z)
    else:
        z = math.exp(x)
        return z / (1.0 + z)

def relu(x: float) -> float:
    if x > 0.0:
        return x
    else:
        return 0.0

def log(x: float) -> float:
    return math.log(x)

def exp(x: float) -> float:
    return math.exp(x)

def log_back(y: float, x: float) -> float:
    if x == 0.0:
        return 0.0
    else:
        return y / x

def inv(x: float) -> float:
    return 1.0 / x

def inv_back(y: float, x: float) -> float:
    if x == 0.0:
        return 0.0
    else:
        x_squared = x * x
        if x_squared == 0.0:
            return 0.0
        return -y / x_squared

def relu_back(x: float, y: float) -> float:
    if x > 0.0:
        return y
    else:
        return 0.0

# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.

def map(f: Callable[[float], float], x: Iterable[float]) -> list[float]:
    result = []
    for i in x:
        result.append(f(i))
    return result

def zipWith(f: Callable[[float, float], float], a: Iterable[float], b: Iterable[float]) -> list[float]:
    result = []
    for i, j in zip(a, b):
        result.append(f(i, j))
    return result

def reduce(f: Callable[[float, float], float], x: Iterable[float], s: float) -> float:
    for i in x:
        s = f(s, i)
    return s

def negList(x: Iterable[float]) -> list[float]:
    return map(neg, x)

def addLists(a: Iterable[float], b: Iterable[float]) -> list[float]:
    return zipWith(add, a, b)

def sum(x: Iterable[float]) -> float:
    return reduce(add, x, 0.0)

def prod(x: Iterable[float]) -> float:
    return reduce(mul, x, 1.0)
