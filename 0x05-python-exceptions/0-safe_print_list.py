#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i in range(x):
        return print(my_list[i], end="")
try:
    safe_print_list()
except Exception as e:
    print(e)
