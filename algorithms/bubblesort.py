import timer, random
from timer import Timer

def bubblesort(array):
    n = len(array) - 1
    while True:
        swapped = False
        for i in range(0,n):
            
            if int(array[i]) > int(array[i+1]):
                #pythonian way of swapping elements
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True

        #the reducing value of n or the array ensures we dont have to worry about the sorted right side when next we loop
        n -= 1
        if not swapped:
            break

    return array
                
            

array = [random.randrange(1000) for k in range(1000)]

#input("input your list: ")
#array = list(array.split())

t = Timer()
t.start()
bubblesort(array)
print("sorted array: " + str(array))
t.stop()