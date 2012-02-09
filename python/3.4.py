#!/bin/env python
def do_twice(f, spam):
    f(spam)
    f(spam)

def print_spam(str):
    print str

do_twice(print_spam, 'print something')
