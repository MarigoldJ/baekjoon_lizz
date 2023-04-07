"""
2048 (Easy)
https://www.acmicpc.net/problem/12100
6:33 ~ 7:45 ~ 8:02
"""
import sys
sys.stdin = open("input.txt", "r")

# 입력받기
N = int(input())
board0 = []
for _ in range(N):
    board0.append(list(map(int, input().split())))

def up():
    global N, board
    for j in range(N):
        col = [board[i][j] for i in range(N)]
        new_col = [0] * N
        
        idx = 0             # 들어올 숫자가 자리할 인덱스
        prior_num = -1      # 직전에 들어온 숫자
        # 새로운 열 만들기
        for i in range(N):
            # 들어온 숫자
            num = col[i]
            
            # 들어온 숫자가 0인 경우
            if num == 0:
                continue
            
            # 들어온 숫자가 0보다 큰 경우
            else:
                # 들어온 숫자가 합쳐지는 경우
                if num == prior_num:
                    new_col[idx-1] += col[i]
                    prior_num = -1
                # 들어온 숫자가 합쳐지지 않는 경우
                else:
                    new_col[idx] += col[i]
                    prior_num = num
                    idx += 1
        
        # 갱신하기
        for i in range(N):
            board[i][j] = new_col[i]

def down():
    global N, board
    for j in range(N):
        col = [board[i][j] for i in range(N)]
        new_col = [0] * N
        
        idx = N-1           # 들어올 숫자가 자리할 인덱스
        prior_num = -1      # 직전에 들어온 숫자
        # 새로운 열 만들기
        for i in range(N-1, -1, -1):
            # 들어온 숫자
            num = col[i]
            
            # 들어온 숫자가 0인 경우
            if num == 0:
                continue
            
            # 들어온 숫자가 0보다 큰 경우
            else:
                # 들어온 숫자가 합쳐지는 경우
                if num == prior_num:
                    new_col[idx+1] += col[i]
                    prior_num = -1
                # 들어온 숫자가 합쳐지지 않는 경우
                else:
                    new_col[idx] += col[i]
                    prior_num = num
                    idx -= 1
        
        # 갱신하기
        for i in range(N):
            board[i][j] = new_col[i]

def right():
    global N, board
    for i in range(N):
        row = [board[i][j] for j in range(N)]
        new_row = [0] * N
        
        idx = N-1           # 들어올 숫자가 자리할 인덱스
        prior_num = -1      # 직전에 들어온 숫자
        # 새로운 행 만들기
        for j in range(N-1, -1, -1):
            # 들어온 숫자
            num = row[j]
            
            # 들어온 숫자가 0인 경우
            if num == 0:
                continue
            
            # 들어온 숫자가 0보다 큰 경우
            else:
                # 들어온 숫자가 합쳐지는 경우
                if num == prior_num:
                    new_row[idx+1] += row[j]
                    prior_num = -1
                # 들어온 숫자가 합쳐지지 않는 경우
                else:
                    new_row[idx] += row[j]
                    prior_num = num
                    idx -= 1
        
        # 갱신하기
        for j in range(N):
            board[i][j] = new_row[j]

def left():
    global N, board
    for i in range(N):
        row = [board[i][j] for j in range(N)]
        new_row = [0] * N
        
        idx = 0             # 들어올 숫자가 자리할 인덱스
        prior_num = -1      # 직전에 들어온 숫자
        # 새로운 행 만들기
        for j in range(N):
            # 들어온 숫자
            num = row[j]
            
            # 들어온 숫자가 0인 경우
            if num == 0:
                continue
            
            # 들어온 숫자가 0보다 큰 경우
            else:
                # 들어온 숫자가 합쳐지는 경우
                if num == prior_num:
                    new_row[idx-1] += num
                    prior_num = -1
                # 들어온 숫자가 합쳐지지 않는 경우
                else:
                    new_row[idx] += num
                    prior_num = num
                    idx += 1
        
        # 갱신하기
        for j in range(N):
            board[i][j] = new_row[j]

# # debug: 초기
# for i in range(N):
#     for j in range(N):
#         print(f"{board0[i][j]:4d}", end=" ")
#     print()
# print()

# 완전탐색
acts = []
for t in range(4**5):
    e = (t // (4**0)) % 4
    d = (t // (4**1)) % 4
    c = (t // (4**2)) % 4
    b = (t // (4**3)) % 4
    a = (t // (4**4)) % 4
    
    acts.append((a, b, c, d, e))

result = 0
for act in acts:
    # 보드 초기화
    board = [[board0[i][j] for j in range(N)] for i in range(N)]
    
    # 5번 시행
    for action in act:
        if action == 0:
            up()
        elif action == 1:
            down()
        elif action == 2:
            left()
        elif action == 3:
            right()
        
        # # debug
        # for i in range(N):
        #     for j in range(N):
        #         print(f"{board[i][j]:4d}", end=" ")
        #     print()
        # print()
    
    # 최댓값 찾기
    max_num = 0
    for i in range(N):
        for j in range(N):
            max_num = max(board[i][j], max_num)
    
    # 갱신하기
    if max_num > result:
        result = max_num

# 출력
print(result)
