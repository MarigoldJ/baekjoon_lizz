"""
포도주 시식
https://www.acmicpc.net/problem/2156
6:55 ~ 7:12
"""

import sys

sys.stdin = open("input.txt", "r")

# 입력
n = int(input())
wines = [int(input()) for _ in range(n)]

if n < 3:
    print(sum(wines))

else:
    # 맨 끝에 2개 와인을 마셨는지 여부에 따라서, 그 다음 와인을 마실지 말지 결정.
    idx = 2
    dp = {0:wines[0], 1:wines[1], 2:wines[0]+wines[1]}
    while idx < n:
        # print(idx, dp)
        # dp 갱신하기
        dp[0], dp[1], dp[2] = max(dp[0], dp[1], dp[2]), dp[0]+wines[idx], dp[1]+wines[idx]
        
        # 다음 와인으로 넘어가기
        idx += 1

    # 출력
    print(max(dp[0], dp[1], dp[2]))


