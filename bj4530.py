"""
AC
https://www.acmicpc.net/problem/5430
7:21
"""

import sys
sys.stdin = open("input.txt", "r")

# 입력
T = int(input())

from collections import deque
for _ in range(T):
    cmd = list(input())
    n = int(input())
    nums = deque(eval(input()))
    is_reverse = False
    is_error = False
    
    for c in cmd:
        if c == "R":
            is_reverse = not is_reverse
        elif c == "D":
            if nums:
                if is_reverse:
                    nums.pop()
                else:
                    nums.popleft()
            else:
                is_error = True
                break
    
    # 출력
    if is_error:
        print("error")
    else:
        print("[", end="")
        if is_reverse:
            while nums:
                print(nums.pop(), end="")
                if nums: print(",", end="")
        else:
            while nums:
                print(nums.popleft(), end="")
                if nums: print(",", end="")
            
        print("]")