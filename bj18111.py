"""
마인크래프트
https://www.acmicpc.net/problem/18111
"""
# 입력받기
N, M, B = map(int, input().split())
field = []
for _ in range(N):
    field += list(map(int, input().split()))

# 예제 입력1
# N, M, B = 3, 4, 99
# field = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

# 완전탐색 진행. (PyPy3 통과)
max_h = max(field)
result_t, result_h = 3*N*M*max_h, -1
for h in range(max_h+1):
    # 걸리는 시간, 필요한 블록 수 계산
    t, dB_sum = 0, 0
    for f in field:
        dB = h - f
        dB_sum += dB
        if dB > 0:
            t += 1 * dB
        elif dB < 0:
            t += -2 * dB
            
    # print(f"현재높이 {h:3d} - 기존기록=({result_t}, {result_h}), 새로운기록=({t}, {h}) (dB = {dB})")
    
    if dB_sum <= B and t <= result_t:
        result_t = t
        if result_h < h: result_h = h

print(result_t, result_h)

# -------------- 아래는 틀린 코드. 이진탐색 시도.
# # 이진탐색을 위한 최소, 최대 높이
# h_start = 0
# h_end = max(field)

# # 이진탐색 수행
# t, h = sum(field)*2, 0    # h가 0일때 결과값 기준.
# while (h_start<=h_end):
#     h_mid = (h_start + h_end) // 2
    
#     # 걸리는 시간, 필요한 블록 수 계산
#     new_t = 0
#     dB = 0
#     for f in field:
#         dB += h_mid - f
#         if h_mid - f > 0:
#             new_t += 1 * (h_mid - f)
#         elif h_mid - f < 0:
#             new_t += 2 * (f - h_mid)
            
#     # print(f"{h_start:3d} {h_mid:3d} {h_end:3d}, 기존기록=({t}, {h}), 새로운기록=({new_t}, {h_mid}) (dB = {dB})")
    
#     # 블록이 부족한 경우
#     if dB > B:
#         # 층수 낮추기
#         h_end = h_mid - 1
#         continue
    
#     # 기존 기록과 비교하여 다음 탐색 수행
#     if new_t < t:
#         # 기록한 뒤, 더 높은 기록이 있는지 탐색
#         t, h = new_t, h_mid
#         h_start = h_mid + 1
#     elif new_t > t:
#         # 높이를 더 낮춰보기
#         h_end = h_mid - 1
#     else:
#         # 기존 기록보다 높이가 더 높은지 확인 후 업데이트
#         if h < h_mid:
#             h = h_mid
#         h_start = h_mid + 1

# print(t, h)
    

# -------------- 아래는 시간초과된 코드

# # 최대 높이와 최소 높이 찾기
# field.sort()
# upper_bound = field[-1]
# lower_bound = field[0]

# # 최대 높이부터 내림차순으로 판단해보기
# from sys import maxsize
# rt, rh = maxsize, upper_bound
# for h in range(upper_bound, lower_bound-1, -1):
#     # 필요한 블록 계산
#     need = h*N*M - sum(field)
    
#     # 블록을 쌓아야 하는 경우
#     if need >= 0:
#         # 보유한 블록이 부족하면 패스
#         if B < need:
#             pass
#         # 보유한 블록이 충분하면 기존 기록과 비교하여 갱신.
#         else:
#             nt, nh = 0, h
#             for f in field:
#                 if f > h: nt += 2   # 블록 제거 2초
#                 elif f < h: nt += 1 # 블록 쌓기 1초
#             if nt < rt:
#                 rt, rh = nt, nh
    
#     # 블록을 제거해야 하는 경우
#     else:
#         # 기존 기록과 비교하여 갱신.
#         nt, nh = 0, h
#         for f in field:
#             if f > h: nt += 2   # 블록 제거 2초
#             elif f < h: nt += 1 # 블록 쌓기 1초
#         if nt < rt:
#             rt, rh = nt, nh

# print(rt, rh)
            

