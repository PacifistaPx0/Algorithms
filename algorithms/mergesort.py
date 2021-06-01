from timer import Timer

def mergesort(myList):
    if myList > 1:
        mid = len(myList)/2
        left = myList[:mid]
        right = myList[mid:]

