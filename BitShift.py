from random import randint
from math import floor


def shift_to_right(num, shiftBy):
    #get binary value of an integer num
    #store the value in an array
    binary = bin(num)
    list1 = [x for x in str(binary)[2:]]

    #create second list of zeroes
    #list lengths equal to each other
    list2 = list()
    for i in range(len(list1)):
        list2.append('0')

    #set bits in list2 = to the bits in list1 offset right by y bits
    i = 0
    while ((i + shiftBy) < len(list2)):
        list2[i + shiftBy] = list1[i]
        i += 1

    #convert list to integer value
    binary = "0b"
    binary += "".join(list2)
    integer = int(binary, 2)

    return integer
