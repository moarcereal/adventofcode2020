import os
import sys

f = open(os.path.join(sys.path[0], "input.txt"),"r").readlines()
# f = ["16,1,2,0,4,2,7,1,2,14"]

positions = {}

minPosition = 10**100
maxPosition = -1

for line in f:
    pos = line.rstrip("\r\n").split(",")
    print(pos)
    for d in pos:
        positions[int(d)] = positions.get(int(d), 0) + 1
        minPosition = min(minPosition, int(d))
        maxPosition = max(maxPosition, int(d))


print(positions)

print(minPosition, maxPosition)

results = [-1]*(maxPosition+1)

steps = [0]*(maxPosition+1)
for i in range(1,maxPosition+1):
    steps[i] = i + steps[i-1]


for pos in range(minPosition, maxPosition+1):
    # print(pos, results[pos])
    results[pos] = 0
    for p in range(minPosition, maxPosition+1):
        results[pos] += positions.get(p, 0)*steps[abs(pos - p)]

# print(min(results), results) 

print('best', min(results))

# for i in range(256):
#     for d in range(-1,8):
#         school[d] = school[d+1]

#     school[6] += school[-1]
#     school[8] = school[-1]
#     # print(i, school)

# tally = sum([school[x] for x in range(9)])
# print(tally)