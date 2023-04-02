"""
나무 자르기
https://www.acmicpc.net/problem/2805
"""

# 입력받기
N, M = map(int, input().split())
trees = list(map(int, input().split()))

# 이진탐색
start = 0
end = max(trees)

while start <= end:
    mid = (start + end) // 2
    sum = 0
    for tree in trees:
        if tree > mid:
            sum += tree - mid
    
    if sum > M:
        start = mid + 1
    elif sum < M:
        end = mid - 1
    else:
        start = mid + 1
        break
print(start - 1)