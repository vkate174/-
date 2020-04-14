  
def insertion_sort(array): 
    length = len(array) 
    for i in range(1, length):
        key = array[i]
        j = i
        while (j - 1 >= 0) and (array[j - 1] > key):
            array[j - 1], array[j] = array[j], array[j - 1]
            j = j - 1
        array[j] = key
import random
arry = [random.randint(1, 999) for i in range(100)]
print(arry)
insertion_sort(arry)
print(arry)  
