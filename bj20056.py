"""
마법사 상어와 파이어볼
https://www.acmicpc.net/problem/20056
11:26 ~ 12:12
"""

import sys

sys.stdin = open("input.txt", "r")

# 입력: 격자크기, 파이어볼 개수, 이동 명령 횟수
N, M, K = map(int, input().split())

# 입력: 격자에 파이어볼 정보 넣기 (행, 열의 좌표는 1이 아닌 0부터 시작하도록 수정)
arr = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    arr[r - 1][c - 1].append((m, s, d))

# 함수: (x,y)에서 d방향으로 s만큼 이동했을 때의 좌표 반환
dxdy = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def move(x, y, d, s):
    global N
    dx, dy = dxdy[d]
    nx, ny = x + s * dx, y + s * dy
    nx %= N
    ny %= N
    return (nx, ny)


# # debug
# for r in range(N):
#     for c in range(N):
#         print(len(arr[r][c]), end=" ")
#     print()
# print()

# 이동 명령 반복
for k in range(K):
    # # debug
    # print(f"{k + 1}번째 이동 시작!")

    # 1. 파이어볼 이동
    new_arr = [[[] for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            balls = arr[r][c]
            # (r, c)의 모든 파이어볼을 이동시키기.
            for m, s, d in balls:
                nr, nc = move(r, c, d, s)
                new_arr[nr][nc].append((m, s, d))
    arr = new_arr

    # # debug
    # for r in range(N):
    #     for c in range(N):
    #         print(arr[r][c], end=" ")
    #     print()

    # 2. 이동 후 처리.
    for r in range(N):
        for c in range(N):
            balls = arr[r][c]
            # (r, c)에 파이어볼이 여러개 있으면 4개의 파이어볼로 변형하기.
            if len(balls) > 1:
                new_balls = []
                new_m = 0
                new_s = 0
                is_odd, is_even = False, False

                for m, s, d in balls:
                    new_m += m
                    new_s += s
                    is_odd = is_odd or (d % 2 == 1)
                    is_even = is_even or (d % 2 == 0)

                new_m //= 5
                new_s //= len(balls)

                # 질량이 0이면 소멸
                if new_m == 0:
                    pass
                # 질량이 1이상이면 4개로 분열됨.
                else:
                    # 모두 홀수이거나 모두 홀수인 경우
                    if not (is_odd and is_even):
                        for new_d in [0, 2, 4, 6]:
                            new_balls.append((new_m, new_s, new_d))
                    # 그렇지 않은 경우
                    else:
                        for new_d in [1, 3, 5, 7]:
                            new_balls.append((new_m, new_s, new_d))
                # 변경한 리스트 넣기
                arr[r][c] = new_balls

    # # debug
    # for r in range(N):
    #     for c in range(N):
    #         print(len(arr[r][c]), end=" ")
    #     print()
    # for r in range(N):
    #     for c in range(N):
    #         print(arr[r][c], end=" ")
    #     print()
    # print()

# 질량 합 구하기
result = 0
for r in range(N):
    for c in range(N):
        for m, _, __ in arr[r][c]:
            result += m

print(result)
