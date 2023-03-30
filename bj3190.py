"""
뱀
https://www.acmicpc.net/problem/3190
클래스 안쓰고 구현해보기.
"""
from collections import deque

# 환경 구성하기
N = int(input())
directs = deque([(0, 1), (1, 0), (0, -1), (-1, 0)])
snake = deque([(1, 1)])

K = int(input())
apples = []
for _ in range(K):
    x, y = map(int, input().split())
    apples.append((x, y))

turns = deque([])
L = int(input())
for _ in range(L):
    X, C = input().split()
    X = int(X)
    turns.append([X, C])

# # 디버깅용 출력 코드
# def debug(N, snake, apples, turns, result):
#     print("경과 시간:", result)
#     print(list(turns))
#     for i in range(1, N+1):
#         for j in range(1, N+1):
#             if (i, j) in snake:
#                 print('▣', end=" ")
#             elif (i, j) in apples:
#                 print('a', end=" ")
#             else:
#                 print('▢', end=" ")
#         print()
#     print()
            
result = 0
while True:
    # # 디버깅 코드
    # debug(N, snake, apples, turns, result)
    
    # ------------ 뱀 이동 --------------
    # 현재 뱀 머리
    x, y = snake[0]
    
    # 다음 이동 위치
    nx, ny = x+directs[0][0], y+directs[0][1]
    
    # 사과 확인
    is_apple = (nx, ny) in apples
    
    # 사과가 있는 경우: 머리 이동 후 사과 제거
    if is_apple:
        snake.appendleft((nx, ny))
        result += 1
        apples.remove((nx, ny))
    
    # 사과가 없는 경우: 머리 이동
    else:
        snake.appendleft((nx, ny))
        result += 1
        
        # 종료 조건 확인.
        is_out = nx < 1 or nx > N or ny < 1 or ny > N
        is_duplicated = snake.count((nx, ny)) > 1
        
        # 벽 또는 자기 자신과 충돌하면 종료.
        if is_out or is_duplicated:
            break
        
        # 충돌하지 않는다면 꼬리 이동
        else:
            snake.pop()
    
    # 시간 경과 후 회전해야 하는지 확인.
    if turns:
        if turns[0][0] == result:
            _, C = turns.popleft()
            if C == "L":
                directs.rotate(1)
            elif C == "D":
                directs.rotate(-1)

print(result)
