"""
온풍기 안녕!
https://www.acmicpc.net/problem/23289
1:23 ~ 3:13 ~ 3:38 ~ 3:41
약 2시간 15분 소요
"""
import sys
sys.stdin = open("input.txt", "r")


# 입력. 모든 좌표는 0부터 시작하게 변경.
R, C, K = map(int, input().split())
fan = []        # (r, c, 방향정보)
target = []     # (r, c)
for i in range(R):
    row = list(map(int, input().split()))
    for j in range(C):
        if row[j] == 1:
            fan.append((i, j, 1))   # 상우하좌의 우
        elif row[j] == 2:
            fan.append((i, j, 3))   # 상우하좌의 좌
        elif row[j] == 3:
            fan.append((i, j, 0))   # 상우좌하의 상
        elif row[j] == 4:
            fan.append((i, j, 2))   # 상우좌하의 하
        elif row[j] == 5:
            target.append((i, j))

W = int(input())
wall = {}               # 딕셔너리. {(x, y): [True, False]}
for i in range(R):
    for j in range(C):
        wall[(i,j)] = [False, False]
for _ in range(W):
    x, y, t = map(int, input().split())
    wall[(x-1, y-1)][t] = True

# 환경 구현
room = [[0]*C for _ in range(R)]        # RxC Array에 방의 온도 구현
move = ((-1,0), (0,1), (1,0), (0,-1))   # 상우하좌

# 함수: 벽이 있는지 혹은 바깥인지 확인
def is_wall(x, y, m):
    global wall
    # 방향은 0, 1, 2, 3순으로 상우하좌 
    # (x, y)에서 k방향에 벽 혹은 바깥인지 확인
    if m == 0 and 0<=x-1<R and 0<=y<C:
        return wall[(x, y)][0]
    elif m == 1 and 0<=x<R and 0<=y+1<C:
        return wall[(x, y)][1]
    elif m == 2 and 0<=x+1<R and 0<=y<C:
        return wall[(x+1, y)][0]
    elif m == 3 and 0<=x<R and 0<=y-1<C:
        return wall[(x, y-1)][1]
    else:
        return True

# 작업 반복
choc = 0
while choc<=100:
    # 1. 온풍기에서 바람이 나옴 ---------------------------
    for x, y, m in fan:
        dx, dy = move[m]
        m1 = (m-1)%4
        m2 = (m+1)%4
        dx1, dy1 = move[m1]
        dx2, dy2 = move[m2]
        
        # 첫 바람
        if not is_wall(x, y, m):
            room[x+dx][y+dy] += 5
        
        # 두번째 바람~마지막까지.
        wind = [(x+dx, y+dy)]
        for temp in range(4, 0, -1):
            # temp 온도만큼의 바람이 불 목록 만들기
            next_wind = []
            for w_x, w_y in wind:
                if not is_wall(w_x, w_y, m):
                    if (w_x+dx, w_y+dy) not in next_wind:
                        next_wind.append((w_x+dx, w_y+dy))
                        
                if not is_wall(w_x, w_y, m1):
                    if (w_x+dx+dx1, w_y+dy+dy1) not in next_wind and not is_wall(w_x+dx1, w_y+dy1, m):
                        next_wind.append((w_x+dx+dx1, w_y+dy+dy1))
                        
                if not is_wall(w_x, w_y, m2):
                    if (w_x+dx+dx2, w_y+dy+dy2) not in next_wind and not is_wall(w_x+dx2, w_y+dy2, m):
                        next_wind.append((w_x+dx+dx2, w_y+dy+dy2))
            
            # 바람 불기
            for nx, ny in next_wind:
                room[nx][ny] += temp
            
            # for i in range(R):
            #     for j in range(C):
            #         print(room[i][j], end=" ")
            #     print()
            # print()
            
            # 다음 바람
            wind = next_wind
    
    # print(f"{choc}개 먹은 상황에서 바람불면?")
    # for i in range(R):
    #     for j in range(C):
    #         print(room[i][j], end=" ")
    #     print()
    # print()
    
    # 2. 온도가 조절됨 -------------------------------------
    
    # 얼마나 조절되는지 구하기
    droom = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            # 온도가 조절되는 인접 칸들 리스트 만들기
            near = []
            for m in range(4):
                if not is_wall(i, j, m):
                    di, dj = move[m]
                    if room[i][j] > room[i+di][j+dj]:
                        near.append(move[m])
            # 온도 조절양 기록하기
            for di, dj in near:
                d_temp = (room[i][j] - room[i+di][j+dj])//4
                droom[i][j] -= d_temp
                droom[i+di][j+dj] += d_temp

    # 조절하기
    for i in range(R):
        for j in range(C):
            room[i][j] += droom[i][j]
            
    # print(f"{choc}개 먹은 상황에서 온도 조절하면?")
    # for i in range(R):
    #     for j in range(C):
    #         print(room[i][j], end=" ")
    #     print()
    # print()
    
    # 3. 바깥쪽 온도 감소 -----------------------------------
    for r in range(R):
        room[r][0] = max(0, room[r][0]-1)
        room[r][C-1] = max(0, room[r][C-1]-1)
    for c in range(1, C-1):
        room[0][c] = max(0, room[0][c]-1)
        room[R-1][c] = max(0, room[R-1][c]-1)

    # print(f"{choc}개 먹은 상황에서 바깥쪽 온도 감소하면?")
    # for i in range(R):
    #     for j in range(C):
    #         print(room[i][j], end=" ")
    #     print()
    # print()
    
    # 4. 초콜릿 먹기 ----------------------------------------
    choc += 1
    
    # 5. 조사하는 모든 칸 검사 ------------------------------
    
    # 검사하기
    is_ok = True
    for x, y in target:
        if room[x][y] < K:
            is_ok = False
            break
    
    # 모두 조건 충족하면 테스트 중단
    if is_ok:
        break


# 출력
# for i in range(R):
#     for j in range(C):
#         print(room[i][j], end=" ")
#     print()

print(choc)
