"""
빵집
https://www.acmicpc.net/problem/3109
"""
import sys
sys.stdin = open("input.txt", "r")

# 입력
R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(input())

# dfs
def dfs(r, c, visited):
    # 경로 가능 여부와 관계없이 오직 1번만 방문하므로, 방문처리
    visited[r][c] = True
    
    # 탈출조건: 마지막 행이면 탈출
    if c == C-1:
        return True
    
    # 다음 경로 탐색
    for dr in [-1, 0, 1]:
        nr = r+dr
        nc = c+1
        
        # 범위를 벗어나는 경우 패스
        if (nr<0 or nr>=R or nc<0 or nc>=C):
            continue
        
        # 방문 가능하면 탐색 진행.
        # 탐색했을 때, 파이프라인으로 설치가능한 경로인 경우 처리
        if (not visited[nr][nc] and board[nr][nc] == '.'):
            isAble = dfs(nr, nc, visited)
            if (isAble):
                return True
    
    return False    

# 행마다 DFS 후 파이프라인 개수 세기
count = 0
visited = [[False for _ in range(C)] for _ in range(R)]
for r in range(R):
    isAble = dfs(r, 0, visited)
    if isAble:
        count += 1

print(count)
