#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    i = len(my_list) - 1
    my_list[idx] = element
    if idx < 0 or idx > i:
        return(my_list)
    else:
        return(my_list)


if __name__ == "__main__":
    replace_in_list()
