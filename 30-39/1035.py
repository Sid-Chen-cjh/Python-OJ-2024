from random import *

a = int(input())
b = int(input())
t = 0

seed(b)
for i in range(a):
    if pow(random()**2 + random()**2, 0.5) <= 1:
        t += 1
print("{:.6f}".format(4*t/a))





"""
from random import *

a = int(input())
b = int(input())
t = 0

seed(b)
for i in range(a):
    if pow(random()-0.5,2) + pow(random()-0.5,2) <= 0.25:
        t += 1
print("{:.6f}".format(4*t/a))
"""