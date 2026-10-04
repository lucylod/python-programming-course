import matplotlib.pyplot as plt
from math import sqrt

n=10
maze = [[0]*n for _ in range(n)]
walls = [(2,8),(0,9),(1,7),(2,2),(2,3),(2,4),(2,5),
         (2,6),(2,7),(3,2),(4,2),(7,2),(6,2),(8,2),
         (4,7),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),
         (5,7),(6,2),(6,6),(7,6),(3,5),(7,4),(8,4),
         (9,4),(8,6),(8,7),(8,8),(5,0)]
for (x,y) in walls:
    maze[x][y]=1
 
start = (8,1)
goal = (3,4)

# Visualize maze in console as text
def print_maze(maze, start=None, goal=None, path=None, dist=None):
    n = len(maze)
    print(*"#"*(n+2), sep="")
    for y in range(n-1,-1,-1):
        row = "#"
        for x in range(n):
            if maze[x][y] == 1:
                row += "#"  # wall
            elif start and (x, y) == start:
                row += "S"  # start
            elif goal and (x, y) == goal:
                row += "G"  # goal
            elif path and (x, y) in path:
                row += "*"  # path
            elif dist and dist[x][y] < float('inf'):
                row += str(int(dist[x][y])) if dist[x][y] < 10 else "+"
            else:
                row += " "
        row += "#"
        print(row)
    print(*"#"*(n+2), sep="")


dist = [[float('inf')]*n for _ in range(n)]
dist[goal[0]][goal[1]] = 0

def update(dist,maze,pos):
    x,y = pos
    n = len(maze)
    for (xp,yp) in [(x-1,y),(x,y-1),(x+1,y),(x,y+1),(x-1,y+1),(x+1,y+1),(x-1,y-1),(x+1,y-1)]:    
        tmp = dist[x][y]+1
        if 0 <= xp < n and 0 <= yp < n  and maze[xp][yp] == 0 and tmp < dist[xp][yp]:
            dist[xp][yp]=tmp
            update(dist,maze,(xp,yp))


#wir erweitern find_shortest_path()

def find_shortest_path(dist, path):
    x, y = path[-1]
    if dist[x][y] != 0:
        # nur 4-Nachbarn: links, unten, rechts, oben
        for (xp, yp) in [(x-1, y), (x, y-1), (x+1, y), (x, y+1),(x-1,y+1),(x+1,y+1),(x-1,y-1),(x+1,y-1)]:
            if 0 <= xp < n and 0 <= yp < n:
                if dist[xp][yp] < dist[x][y]:
                    path.append((xp, yp))
                    return find_shortest_path(dist, path)
    return path




print_maze(maze, start=start, goal=goal)
