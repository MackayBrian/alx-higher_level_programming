#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
=======
def safe_print_list(my_list=[], x=0):
    for i in range(x):
        print(my_list[i], end="")
try:
    safe_print_list()
except Exception as e:
    print(e)
>>>>>>> 934959637ebae039dec7777f044c032cf7a971bd
