import timer
from timer import Timer
import random

array = [random.randrange(1000000) for k in range(1000000)]

t = Timer()
t.start()
sorted(array)
print("sorted array: " + str(array))
t.stop()