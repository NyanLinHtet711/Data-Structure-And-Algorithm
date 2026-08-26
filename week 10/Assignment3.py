n = int(input())
adj_list = [list(map(int,input().split())) for _ in range(n)]

adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
for adj in adj_list:
    for i in range(adj[1]):
        adj_matrix[adj[0]-1][adj[i+2]-1] = 1

for row in adj_matrix:
    print(*row)
