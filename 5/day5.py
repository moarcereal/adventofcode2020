import os
import sys

f = open(os.path.join(sys.path[0], "input.txt"),"r").readlines()

terrain = {}

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'''({self.x},{self.y})'''

    def isVertical(self, b):
        return self.x == b.x
        
    def isHorizontal(self, b):
        return self.y == b.y

    
class CoordParse(Coord):
    def __init__(self, subString):
        a, b = subString.split(",")
        self.x = int(a)
        self.y = int(b)


maxDanger = ''

for line in f:
    a, b = line.rstrip("\r\n").split(" -> ")
    start = CoordParse(a)
    stop = CoordParse(b)

    if start.isVertical(stop):
        smallerY = min(start.y, stop.y)
        largerY = max(start.y, stop.y)
        for y in range(smallerY, largerY+1):
            label = str(Coord(start.x, y))
            terrain[label] = terrain.get(label, 0) + 1
            if not maxDanger or terrain[label] > terrain[maxDanger]:
                maxDanger = label
    elif start.isHorizontal(stop):
        smallerX = min(start.x, stop.x)
        largerX = max(start.x, stop.x) 
        for x in range(smallerX, largerX+1):
            label = str(Coord(x, start.y))
            terrain[label] = terrain.get(label, 0) + 1
            if not maxDanger or terrain[label] > terrain[maxDanger]:
                maxDanger = label
    else: #isDiagonal
        if start.x < stop.x:
            x = start.x
            largerX = stop.x
            y = start.y
            if start.y < stop.y:
                yDelta = 1
            else:
                yDelta = -1
        else:
            x = stop.x
            largerX = start.x
            y = stop.y
            if stop.y < start.y:
                yDelta = 1
            else:
                yDelta = -1

        while x <= largerX:
            label = str(Coord(x, y))
            terrain[label] = terrain.get(label, 0) + 1
            if not maxDanger or terrain[label] > terrain[maxDanger]:
                maxDanger = label
            x += 1
            y += yDelta


        # print(line)
        # [print(t, terrain[t]) for t in terrain]
        # break


print(maxDanger, terrain[maxDanger])

overlapCount = 0
for k in terrain.values():
    if k > 1:
        overlapCount += 1

print(overlapCount)