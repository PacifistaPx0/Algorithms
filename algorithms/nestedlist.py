#Recursive function that sums nested list

def sumtree(array):
    total = 0
    for x in array: 
        if not isinstance(x, list):
            total += x
        else:
            total += sumtree(x)
    return total

L = [1, [2, [3, 4], 5], 6, [7, 8]] # Arbitrary nesting
print(sumtree(L))
