from timer import Timer
import timer
import random


def insertion_sort(array):
    #loop around the array, i starts from the second index in the array as we assume the first value is part of the sorted list
    for i in range(1, len(array)):
        currentValue = array[i]
        

        #we compare the values of the first item in the unsorted half with the items in the sorted half
        while i > 0 and int(array[i-1]) > int(currentValue):
            array[i] = array[i-1]
            i = i-1

        array[i] = currentValue
        
    return array

array = [random.randrange(100) for k in range(100)]
#array = input("input your list: ")
#array = list(array.split())

t = Timer()
t.start()
insertion_sort(array)
print("sorted array: " + str(array))
t.stop()
