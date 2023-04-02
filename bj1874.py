"""
스택 수열
https://www.acmicpc.net/problem/1874
PyPy3 통과.
"""

n = int(input())

target = []
for _ in range(n):
    target.append(int(input()))

t_idx = 0
push = 1
stack = []
popped = []
result = []
is_able = True
while push <= n or stack:
    # push 조건: stack에 뽑을 숫자가 아직 없는 경우
    if target[t_idx] not in stack:
        stack.append(push)
        result.append("+")
        push += 1
    
    # pop 조건: stack에서 뽑을 숫자가 있으며, 상단인 경우
    elif target[t_idx] == stack[-1]:
        popped.append(stack.pop())
        result.append("-")
        t_idx += 1
    
    # 종료 조건: stack에서 뽑을 숫자가 있으며, 상단이 아닌 경우
    else:
        is_able = False
        break

if is_able:
    for oper in result:
        print(oper)
else:
    print("NO")