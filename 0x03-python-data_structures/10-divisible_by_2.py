#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    divi = []
    for x in my_list:
        if (x % 2 == 0):
            divi.append(True)
        else:
            divi.append(False)
    return(divi)

