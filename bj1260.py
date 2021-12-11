"""
* 문제
    그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
    단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 
    정점 번호는 1번부터 N번까지이다.

* 입력
    첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
    다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
    어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 
    입력으로 주어지는 간선은 양방향이다.

* 출력
    첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. 
    V부터 방문된 점을 순서대로 출력하면 된다.
"""

from collections import deque

# N, M, V 값 입력받기
n, m, v = map(int, input().split())

# 간선의 연결 정보 입력받기
graph = [[] for _ in range(n+1)]    # 0항은 쓰지 않음
for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

# 작은 숫자부터 정렬
graph = [sorted(g) for g in graph]


def dfs(graph, start, n):
    """
    Args:
        graph: 각 노드들의 연결상태 표현. 0항은 쓰지 않음
        start: DFS 탐색을 시작하는 노드의 index
        n: 노드의 총 개수
    """
    stack = [start]
    visited = [False] * (n+1)                   # 탐색 완료 여부 기록. 0항은 쓰지 않음
    visited[start] = True                       # 시작 항 탐색 완료
    print(start, end=" ")

    while stack:                                # stack이 빌 때까지 반복 탐색
        v = stack[-1]                           # 최상단 노드

        is_search_done = True                   # 최상단 노드와 연결된 노드들을 모두 탐색했는가?
        for v_connected in graph[v]:
            
            if not visited[v_connected]:
                visited[v_connected] = True     # 탐색 완료
                print(v_connected, end=" ")
                stack.append(v_connected)       # stack 최상단 노드에 올려놓기
                is_search_done = False          # 아직 다 탐색 못했음
                break
        
        if is_search_done:                      # 만약 최상단 노드에 연결된 노드를 다 살펴봤으면
            stack.pop()                         # stack에서 최상단 노드 제거


def bfs(graph, start, n):
    """
    Args:
        graph: 각 노드들의 연결상태 표현. 0항은 쓰지 않음
        start: BFS 탐색을 시작하는 노드의 index
        n: 노드의 총 개수
    """
    queue = deque([start])
    visited = [False] * (n+1)                   # 탐색 완료 여부 기록. 0항은 쓰지 않음
    visited[start] = True                       # 시작 항 탐색 완료

    while queue:                                # queue가 빌 때까지 반복 탐색
        v = queue.popleft()                     # queue에서 노드 출력하기
        print(v, end=" ")
        for v_connected in graph[v]:            # 출력한 노드에 연결된 노드들에 대해서,
            if not visited[v_connected]:        # 탐색하지 않았으면
                visited[v_connected] = True     # 탐색하기
                queue.append(v_connected)       # queue에 방금 탐색한 노드 삽입하기

dfs(graph, v, n)
print()
bfs(graph, v, n)