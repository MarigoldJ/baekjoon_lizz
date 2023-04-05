"""
연구소 3
https://www.acmicpc.net/problem/17142

arr: 0, 1, 2로 격자 구현 (이중리스트)
virus: 비활성화된 바이러스들.  = [(x1, y1), ...]

acts: 활성화 시킬 바이러스들을 담은 리스트. 
    ex) virus = [(x1, y1), (x2, y2)]면 M=1일떄 acts = [[(x1, y1)], [(x2, y2)]]
arr0: arr를 복사해옴. 예제 설명처럼 벽은 -, 활성화된 바이러스는 0 등으로 표현.

"""
# import sys
# sys.stdin = open("input.txt", "r")

# 입력
N, M = map(int, input().split())
arr = []
virus = []      # 비활성화된 바이러스들 (x, y)
for i in range(N):
    row = list(map(int, input().split()))
    for j, r in enumerate(row):
        if r == 2:
            virus.append((i, j))
    arr.append(row)

# 환경
move = ((-1,0), (0,1), (1,0), (0,-1))   # 상우하좌. 시계방향

# 함수: Combination by DFS
def comb(a, n, r):
    # a에서 nCr 모두 반환 by DFS
    if r == 1:
        return [[i] for i in a]
    elif r == n:
        return [a]
    else:
        result = comb(a[1:], n-1, r)
        c = comb(a[1:], n-1, r-1)
        l = len(c)
        b = [[a[0]] for _ in range(l)]
        for i in range(l):
            b[i] += c[i]
        result += b
        return result

# 완전탐색: 바이러스를 활성화하는 모든 방법 시도
from collections import deque

acts = comb(virus, len(virus), M)       # virus중 M개 뽑기
t_min = 10**6                           # 최소 시간

for act in acts:
    
    # 연구소
    arr0 = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            target = arr[i][j]
            if target == 0:
                arr0[i][j] = '+'    # 빈칸
            elif target == 1:
                arr0[i][j] = '-'    # 벽
            elif target == 2:
                arr0[i][j] = '*'    # 비활성화
    
    # 첫 활성화. 
    for x, y in act:
        arr0[x][y] = 0              # 활성화
        
    # BFS로 바이러스 전파 구현
    q = deque(act)      # BFS를 위한 큐
    t = 0               # 최대 시간
    while q:
        # print(q)
        x, y = q.popleft()
        for dx, dy in move:
            nx, ny = x+dx, y+dy
            # 연구소 밖이면 건너뛰기
            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            # 벽이면 건너뛰기
            if arr0[nx][ny] == '-':
                continue
            
            a = arr0[x][y]
            na = arr0[nx][ny]
            
            # 빈칸이거나 비활성화 바이러스면 전파
            if na == '*' or na == '+':
                arr0[nx][ny] = a + 1
                q.append((nx, ny))
            # 바이러스 전파된 곳이면 전파
            else:
                if a+1 < na:
                    arr0[nx][ny] = a + 1
                    q.append((nx, ny))
    
    # 전파 시간 계산
    t = 0
    is_valid = True
    for i in range(N):
        for j in range(N):
            target = arr0[i][j]
            if target == '-' or target == '*':
                continue
            elif target == '+':
                is_valid = False
            else:
                if arr[i][j] < 2:
                    t = max(t, target)
                
    
    if is_valid and t<t_min:
        # print(act)
        # for i in range(N):
        #     for j in range(N):
        #         print(arr0[i][j], end=" ")
        #     print()
        t_min = t
                

# 출력
if t_min == 10**6:
    print(-1)
else:
    print(t_min)
