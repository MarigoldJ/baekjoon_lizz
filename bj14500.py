"""
테트로미노
https://www.acmicpc.net/problem/14500
"""
# 입력받기
N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

move = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 갈래가 없는 테트로미노
def search1(tetro, left):
    if left:
        result_max = 0
        x, y = tetro[-1]
        for dx, dy in move:
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<M and (nx, ny) not in tetro:
                new_tetro = tetro[:] + [(nx, ny)]
                result_max = max(result_max, search1(new_tetro, left-1))
        return result_max
    else:
        score = 0
        for x, y in tetro:
            score += board[x][y]
        return score
    
# 갈래가 있는 테트로미노 (ㅏ자 모양)
from itertools import combinations
def search2(x, y):
    result_max = 0
    for three_move in combinations(move, 3):
        result = board[x][y]
        for dx, dy in three_move:
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<M:
                result += board[nx][ny]
        result_max = max(result_max, result)
    return result_max
        

result = 0
for i in range(N):
    for j in range(M):
        # 시작점을 기준으로, 완전탐색 진행
        tetro = [(i, j)]
        x, y = i, j
        result = max(result, search1(tetro, 3))
        result = max(result, search2(x, y))
print(result)