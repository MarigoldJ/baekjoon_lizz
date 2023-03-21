"""
청소년 상어
https://www.acmicpc.net/problem/19236
"""
from collections import deque
from copy import deepcopy
# 입력받기
arr = []
for _ in range(4):
    temp = list(map(int, input().split()))
    arr.append([[num, d-1] for num, d in zip(temp[0::2], temp[1::2])])
# arr = [[[7, 5], [2, 2], [15, 5], [9, 7]], [[3, 0], [1, 7], [14, 6], [10, 0]], [[6, 0], [13, 5], [4, 2], [11, 3]], [[16, 0], [8, 6], [5, 1], [12, 1]]]
# [물고기번호(1~16), 방향(0~7)]

test = ['↑', '↖', '←', '↙', '↓', '↘', '→', '↗']

class Field:
    def __init__(self, arr):
        self.arr = arr
        self._arrows = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
        
        # 물고기 번호별 위치 기록
        self._exists = [False] * 17
        for i in range(4):
            for j in range(4):
                num = self.arr[i][j][0]
                self._exists[num] = (i, j)
        # self._exists = [False, (x1, y1), ..., (x16, y16)]
        
        self.x, self.y = 0, 0   # 상어 위치 초기화
        
    def get_result(self, x, y):
        arr = deepcopy(self.arr)
        exists = deepcopy(self._exists)
        
        # for a in arr:
        #     for b in a:
        #         print(f"{b[0]}{test[b[1]]}", end=" ")
        #     print()
        # print('------------start---------')
        
        return self.dfs(arr, exists, x, y)
    
    def dfs(self, arr, exists, x, y):
        """
        재귀 함수 형태를 활용해서 DFS 탐색을 하자.
        cx, cy: current
        nx, ny: next
        fx, fy: fish
        dx, dy: delta xy
        """
        # 현재 위치 정보
        f_num = arr[x][y][0]
        # for a in arr:
        #     for b in a:
        #         print(f"{b[0]}{test[b[1]]}", end=" ")
        #     print()
        # print(exists)
        
        # 현재 위치 잡아먹기
        exists[f_num] = False
        arr[x][y][0] = 0
        
        # 물고기 이동시키기
        for num, fish in enumerate(exists):
            # 물고기가 먹히지 않았으면
            if fish:
                # 물고기는 규칙에 따라 이동
                fx, fy = fish
                arrow_que = deque(self._arrows, 8)
                arrow_que.rotate(-arr[fx][fy][1])
                for _ in range(8):
                    fdx, fdy = arrow_que[0]
                    fnx, fny = fx+fdx, fy+fdy
                    # 벽이 있으면 패스
                    if not self._is_valid_xy(fnx, fny):
                        arrow_que.rotate(-1)
                        arr[fx][fy][1] = (arr[fx][fy][1] + 1) % 8
                        continue
                    # 상어가 있으면 패스
                    elif x == fnx and y == fny:
                        arrow_que.rotate(-1)
                        arr[fx][fy][1] = (arr[fx][fy][1] + 1) % 8
                        continue
                    # 이동 가능하므로 자리교환
                    else:
                        num2 = arr[fnx][fny][0]
                        # 이동할 자리가 빈자리인 경우
                        if num2 == 0:
                            arr[fx][fy], arr[fnx][fny], exists[num] = \
                                arr[fnx][fny], arr[fx][fy], (fnx, fny)
                        
                        # 이동할 자리가 빈자리가 아닌 경우
                        else:
                            arr[fx][fy], arr[fnx][fny], exists[num], exists[num2] = \
                                arr[fnx][fny], arr[fx][fy], (fnx, fny), (fx, fy)
                        break

        # print(x, y)
        # for a in arr:
        #     for b in a:
        #         print(f"{b[0]}{test[b[1]]}", end=" ")
        #     print()
        # print(exists)
        
        # 상어가 이동할 수 있는지 확인
        cango_list = self._get_cango_list(arr, exists, x, y)
        # print(cango_list, '\n--------------------')
        if cango_list:
            # 재귀함수로 추가 탐색
            sum_list = []
            for fn_num in cango_list:
                nx, ny = exists[fn_num]
                temp_arr, temp_exists = deepcopy(arr), deepcopy(exists)
                # print(f"{x} {y}에서 추가로 {nx} {ny} 탐색")
                sum_list.append(self.dfs(temp_arr, temp_exists, nx, ny))
            return f_num + max(sum_list)
        else:
            # 상어는 집으로 가고 종료됨.
            return f_num

        
    def _is_valid_xy(self, x, y):
        if 0<=x<4 and 0<=y<4:
            return True
        else:
            return False
        
    def _get_cango_list(self, arr, exists, x, y):
        """
        상어의 위치가 x, y일때 이동이 가능한 물고기 번호 리스트 반환.
        """
        cango_list = []
        dx, dy = self._arrows[arr[x][y][1]]
        for i in range(3):
            nx, ny = x + (i+1)*dx, y + (i+1)*dy
            # 벽이 있으면 패스
            if not self._is_valid_xy(nx, ny):
                continue
            # 물고기가 없으면 패스
            if arr[nx][ny][0] == 0:
                continue
            # 이동 가능하므로 cango_list에 추가
            cango_list.append(arr[nx][ny][0])
        return cango_list

field = Field(arr)
result = field.get_result(0, 0)
print(result)
