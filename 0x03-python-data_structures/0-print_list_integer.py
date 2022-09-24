#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in list(my_list):
        print("{}".format(i), end="\n")


if __name__ == "__main__":
    print_list_integer()
