import os
import sys

f = open(os.path.join(sys.path[0], "input.txt"),"r").readlines()


class Board:
    def __init__(self, strRows):
        self.bingo = False
        self.layout = [[0 for c in range(5)] for r in range(5)]
        self.matches = {}
        self.row_matches = [0 for r in range(5)]
        self.col_matches = [0 for c in range(5)]
        for row, r in enumerate(strRows):
            for col, v in enumerate(r.split()):
                self.layout[row][col] = int(v)
                self.matches[int(v)] = {'row' : row, 'col' : col, 'matched' : False}
                
    def __str__(self):
        return f'''{self.row_matches} {self.col_matches} {str([['X' if self.matches[c]['matched'] else c for c in r] for r in self.layout])}'''

    def numberCalled(self, num):
        if not num in self.matches or self.bingo:
            return 0
        info = self.matches[num]
        info['matched'] = True
        self.row_matches[info['row']] += 1
        self.col_matches[info['col']] += 1
        self.bingo = max(self.row_matches[info['row']], self.col_matches[info['col']]) >= 5
        return self.bingo

    def sumUnmarked(self):
        tally = 0
        for k in self.matches:
            if not self.matches[k]['matched']:
                tally += k
        return tally

numbers = [int(v) for v in f[0].split(',')]

boards = []
buffer = [[] for r in range(6)]

for num, line in enumerate(f[2:]):
    buffer[num % 6] = line.rstrip('\r\n')
    if num % 6 == 5:
        boards.append(Board(buffer))

# [print(i,b) for i,b in enumerate(boards)]


bingoCount = 0
bingo = False
for n in numbers:
    for i, b in enumerate(boards):
        bingoCount += b.numberCalled(n)
        if bingoCount == len(boards):
            print('BINGO', i+1, b.sumUnmarked(), n*b.sumUnmarked(), b)
            bingo = True
            break
    if bingo:
        break

