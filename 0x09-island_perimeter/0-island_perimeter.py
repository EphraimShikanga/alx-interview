#!/usr/bin/python3
'''Island perimeter module'''


def island_perimeter(grid):
    '''Calculates the perimeter of an island'''
    rows = len(grid)
    columns = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == 1:
                if r == 0 or grid[r - 1][c] == 0:
                    perimeter += 1
                if r == rows - 1 or grid[r + 1][c] == 0:
                    perimeter += 1
                if c == 0 or grid[r][c - 1] == 0:
                    perimeter += 1
                if c == columns - 1 or grid[r][c + 1] == 0:
                    perimeter += 1

    return perimeter
