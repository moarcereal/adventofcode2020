import os
import sys

f = open(os.path.join(sys.path[0], "input.txt"),"r")

horizontal = 0
depth = 0
aim = 0

def forward(x):
    global horizontal
    global depth
    global aim
    horizontal += x
    depth += aim*x

def down(x):
    global aim
    aim += x

def up(x):
    global aim
    aim -= x

table = {'forward' : forward, 
        'down' : down,
        'up' : up}
for line in f:
    func, x = line.split(' ')
    table[func](int(x))


print(horizontal, depth, horizontal*depth)

