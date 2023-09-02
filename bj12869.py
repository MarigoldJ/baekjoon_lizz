"""
뮤탈리스크
https://www.acmicpc.net/problem/12869
"""
import sys
sys.stdin = open("input.txt", "r")

# 입력
N = int(input())
scv = list(map(int, input().split()))

# scv를 길이가 3인 list로 설정
while (len(scv) < 3):   
    scv.append(0)

# BFS by DP
from collections import deque
q = deque()
dp = dict()

# BFS 첫 방문
scv.sort()
dp[tuple(scv)] = 0
q.append((scv, 0))

# 큐가 빌때까지 진행
from itertools import permutations
while len(q) > 0:
    hp_list, attack_count = q.popleft()
    
    # 공격 이후 탐색
    for order in permutations(range(3), 3):
        new_hp_list = [0, 0, 0]
        for i, idx in enumerate(order):
            new_hp_list[idx] = max(0, hp_list[idx] - 3**(2-i))
        new_hp_list.sort()
        
        # 존재하지 않으면 dp와 큐에 추가
        if (tuple(new_hp_list) not in dp):
            dp[tuple(new_hp_list)] = attack_count + 1
            q.append((new_hp_list, attack_count+1))
        # 존재하지만 더 적은 공격 횟수면 dp 갱신하고 큐에 추가
        elif (attack_count + 1 < dp[tuple(new_hp_list)]):
            dp[tuple(new_hp_list)] = attack_count + 1
            q.append((new_hp_list, attack_count+1))

# 출력
print(dp[(0, 0, 0)])