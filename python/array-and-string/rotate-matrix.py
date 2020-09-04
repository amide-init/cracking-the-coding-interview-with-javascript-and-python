def rotateMatrix(grid):
    m = len(grid)
    n = len(grid[0])
    x =[[0]*m]*n
    for a in range(len(x)):
        for i in range(len(x[a])):
            x[a][i] = grid[m-1-i][n-1-a]
    return x

        



grid = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]]

print(rotateMatrix(grid))