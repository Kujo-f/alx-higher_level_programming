#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    replaces an element from a list
    at a specific position

    """
    size = len(my_list)
    
    if idx >= size or idx < 0:
        return (my_list)

    my_list[idx] = element
    return(my_list)
