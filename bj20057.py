"""
마법사 상어와 토네이도
https://www.acmicpc.net/problem/20057
12:15 ~ 12:56
"""

import sys

sys.stdin = open("input.txt", "r")

# 입력: 격자 크기
N = int(input())

# 입력: 모래 격자
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

# 변수: dr, dc. 좌하우상 순서로.
dr = (0, 1, 0, -1)
dc = (-1, 0, 1, 0)


# 함수: 토네이도의 d 리스트 얻기 (d는 좌=0, 하=1, 우=2, 상=3 이다.)
def get_hurricane_dxdy():
    global N
    d_list = []
    d = 0

    # 몇번 반복해서 이동하는지 리스트 만들기
    # N=3, 11222
    # N=5, 112233444
    # N=7, 1122334455666
    dxdy_nums = []
    for i in range(1, N):
        dxdy_nums.extend([i, i])
    dxdy_nums.append(N - 1)

    # dxdy 리스트 만들기
    for nums in dxdy_nums:
        d_list.extend([d for _ in range(nums)])
        d = (d + 1) % 4

    return d_list


# 함수: (r, c)에 d방향으로 토네이도가 이동했을 때 모래 y가 퍼지고 난 후 모래 정보 (sr, sc, s) 리스트
def get_after_wind(r, c, y, d):
    sand_list = []

    # 토네이도 이동 방향의 좌우 방향
    d_left = (d + 1) % 4
    d_right = (d - 1) % 4
    d_back = (d + 2) % 4

    # 모래 양 계산하기
    s_1 = (y * 1) // 100
    s_2 = (y * 2) // 100
    s_5 = (y * 5) // 100
    s_7 = (y * 7) // 100
    s_10 = (y * 10) // 100
    s_alpha = y - 2 * (s_1 + s_2 + s_7 + s_10) - s_5

    # 1% 모래 좌표 찾아서 추가하기
    r1, c1 = r + dr[d_back] + dr[d_left], c + dc[d_back] + dc[d_left]
    r2, c2 = r + dr[d_back] + dr[d_right], c + dc[d_back] + dc[d_right]
    sand_list.extend([(r1, c1, s_1), (r2, c2, s_1)])

    # 2% 모래 좌표 찾아서 추가하기
    r1, c1 = r + dr[d_left] + dr[d_left], c + dc[d_left] + dc[d_left]
    r2, c2 = r + dr[d_right] + dr[d_right], c + dc[d_right] + dc[d_right]
    sand_list.extend([(r1, c1, s_2), (r2, c2, s_2)])

    # 5% 모래 좌표 찾아서 추가하기
    r1, c1 = r + dr[d] + dr[d], c + dc[d] + dc[d]
    sand_list.extend([(r1, c1, s_5)])

    # 7% 모래 좌표 찾아서 추가하기
    r1, c1 = r + dr[d_left], c + dc[d_left]
    r2, c2 = r + dr[d_right], c + dc[d_right]
    sand_list.extend([(r1, c1, s_7), (r2, c2, s_7)])

    # 10% 모래 좌표 찾아서 추가하기
    r1, c1 = r + dr[d] + dr[d_left], c + dc[d] + dc[d_left]
    r2, c2 = r + dr[d] + dr[d_right], c + dc[d] + dc[d_right]
    sand_list.extend([(r1, c1, s_10), (r2, c2, s_10)])

    # alpha 모래 좌표 찾아서 추가하기
    r1, c1 = r + dr[d], c + dc[d]
    sand_list.extend([(r1, c1, s_alpha)])

    return sand_list


# 토네이도 이동 반복
tr, tc = N // 2, N // 2  # 현재 토네이도 위치
sand_out = 0  # 바깥으로 나간 모래 총량
for d in get_hurricane_dxdy():
    # 토네이도 한칸 이동
    tr, tc = tr + dr[d], tc + dc[d]

    # 이동한 위치의 모래 흩날리기
    y = A[tr][tc]
    dA_list = get_after_wind(tr, tc, y, d)

    A[tr][tc] = 0
    for r, c, s in dA_list:
        if r < 0 or r >= N or c < 0 or c >= N:
            sand_out += s
        else:
            A[r][c] += s

# 출력
print(sand_out)
