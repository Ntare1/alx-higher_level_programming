#!/usr/bin/python3
def weight_average(my_list=[]):
    num = 0
    den = 0
    if my_list and len(my_list):
        return (0)
    else:
        for tup in my_list:
            num += (tup[0] * tup[1])
            den += (tup[1])
        return (num/den)
