
# relative distance of above, below, left, and right cells
adj = [(0,-1),(0,1),(-1,0),(1,0)]

def valid(r,c,n):
    # return True if coordinate (r,c) is not outside the matrix
    # and is not a part of a wall
    
    global steps
    
    if r >= 0 and r < n and c >= 0 and c < n:
        if steps[r][c] == 0:
            return True
    return False

'''
maze:  the input maze
ends:  the list of source and destination coordinates
steps: matrix that stores the minimum number of steps from
       the source coordinate to each visited maze cell.
       = -1 if the cell is part of a wall.
'''

n = int(input())
# Read input maze
maze = []
ends = []
for r in range(n):
    maze.append(input().split())

# Set up the steps matrix
steps = [[0]*n for _ in range(n)]
for r in range(n):
    for c in range(n):
        if maze[r][c] == "1":
            steps[r][c] = -1



ends.append((0,0))
ends.append((n-1,n-1))




Queue = []
Queue.append((ends[0],0))

while Queue != []:
    # Fill in the code below
    u = Queue[0]
    del Queue[0]

    if u[0] == ends[1]:
        print(u[1])
        break

    for d in adj:
        r = u[0][0] + d[0]
        c = u[0][1] + d[1]
        if valid(r,c,n):
            v = ((r,c,n),u[1] + 1)
            steps[r][c] = u[1] + 1
            Queue.append(v)


    


if steps[n-1][n-1] == 0:
    print("no")
else:
    print("yes")
                


        

