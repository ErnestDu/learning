#!/bin/env python
def right_justify(str):
    space = 70 - len(str)
    print ' ' * space + str
right_justify('allen')
