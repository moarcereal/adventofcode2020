import os
import sys

f = open(os.path.join(sys.path[0], "input.txt"),"r")

width = len("100111111100")

class Node:
    def __init__(self):
        self.zeros = []
        self.ones = []

    def __str__(self):
        return str(self.zeros) + str(self.ones) 

tree = f

oxygen = ''
for w in range(width):
    if len(tree) <= 1:
        oxygen += tree[0][w:]
        break
    
    ones = []
    zeros = []
    for line in tree:
        if line[w] == '0':
            zeros.append(line)
        else:
            ones.append(line)

    print(len(zeros), len(ones))
    if len(zeros) <= len(ones):
        oxygen += '0'
        tree = zeros
    else:
        oxygen += '1'
        tree = ones

print(oxygen,int(oxygen,2))
# for i, c in enumerate(line.rstrip('\r\n')):
#             bits[i][c] += 1
# gamma = ''
# elipson = ''
# for z in bits:
#     if z['0'] > z['1']:
#         gamma += '0'
#         elipson += '1'
#     else:
#         gamma += '1'
#         elipson += '0'

# gammaRate = int(gamma, 2)
# epsilonRate = int(elipson, 2)

# print(epsilonRate * gammaRate, epsilonRate, gammaRate)

