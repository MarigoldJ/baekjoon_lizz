# 입력
N = int(input())

# bottom-up DP
d = [0] * (10**6 + 1)
for x in range(2, 10**6 + 1):
    next_list = []
    if x % 3 == 0:
        next_list.append(x // 3)
    if x % 2 == 0:
        next_list.append(x // 2)
    next_list.append(x - 1)
    d[x] = 1 + min([d[next_num] for next_num in next_list])

# 출력
print(d[N])
