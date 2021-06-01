from timer import Timer

def mergesort(array):
    if len(array) > 1:
        #dividing the list into two parts and assaigning left and right hand side of the list into separate variables
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]

        #recursively sorting both lists
        mergesort(left)
        mergesort(right)

        #declaring variables to be used for iteration,  i and j are used to iterate over the new sub lists while k is used for the original array

        i = 0
        j = 0
        k = 0

        #while loop compares the smallest element in both sublists and appends it to the original array
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i = i+1
                
            else:
                array[k] = right[j]
                j = j+1
                
            k = k+1

        #One of the while loops will execute and the remaining sorted elements in left or right sublist will be appended to the original array
        while i < len(left):
            array[k] = left[i]
            i = i+1
            k = k+1
        while j < len(right):
            array[k] = right[j]
            j = j+1
            k = k+1

array = input("input your list: ")
array = list(array.split())

t = Timer()
t.start()
mergesort(array)
print("sorted array: " + str(array))
t.stop()




