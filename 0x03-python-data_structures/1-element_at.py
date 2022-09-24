#!/usr/bin/python3


def element_at(my_list, idx):
    i = len(my_list)
    element = my_list[idx]
    if idx < 0:
        return None
    elif idx > i:
        return None
    else:
        return (element)


if __name__ == "__main__":
    element_at()
