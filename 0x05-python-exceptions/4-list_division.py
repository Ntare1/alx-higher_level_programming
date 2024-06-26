#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for count in range(list_length):
        try:
            x = my_list_1[count] / my_list_2[count]
        except(TypeError):
            print("wrong type")
            x = 0
        except(ZeroDivisionError):
            print("division by 0")
            x = 0
        except(IndexError):
            print("out of range")
            x = 0
        finally:
            result.append(x)
    return(result)
