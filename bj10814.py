"""
나이 순 정렬
https://www.acmicpc.net/problem/10814
"""
N = int(input())

# 1~200살 이름 저장하기
ages = [[] for _ in range(201)]
for _ in range(N):
    age, name = input().split()
    ages[int(age)].append(name)

# 출력하기
for age, names in enumerate(ages):
    if names:
        for name in names:
            print(age, name)