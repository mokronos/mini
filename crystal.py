# crystal ball problem
# Given two crystal balls that will break if dropped from high enough distance,
# determine the exact spot in which it will break in the most optimized way.

import math

def crystal(height, max, func):

    step = math.floor(func(height))

    i = 1

    while 1:
        if i>max:
            break
        i += step

    i-=step

    while 1:
        if i>max:
            return i-1
        i+=1

n = 100000000
height = n
max = n

import time

func1 = math.sqrt
func2 = math.log

t0 = time.time()
print(crystal(height, max, func1))
t1 = time.time()
print(crystal(height, max, func2))
t2 = time.time()

print(f"sqrt: {t1-t0}")
print(f"log: {t2-t1}")
