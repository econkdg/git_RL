# ====================================================================================================
# DP: dynamic programming
# ====================================================================================================
# import library

import numpy as np
import timeit

from sqlalchemy import value_sets
# ----------------------------------------------------------------------------------------------------
# recursive algorithm

# 1. foo example

print('{c}\n'.format(c='hello class'))
print('hello class')


def foo(str):
    print(str)


foo('hello class')

# infinite loop -> do not run!


def foo_recursion(str):

    print(str)
    foo_recursion(str)

# base case


def foo_recursion_correct(n):

    # base case
    if n <= 0:  # set break out point
        return

    else:
        print('hi \n')
        foo_recursion_correct(n-1)


foo_recursion_correct(4)

# 2. factorial example

# case (1)
print(range(5))

n = 5
m = 1

for i in range(n):

    m = m*(i+1)

print(m)

# case (2): recursive


def fac(n):

    if n == 1:
        return 1

    else:
        return n*fac(n-1)


fac(5)
# ----------------------------------------------------------------------------------------------------
# dynamic programming (1)

# naive Fibonacci


def fib(n):

    if n <= 2:
        return 1

    else:
        return fib(n-1) + fib(n-2)


fib(10)
# ----------------------------------------------------------------------------------------------------
# dynamic programming (2)

# memorized DP Fibonacci


def mfib(memo, n):

    if memo[n-1] != 0:
        return memo[n-1]

    elif n <= 2:
        memo[n-1] = 1
        return 1

    else:
        memo[n-1] = mfib(memo, n-1) + mfib(memo, n-2)
        return memo[n-1]


n = 10
memo = np.zeros(n)

mfib(memo, n)

# time(s) for fib()
start = timeit.default_timer()
fib(30)
end = timeit.default_timer()
print(end - start)

# time(s) for mfib()
start = timeit.default_timer()
memo = np.zeros(30)
mfib(memo, 30)
end = timeit.default_timer()
print(end - start)
# ----------------------------------------------------------------------------------------------------
# dynamic programming (3)

# climbing a stair problem

# case (1)


def stair(memo_1, n):

    if memo_1[n-1] != 0:
        m = memo_1[n-1]

    elif n == 1:
        m = 1
        memo_1[n-1] = m

    elif n == 2:
        m = 2
        memo_1[n-1] = m

    elif n == 3:
        m = 4
        memo_1[n-1] = m

    else:
        m = stair(memo_1, n-1) + stair(memo_1, n-2) + stair(memo_1, n-3)

    memo_1[n-1] = m
    return m


n = 10

memo_1 = np.zeros(n)
stair(memo_1, n)
print(memo_1)


# case (2)
global memo_2


def stair(n):

    if memo_2[n-1] != 0:
        m = memo_2[n-1]

    elif n == 1:
        m = 1
        memo_2[n-1] = m

    elif n == 2:
        m = 2
        memo_2[n-1] = m

    elif n == 3:
        m = 4
        memo_2[n-1] = m

    else:
        m = stair(n-1) + stair(n-2) + stair(n-3)

    memo_2[n-1] = m
    return m


n = 10

memo_2 = np.zeros(n)
stair(n)
print(memo_2)
# ----------------------------------------------------------------------------------------------------
# dynamic programming (4)

# knapsack problem using DP

global weight_set
global value_set


def chooseBest(items, maxweight):

    # base case
    if len(items) == 0 or maxweight <= 0:
        value = 0
        taken = []  # empty

    else:
        first = items[0]
        rest = items[1:]
        w = weight_set[first]

        # do not take the first item
        v1, t1 = chooseBest(rest, maxweight)

        # do take the first item
        v2, t2 = chooseBest(rest, maxweight - w)
        v2 = v2 + value_set[first]
        t2 = t2 + [first]  # list

        if v2 >= v1 and maxweight - w >= 0:

            value = v2
            taken = t2

        else:

            value = v1
            taken = t1

    return value, taken


items = range(6)  # 0 ~ 5
weight_set = [10, 9, 4, 2, 1, 20]
value_set = [175, 90, 20, 50, 10, 200]

maxweight = 20

chooseBest(items, maxweight)
# ----------------------------------------------------------------------------------------------------
# reference

# https://www.youtube.com/watch?v=M6OGAI_4N_w&list=PLGMtjo8jDX9CjkmQOEUSoY5QMVE-D86pK&index=3
# https://www.youtube.com/watch?v=wY4lW0t8QZg&list=PLGMtjo8jDX9CjkmQOEUSoY5QMVE-D86pK&index=4
# ====================================================================================================
