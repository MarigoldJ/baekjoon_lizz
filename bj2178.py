"""
* 문제
    NxM크기의 배열로 표현되는 미로가 있다.
    1 0 1 1 1 1
    1 0 1 0 1 0
    1 0 1 0 1 1
    1 1 1 0 1 1
    미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 
    이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 
    한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

    위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

* 입력
    첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 
    다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 
    각각의 수들은 붙어서 입력으로 주어진다.

* 출력
    첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 
    항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.
"""

from collections import deque

# N, M 입력받기
n, m = map(int, input().split())

# 미로 입력받기
maze = [[int(v) for v in input()] for _ in range(n)]

# BFS로 미로 최단 탈출 거리 찾기
def maze_bfs(maze, n, m):

    dx = [0, 0, -1, 1]      # 상하좌우
    dy = [1, -1, 0, 0]      # 상하좌우

    queue = deque()
    queue.append((0, 0))

    while queue:
        # queue에서 살펴볼 좌표 출력하기
        x, y = queue.popleft()
        
        # 상하좌우 좌표 탐색
        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            if (0 <= new_x < n) and (0 <= new_y < m):

                # 0인 경우 무시하기
                if maze[new_x][new_y] == 0:
                    continue

                # 해당 좌표를 처음 방문하는 경우에만 최단 거리 기록
                if maze[new_x][new_y] == 1:
                    maze[new_x][new_y] += maze[x][y]
                    queue.append((new_x, new_y))
    
    return maze[n-1][m-1]

print(maze_bfs(maze, n, m))


