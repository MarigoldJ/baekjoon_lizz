"""
주사위 굴리기 2
https://www.acmicpc.net/problem/23288

"""
from collections import deque

# 입력받기
n, m, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))


# 지도 클래스
class Map:
    def __init__(self, n, m, arr):
        # 지도 저장
        self.n, self.m, self.arr = n, m, arr
        # arr의 한 칸에 도달했을 때 얻는 점수 저장하기.
        self.point = [[0]*m for _ in range(n)]
        
        # 이동방향들, 이동방향에 따른 dx와 dy들
        self.directions = deque(['동', '남', '서', '북'], 4)
        self.moves = {'동': (0, 1), '서': (0, -1), '남': (1, 0), '북': (-1, 0)}
        # 현재 주사위 위치
        self.x, self.y = 0, 0
        
        
    def move(self):
        # 현재 이동방향대로 좌표 이동
        dx, dy = self.moves[self.directions[0]]
        nx, ny = self.x+dx, self.y+dy
        if self._is_valid_xy(nx, ny):
            self.x, self.y = nx, ny
        else:
            # 방향 반대로 전환
            self.turn_right()
            self.turn_right()
            # 다시 move 진행.
            self.move()
    
    def get_current_num(self):
        return self.arr[self.x][self.y]

    def get_point(self):
        # x, y에서 얻는 점수 확인하기
        if self.point[self.x][self.y] == 0:
            self._update_point(self.x, self.y)
        return self.point[self.x][self.y]
    
    def get_current_direction(self):
        return self.directions[0]
    
    def _update_point(self, x, y):
        # bfs로 같은 숫자 개수 탐색
        visited = [[False]*m for _ in range(n)]
        visited[x][y] = True
        count_list = [(x, y)]
        
        B = self.arr[x][y]
        queue = deque([(x, y)])
        while queue:
            px, py = queue.popleft()
            for dx, dy in self.moves.values():
                # 범위를 벗어나면 무시
                if not self._is_valid_xy(px+dx, py+dy):
                    continue
                # 방문한적 없는 같은 숫자 B면...
                if self.arr[px+dx][py+dy] == B and not visited[px+dx][py+dy]:
                    visited[px+dx][py+dy] = True
                    queue.append((px+dx, py+dy))
                    count_list.append((px+dx, py+dy))
                    
        # 포인트 업데이트
        point = B * len(count_list)
        for cx, cy in count_list:
            self.point[cx][cy] = point

    def _is_valid_xy(self, x, y):
        # (x, y)가 지도 내에 있는 좌표인지 확인.
        if 0<=x<self.n and 0<=y<self.m:
            return True
        else:
            return False
        
    def turn_right(self):
        # 이동방향을 시계방향으로 회전
        self.directions.rotate(-1)
        

# 주사위 설정하기
class Dice:
    def __init__(self):
        self.nums = [2, 4, 1, 3, 5, 6]
        
    def get_top(self):
        return self.nums[2]
    
    def get_bottom(self):
        return self.nums[5]
    
    def move(self, direction):
        if direction == '동':
            self.go_right()
        elif direction == '서':
            self.go_left()
        elif direction == '남':
            self.go_down()
        elif direction == '북':
            self.go_up()
        
    def go_right(self):
        self.nums[1], self.nums[2], self.nums[3], self.nums[5] = \
            self.nums[5], self.nums[1], self.nums[2], self.nums[3]
    
    def go_down(self):
        self.nums[0], self.nums[2], self.nums[4], self.nums[5] = \
            self.nums[5], self.nums[0], self.nums[2], self.nums[4]
    
    def go_left(self):
        self.nums[1], self.nums[2], self.nums[3], self.nums[5] = \
            self.nums[2], self.nums[3], self.nums[5], self.nums[1]
            
    def go_up(self):
        self.nums[0], self.nums[2], self.nums[4], self.nums[5] = \
            self.nums[2], self.nums[4], self.nums[5], self.nums[0]


# 이제 주사위 굴리고 포인트 얻자.
my_map = Map(n, m, arr)
my_dice = Dice()
mx, my = 0, 0
result = 0
for _ in range(k):
    # 주사위 이동하고 점수얻기
    my_map.move()
    my_dice.move(my_map.directions[0])
    result += my_map.get_point()
    
    # 방향 전환하기
    A = my_dice.get_bottom()
    B = my_map.get_current_num()
    if A > B:
        my_map.turn_right()
    elif A < B:
        my_map.turn_right()
        my_map.turn_right()
        my_map.turn_right()
    
print(result)
