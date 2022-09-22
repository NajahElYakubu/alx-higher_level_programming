#!/usr/bin/python3
import sys


def arg_print(argv):
    number = len(argv) - 1
    if number == 0:
        print("{:d} arguments.".format(number))
    elif number == 1:
        print("{:d} argument:".format(number), end="\n")
    else:
        print("{:d} arguments".format(number), end="\n")
    i = 1
    while i <= number:
        print("{:d}: {:s}".format(i, argv[i]))
        i += 1


if __name__ == '__main__':
    arg_print(sys.argv)
