"""
스타트와 링크
https://www.acmicpc.net/problem/14889
"""

# 입력
N = int(input())
S = []
for _ in range(N):
    S.append(list(map(int, input().split())))

# 완전탐색
from itertools import combinations as comb
from itertools import permutations as perm
diff = 10**7
for team1 in comb(range(N), N//2):
    team2 = list(set(range(N)) - set(team1))
    stats1, stats2 = 0, 0
    for p1, p2 in perm(team1, 2):
        stats1 += S[p1][p2]
    for p1, p2 in perm(team2, 2):
        stats2 += S[p1][p2]
    
    diff = min(diff, abs(stats1 - stats2))

# 출력
print(diff)