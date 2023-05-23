"""
평범한 배낭
https://www.acmicpc.net/problem/12865
8:22 ~ 
"""
import sys
sys.stdin = open("input.txt", "r")

# 입력
n, k = map(int, input().split())
things = []
for _ in range(n):
    w, v = map(int, input().split())
    things.append((w, v))

# DP에 배낭 최대 무게 별로 기록.
dp = dict()
max_v = 0
for w, v in things:
    ndp = dp.copy()
    
    if w <= k:
        if w in dp:
            ndp[w] = max(ndp[w], v)
        else:
            ndp[w] = v
        if v > max_v:
            max_v = v
    
        for dw, dv in dp.items():
            if w+dw <= k:
                if w+dw in dp:
                    ndp[w+dw] = max(ndp[w+dw], v+dv)
                else:
                    ndp[w+dw] = v+dv
                if v+dv > max_v:
                    max_v = v+dv

    dp = ndp

# 출력
print(max_v)
