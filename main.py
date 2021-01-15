

#2D array that can store every spot for the grid


import pygame
import math
import time
grey = (220, 220, 220)
columns = 25
rows = 25
row_array = []
grid = [0 for i in range(columns)]

openset = []
closedset = []
path = []

width = 800 / columns
height = 800 / rows
white = [255, 255, 255]
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("A Star Algorithm Visualization")
screen.fill(white)

class Cell:
    def __init__(self, x,y):
        self.f = 0
        self.g = 0
        self.h = 0

        self.i = x
        self.j = y
        self.neighbours = []
        self.previous = None
    def display(self, color, thickness):
        pygame.draw.rect(screen, color, (self.i * width, self.j * height, width, height), thickness)
        pygame.display.update()
    def build_neighbours(self, grid):
        x = self.i
        y = self.j
        #We need to account for edge cases ( literally :))
        if x < rows - 1:
            self.neighbours.append(grid[x+1][y])
        if x > 0:
            self.neighbours.append(grid[x - 1][y])
        if y < rows - 1:
            self.neighbours.append(grid[x][y + 1])
        if y > 0:
            self.neighbours.append(grid[x][y - 1])

for i in range(columns):
    grid[i] = [0 for i in range(rows)]
for i in range(columns):
    for j in range(rows):
        grid[i][j] = Cell(i,j)
start = grid[20][10]
end = grid[20][20]

for i in range(columns):
    for j in range(rows):
        grid[i][j].display((0,0,0),2)
for i in range(columns):
    for j in range(rows):
        grid[i][j].build_neighbours(grid)


openset.append(start)

for i in range(len(openset)):
    openset[i].display((0,255,0),1)
for i in range(len(closedset)):
    closedset[i].display((255,0,0),1000)



def heuristic(neighbor, end):
    d = math.sqrt((neighbor.i - end.i) ** 2 + (neighbor.j - end.j) ** 2)
    return d


def main():
    pygame.init()
    start.display((0, 0, 255), 0)
    end.display((0, 255, 0), 0)
    while len(openset) > 0:
        winner = 0
        for i in range(len(openset)):
            if (openset[i].f < openset[winner].f):
                winner = i
        current = openset[winner]

        if (current == end):
            start.display((255, 8, 127), 0)
            temp = current.f
            for i in range(round(current.f)):
                current.closed = False
                current.display((0, 0, 255), 0)
                current = current.previous
            end.display((255, 8, 127), 0)
        openset.pop(winner)
        closedset.append(current)

        neighbors = current.neighbours
        for i in range(len(neighbors)):
            neighbor = neighbors[i]

            if neighbor not in closedset:
                tenta_g = current.g + 1
                if neighbor in openset:
                    if (tenta_g > neighbor.g):
                        neighbor.g = tenta_g
                else:
                    neighbor.g = tenta_g
                    openset.append(neighbor)

            neighbor.h = heuristic(neighbor, end)
            neighbor.f = neighbor.g + neighbor.h
            if neighbor.previous == None:
                neighbor.previous = current

    for i in range(len(path)):
        path[i].display((0,0,255),1)
while True:
    pygame.init()
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        pygame.quit()
    pygame.display.update()
    main()










