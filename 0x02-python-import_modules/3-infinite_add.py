#!/usr/bin/python3
import sys


def arg_count(argv):
    n = len(argv) - 1
    if n == 0:
        print("{:d}".format(n))

    else:
        res = 0
        i = 1
        while i <= n:
            res += int(argv[i])
            i += 1
        print("{:d}".format(res))


if __name__ == '__main__':
    arg_count(sys.argv)
