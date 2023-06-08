"""
N과 M (2)
https://www.acmicpc.net/problem/15650
"""

import sys
sys.stdin = open("input.txt", "r")

# 입력
n, m = map(int, input().split())

def dfs(n, m, nums):
    if len(nums) == m:
        # 출력
        for num in nums:
            print(num, end=" ")
        print()
    
    elif len(nums) == 0:
        for i in range(1, n+1):
            dfs(n, m, nums+[i])
    
    else:
        for i in range(nums[-1]+1, n+1):
            dfs(n, m, nums+[i])
        
dfs(n, m, [])
