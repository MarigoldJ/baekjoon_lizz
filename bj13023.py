# 입력
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# dfs
import sys
sys.setrecursionlimit(10**6)

is_ok = False
visited = [False] * N
def dfs(v, length):
    global is_ok, visited
    
    # 방문 처리
    visited[v] = True
    
    # 5연속 방문이면 종료
    if length == 4:
        # 발견 여부 체크
        is_ok = True
        # 방문 해제하기
        visited[v] = False
        return
    
    # 5연속 미만이면 추가 방문시도.
    for nv in graph[v]:
        if not visited[nv]:
            # 방문하기
            dfs(nv, length+1)
            # 방문 해제하기
            visited[nv] = False
    
    # 방문 해제하기
    visited[v] = False
    

# 0 ~ N-1까지 dfs 진행.
for i in range(N):
    dfs(i, 0)
    if is_ok:
        break

# 출력
if is_ok:
    print(1)
else:
    print(0)

