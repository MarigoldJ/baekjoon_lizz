"""
치킨 배달
https://www.acmicpc.net/problem/15686
6:37 ~ 7:10
"""
import sys
sys.stdin = open("input.txt", "r")

# 입력
n, m = map(int, input().split())
home_list = []
chick_list = []
for i in range(n):
    temp = input().split()
    for j, num in enumerate(temp):
        if num == "1":
            home_list.append((i, j))
        if num == "2":
            chick_list.append((i, j))

# 각 집의 치킨거리 리스트 구하기
dists_list = []
for hr, hc in home_list:
    temp = []
    for cr, cc in chick_list:
        temp.append(abs(hr-cr)+abs(hc-cc))
    dists_list.append(temp)

# M개만을 골라서 치킨거리 합 구하기
from itertools import combinations
min_summ = 10**9
for idx_list in combinations(range(len(chick_list)), m):
    summ = 0
    for dists in dists_list:
        dist = 10**9
        for idx in idx_list:
            dist = min(dist, dists[idx])
        summ += dist
    
    min_summ = min(min_summ, summ)
        
        
# 출력
print(min_summ)
