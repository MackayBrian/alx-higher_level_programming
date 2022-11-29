#!/usr/bin/python3
def print_last_digit(number):
    new = repr(number)
    last = new[-1]
    return int(last)
res = print_last_digit(number)
print(res)
