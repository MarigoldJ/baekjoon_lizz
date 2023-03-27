"""
체스판 다시 칠하기
https://www.acmicpc.net/problem/1018
"""
# 입력받기
N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(input()))

# 예제 입력 1
# N, M = 8, 8
# board = [
#     list("WBWBWBWB"),
#     list("BWBWBWBW"),
#     list("WBWBWBWB"),
#     list("BWBBBWBW"),
#     list("WBWBWBWB"),
#     list("BWBWBWBW"),
#     list("WBWBWBWB"),
#     list("BWBWBWBW")
# ]

# 8x8에서 몇 개 바꿔야하는지 계산하는 함수
def check(board8x8):
    sum = 0
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0 and board8x8[i][j] == "B":
                sum += 1
            elif (i+j) % 2 == 1 and board8x8[i][j] == "W":
                sum += 1
    
    if sum >= 32:
        return 64 - sum
    else:
        return sum

# 모든 경우 계산하기
nums = []        
for i in range(N-7):
    for j in range(M-7):
        temp = [row[j:j+8] for row in board[i:i+8]]
        nums.append(check(temp))

# 가장 작은 값 출력하기
# print(nums)
print(min(nums))