"""
수 찾기
https://www.acmicpc.net/problem/1920
"""
# 입력받기
N = int(input())
nums1 = list(map(int, input().split()))
nums1.sort()
M = int(input())
nums2 = list(map(int, input().split()))

# 이진탐색 함수
def check(n, sorted_nums):
    start = 0
    end = len(sorted_nums) - 1
    result = False
    while start <= end:
        mid = (start + end) // 2
        if n == sorted_nums[mid]:
            result = True
            break
        elif n > sorted_nums[mid]:
            start = mid + 1
        else:
            end = mid - 1
            
    return result
            
# 각 숫자에 대해 이진탐색 수행.
for n2 in nums2:
    if check(n2, nums1):
        print(1)
    else:
        print(0)