import os
import sys

f = open(os.path.join(sys.path[0], "input.txt"),"r").readlines()

school = {}
for d in range(-1,9):
    school[d] = 0

for line in f:
    fish = line.rstrip("\r\n").split(",")
    for d in fish:
        school[int(d)] += 1

# print(school)

for i in range(256):
    for d in range(-1,8):
        school[d] = school[d+1]

    school[6] += school[-1]
    school[8] = school[-1]
    # print(i, school)

tally = sum([school[x] for x in range(9)])
print(tally)