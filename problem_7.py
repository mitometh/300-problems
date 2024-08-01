# Given a 2-D matrix representing an image, a location of a pixel in the screen and a color C, replace the color of the given pixel and all adjacent same colored pixels with C.

# For example, given the following matrix, and location pixel of (2, 2), and 'G' for green:
# B B W
# W W W
# W W W
# B B B

# Becomes
# B B G
# G G G
# G G G
# B B B

def solve(grid, pixel, new_value):
    if(not grid):
        return None
    
    [x, y] = pixel
    if(len(grid) < x + 1 or len(grid[x]) < y + 1):
        return grid

    given_color = grid[x][y]
    
    for r in range(len(grid[0])):
        for c in range(len(grid[r])):
            grid[r][c] = new_value if grid[r][c] == given_color else grid[r][c]
    return grid

if __name__ == '__main__':
    grid =  [["B","B","W"],
            ["W","W","W"],
            ["W","W","W"],
            ["B","B","B"]]
    print(solve(grid, [2,2], "G"))