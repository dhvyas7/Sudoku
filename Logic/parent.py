from random import *     
def transpose_grid(grid):
    block_c = []
    i=0
    for j in range (3):
        bl_tmp = [[grid[0][i][j*3+0],grid[0][i+1][j*3+0],grid[0][i+2][j*3+0],
        grid[1][i][j*3+0],grid[1][i+1][j*3+0],grid[1][i+2][j*3+0],
        grid[2][i][j*3+0],grid[2][i+1][j*3+0],grid[2][i+2][j*3+0]],
        [grid[0][i][j*3+1],grid[0][i+1][j*3+1],grid[0][i+2][j*3+1],
        grid[1][i][j*3+1],grid[1][i+1][j*3+1],grid[1][i+2][j*3+1],
        grid[2][i][j*3+1],grid[2][i+1][j*3+1],grid[2][i+2][j*3+1]],
        [grid[0][i][j*3+2],grid[0][i+1][j*3+2],grid[0][i+2][j*3+2],
        grid[1][i][j*3+2],grid[1][i+1][j*3+2],grid[1][i+2][j*3+2],
        grid[2][i][j*3+2],grid[2][i+1][j*3+2],grid[2][i+2][j*3+2]]]
        block_c.append (bl_tmp)
    return block_c
    

def randomize_grid(bl_r):
    bl_r = sample(bl_r,3)
    bl_r[0] = sample(bl_r[0],3)
    bl_r[1] = sample(bl_r[1],3)
    bl_r[2] = sample(bl_r[2],3)
    return bl_r

def remove_nums(grid):
    num_remove = 25
    while num_remove > 0:
        r = randint(0, 8)
        c = randint(0, 8)
        if grid[r][c] != 0:
            grid[r][c] = 0
            grid[8-r][8-c]=0
            num_remove -= 1
    return grid

def check(grid):
    li=[1,2,3,4,5,6,7,8,9]
    transpose=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
    box_arr=[]
    box1=[grid[0][0],grid[0][1],grid[0][2],
          grid[1][0],grid[1][1],grid[1][2],
          grid[2][0],grid[2][1],grid[2][2]]
    box_arr.append(box1)
    box2=[grid[0][3],grid[0][4],grid[0][5],
          grid[1][3],grid[1][4],grid[1][5],
          grid[2][3],grid[2][4],grid[2][5]]
    box_arr.append(box2)
    box3=[grid[0][6],grid[0][7],grid[0][8],
          grid[1][6],grid[1][7],grid[1][8],
          grid[2][6],grid[2][7],grid[2][8]]
    box_arr.append(box3)
    box4=[grid[3][0],grid[3][1],grid[3][2],
          grid[4][0],grid[4][1],grid[4][2],
          grid[5][0],grid[5][1],grid[5][2]]
    box_arr.append(box4)
    box5=[grid[3][3],grid[3][4],grid[3][5],
          grid[4][3],grid[4][4],grid[4][5],
          grid[5][3],grid[5][4],grid[5][5]]
    box_arr.append(box5)
    box6=[grid[3][6],grid[3][7],grid[3][8],
          grid[4][6],grid[4][7],grid[4][8],
          grid[5][6],grid[5][7],grid[5][8]]
    box_arr.append(box6)
    box7=[grid[6][0],grid[6][1],grid[6][2],
          grid[7][0],grid[7][1],grid[7][2],
          grid[8][0],grid[8][1],grid[8][2]]
    box_arr.append(box7)
    box8=[grid[6][3],grid[6][4],grid[6][5],
          grid[7][3],grid[7][4],grid[7][5],
          grid[8][3],grid[8][4],grid[8][5]]
    box_arr.append(box8)
    box9=[grid[6][6],grid[6][7],grid[6][8],
          grid[7][6],grid[7][7],grid[7][8],
          grid[8][6],grid[8][7],grid[8][8]]
    box_arr.append(box9)
    for d in range(len(grid)):
        for e in range(len(grid[d])):
            transpose[e][d]=grid[d][e]
    for i in range(len(transpose)):
        if not(sorted(transpose[i])==li and sorted(grid[i])==li and sorted(box_arr[i])==li):
            return False
    return True

def creator():
    default_grid = [[1,2,3,4,5,6,7,8,9],
                    [4,5,6,7,8,9,1,2,3],
                    [7,8,9,1,2,3,4,5,6],
                    [2,3,4,5,6,7,8,9,1],
                    [5,6,7,8,9,1,2,3,4],
                    [8,9,1,2,3,4,5,6,7],
                    [3,4,5,6,7,8,9,1,2],
                    [6,7,8,9,1,2,3,4,5],
                    [9,1,2,3,4,5,6,7,8]]
                    
    block_r = [[default_grid[0],default_grid[1],default_grid[2]],
               [default_grid[3],default_grid[4],default_grid[5]],
               [default_grid[6],default_grid[7],default_grid[8]]]

    x = 100
    while (x>0):
        block_r = randomize_grid(block_r)   
        block_r = transpose_grid(block_r)
        block_r = randomize_grid(block_r)
        block_r = transpose_grid(block_r)
        x=x-1
    final_grid=[block_r[0][0],block_r[0][1],block_r[0][2],
                block_r[1][0],block_r[1][1],block_r[1][2],
                block_r[2][0],block_r[2][1],block_r[2][2]]
      
    #print (final_grid)
    return remove_nums(final_grid)

