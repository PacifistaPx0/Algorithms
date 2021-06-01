from timer import Timer 

def linearsearch(array):
    for i in range(0, len(array)):
        if int(array[i]) == int(user_number):
                return i
    return -1
            

array = input("Enter your array of numbers: ")
array = list(array.split())
user_number = input("What number would you like to search for: ")

t = Timer()
t.start()
#calling the function
result = linearsearch(array)
if result == -1:
    print("your number was not in the array")
else:
    print("your number is in index "+ str(result))
t.stop()

