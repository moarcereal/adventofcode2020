import os
import sys

f = open(os.path.join(sys.path[0], "input.txt"),"r")

tally = 0
t = 0
window = []

for line in f:
    v = int(line)
    window.append(v)
    if len(window) > 3:
        n = t - window.pop(0) + v
        if n > t:
            tally += 1
        t = n
    else:
        t = sum(window)
    
print(tally) 