#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a common module"""
__author__ = 'ling'
import logging


# def foo(s):
#     return 10 / int(s)
#
#
# def bar(s):
#     return foo(s) * 2
#
#
# def main():
#     try:
#         bar('s')
#     except Exception as e:
#         logging.exception(e)
# main()
# print('END')

class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n
foo('0')
