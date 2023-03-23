"""
스택
https://www.acmicpc.net/problem/10828
"""
# 시간 초과가 나지 않기 위해
# sys.stdin.readline() 사용.
import sys
N = int(input())

stack = []
size = 0
for _ in range(N):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push":
        stack.append(int(cmd[1]))
        size += 1
    elif cmd[0] == "pop":
        if size > 0:
            print(stack.pop())
            size -= 1
        else:
            print(-1)
    elif cmd[0] == "size":
        print(size)
    elif cmd[0] == "empty":
        if size > 0:
            print(0)
        else:
            print(1)
    else:   # cmd[0] == "top"
        if size > 0:
            print(stack[-1])
        else:
            print(-1)