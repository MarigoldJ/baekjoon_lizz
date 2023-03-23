"""
랜선 자르기
https://www.acmicpc.net/problem/1654
"""
# 입력받기
K, N = map(int, input().split())
lans = []
for _ in range(K):
    lans.append(int(input()))
# 예제 입력
# K, N = 4, 11
# lans = [802, 743, 457, 539]

# 이진탐색을 위한 최소, 최대길이 찾기
start = 0
end = sum(lans) // N

# 이진탐색 수행
result = 0
while (start <= end):
    num = 0
    mid = (start + end) // 2
    if mid == 0: mid = 1
    for lan in lans:
        num += lan // mid
    
    # print(f"{start:3d}-{mid:3d}-{end:3d} : {num}개, ", [lan//mid for lan in lans])
    
    if num > N:
        # 더 큰 길이로 잘라야 함
        result = mid
        start = mid + 1
    elif num < N:
        # 더 작은 길이로 잘라야 함
        end = mid - 1
    else:
        # 적정 길이임. 더 큰 길이가 되는지 확인해야함.
        result = mid
        start = mid + 1
        
print(result)

# -------------- 아래는 시간초과된 코드
# # 만들 수 있는 랜선 최대 길이 상한선 구하기
# upper_bound = sum(lans) // N

# # 상한선부터 길이를 줄여나가면서 잘라보기.
# result = upper_bound
# while result > 0:
#     num = 0
#     for lan in lans:
#         num += lan // result
#     if num == N:
#         break
#     else:
#         result -= 1
# print(result)
