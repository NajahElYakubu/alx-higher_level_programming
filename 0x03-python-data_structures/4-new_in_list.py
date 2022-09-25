#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    i = len(my_list) - 1
    cpy_list = []
    if idx > i or idx < 0:
        return(my_list)
    for x in my_list:
        cpy_list.append(x)
        x += 1
    cpy_list[idx] = element
    return(cpy_list)


if __name__ == "__main__":
    new_in_list()
