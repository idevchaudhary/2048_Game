import random
def start_game():
    mat=[]
    for i in range(4):
        mat.append([0]*4)
    return mat

def add_new_2(mat):
    r=random.randint(0,3)
    c=random.randint(0,3)
    while mat[r][c]!=0:
        r=random.randint(0,3)
        c=random.randint(0,3)
    mat[r][c]=2
    
def reverse(mat):
    new_mat=[]
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][4-j-1])
    return new_mat

def transpose(mat):
    new_mat=[]
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
            
            
    return new_mat
def move_left(grid):
    new_grid=compress(grid)
    new_grid=merge(new_grid)
    new_grid=compress(new_grid)
    final=new_grid
    return final
def move_right(grid):
    reverse_grid=reverse(grid)
    new_grid=compress(grid)
    new_grid=merge(new_grid)
    new_grid=compress(new_grid)
    
    final=reverse(new_grid)
    return final
def move_up(grid):
    t_grid=transpose(grid)
    new_grid=compress(t_grid)
    new_grid=merge(new_grid)
    new_grid=compress(new_grid)
    final=transpose(new_grid)
    return final

    
def move_down(grid):
    t_grid=transpose(grid)
    r_grid=reverse(t_grid)
    new_grid=compress(r_grid)
    new_grid=merge(new_grid)
    new_grid=compress(new_grid)
    new_grid=reverse(new_grid)
    final=transpose(new_grid)
    return final
    
    
def get_current_state(mat):
    #if 2048 is there in the mat it mean victory 
    for i in range(4):
        for j in range(4):
            if (mat[i][j]==2048):
                return "WON"
            
    # checking for 0 in mat 
    for i in range(4):
        for j in range(4):
            if (mat[i][j]==0):
                return "GAME NOT OVER"
    #checking for consecutive elments in the mat in order to make move except last row and last col
    for i in range(3):
        for j in range(3):
            if (mat[i][j]==mat[i+1][j] or mat[i][j]==mat[i][j+1]):
                return "GAME NOT OVER"
    
    #checking for last row
    for j in range(3):
        if mat[3][j]==mat[3][j+1]:
            return "GAME NOT OVER"
    #for checking in last col
    for i in range(3):
        if mat[i][3]==mat[i+1][3]:
            return "GAME NOT OVER"
    #if nothing to return it means lost return :"Lost"
    return "LOST"

def compress(mat):
    new_mat=[]
    for i in range(4):
        new_mat.append([0]*4)
    for i in range(4):
        pos=0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos]=mat[i][j]
                pos+=1
    return new_mat
def merge(mat):
    for i in range(4):
        for j in range(3):
            if mat[i][j]==mat[i][j+1] and mat[i][j]!=0:
                mat[i][j]=mat[i][j]*2
                mat[i][j+1]=0
    return mat 