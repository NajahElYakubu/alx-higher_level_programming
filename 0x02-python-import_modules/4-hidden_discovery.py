#!/usr/bin/python3
import hidden_4


def print_name():
    name = dir(hidden_4)
    for i in name:
        if i != '__':
            print("{:s}".format(i))


if __name__ == "__main__":
    print_name()