#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 
@Author:ling 
@Date: 2017/11/13 
"""


# def is_odd(n):
#     return n % 2 == 1
# list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
#
#
# def not_empty(s):
#     return s and s.strip()
# list(filter(not_empty, ['A', '', 'B', None, 'C', ' ']))


def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break
print(_not_divisible(5))
