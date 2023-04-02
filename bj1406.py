import sys
input = sys.stdin.readline

# 리스트 슬라이싱 최소화를 위해 두개 리스트 관리.
# 커서 기준 왼쪽, 오른쪽 문자들.
left = list(input().strip())
right = []
M = int(input())

for _ in range(M):
    cmd = input()
    if cmd[0] == "L":
        if left:
            right.append(left.pop())
    elif cmd[0] == "D":
        if right:
            left.append(right.pop())
    elif cmd[0] == "B":
        if left:
            left.pop()
    elif cmd[0] == "P":
        left.append(cmd[2])

# 출력
print("".join(left) + "".join(right[::-1]))