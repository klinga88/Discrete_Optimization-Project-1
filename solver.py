#!/usr/bin/python

from random import randint
def solve_it():
    # return a positive integer, as a string
    i = randint(0,9)
    return i

if __name__ == '__main__':
    print('This script submits the integer: {}'.format(solve_it()))
