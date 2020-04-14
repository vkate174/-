from random import randint
 
 
def sel_sort(array):
    for i in range(len(array) - 1):
        m = i
        j = i + 1
        while j < len(array):
            if array[j] < array[m]:
                m = j
            j = j + 1
        array[i], array[m] = array[m], array[i]
 
 
import random
arry = [random.randint(0, 2600) for i in range(2600)]
print(arry)
sel_sort(arry)
print(arry)
