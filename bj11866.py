"""
요세푸스 문제 0
https://www.acmicpc.net/problem/11866
"""
from collections import deque

# 입력받기
N, K = map(int, input().split())

# 큐로 구현하기
result = []
q = deque([i for i in range(1, N+1)])
while q:
    q.rotate(-(K-1))
    result.append(str(q.popleft()))

# 출력하기
print("<" + ", ".join(result) + ">")