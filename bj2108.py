import sys
N = int(sys.stdin.readline())

l = []
for _ in range(N):
    l.append(int(sys.stdin.readline()))
l.sort()

# 산술평균
print(round(sum(l)/N))

# 중앙값
print(l[N//2])

# 최빈값
from collections import Counter
most = Counter(l).most_common(2)
if len(most) > 1 and most[0][1] == most[1][1]:
    print(max(most[0][0], most[1][0]))
else:
    print(most[0][0])

# 범위
print(l[-1] - l[0])
