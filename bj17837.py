"""
새로운 게임 2
https://www.acmicpc.net/problem/17837
"""
class Game():
    def __init__(self, is_print=False):
        # 디버그 옵션
        self.is_print = is_print
        
        # 입력받기
        self.N, self.K = map(int, input().split())
        
        self.board = []
        for _ in range(self.N):
            self.board.append(list(map(int, input().split())))

        self.pawns = []  # [[x0, y0, d0], [x1, y1, d1], ...]
        self.state = [[[] for _ in range(self.N)] for _ in range(self.N)]
        self._move = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for pawn in range(self.K):
            # 0~K-1번 말의 위치 정보 저장하기.
            # x=0~N-1, y=0~N-1, d=0~3
            x, y, d = map(lambda x: int(x)-1, input().split())
            self.pawns.append([x, y, d])
            self.state[x][y].append(pawn)

    def run(self):
        turn = 1
        # 1000번까지 진행.
        while turn <= 1000:
            # 디버그
            if self.is_print: 
                print(turn, "번째 턴")
                for i in self.state:
                    print(i)
                print()
            
            is_over = False
            # 앞번호 말부터 순서대로 이동
            for a in range(self.K):
                
                next_d = self._get_next_d(a)
                
                # 가려는 칸이 흰색인 경우
                if next_d == 0:
                    self._move_pawn(a)

                # 가려는 칸이 적색인 경우
                elif next_d == 1:
                    self._move_pawn(a, reverse=True)

                # 가려는 칸이 청색 혹은 이동 불가한 경우
                elif next_d >= 2:
                    # 방향 전환하기
                    self._reverse_d(a)
                    
                    # 방향 전환 후 이동가능한지 확인
                    next_d = self._get_next_d(a)
                    # 전환 후 가려는 칸이 흰색인 경우
                    if next_d == 0:
                        self._move_pawn(a)
                    # 전환 후 가려는 칸이 적색인 경우
                    elif next_d == 1:
                        self._move_pawn(a, reverse=True)
                    # 전환 후 가려는 칸이 청색 혹은 이동 불가한 경우
                    elif next_d >= 2:
                        pass
                
                # 4개가 쌓인 칸이 있는지 확인
                is_over = self._check_over()

                # 디버그
                if self.is_print:
                    for i in self.state:
                        print(i)
                    print()
                
                # 이동 후 게임종료면 턴 도중 종료
                if is_over:
                    break

            # 게임종료 트리거 발생하면 종료
            if is_over:
                break
            
            turn += 1

        # 결과 출력
        if turn > 1000:
            print(-1)
        else:
            print(turn)
    
    def _get_next_d(self, pawn):
        x, y, d = self.pawns[pawn]
        nx, ny = x+self._move[d][0], y+self._move[d][1]
        next_d = -1
        # 체스판을 벗어나는 경우
        if nx<0 or nx>=self.N or ny<0 or ny>=self.N:
            next_d = 3
        # 다음 칸의 색 숫자 반환(0~2)
        else:
            next_d = self.board[nx][ny]
        
        # 디버그
        if self.is_print:
            print(f"{pawn}({x}, {y}) -> ({nx}, {ny}) 색상 {next_d}")
        
        # 반환
        return next_d

        
    def _move_pawn(self, pawn, reverse=False):
        # 이동할 위치 파악
        x, y, d = self.pawns[pawn]
        nx, ny = x+self._move[d][0], y+self._move[d][1]
        
        # pawn이 있는 칸에서 pawn이 나올때 까지 말 꺼내기
        buf = []
        while True:
            p = self.state[x][y].pop()
            buf.append(p)
            if p == pawn:
                break
            
        # 꺼낸 말을 가려는 칸으로 이동 (역순이면 역순 적용)
        if reverse:
            self.state[nx][ny] += buf
        else:     
            self.state[nx][ny] += reversed(buf)
        
        # 이동한 말 정보 수정
        for p in buf:
            self.pawns[p][:2] = nx, ny
    
    def _reverse_d(self, pawn):
        d = self.pawns[pawn][2]
        # 0 <-> 1, 2 <-> 3
        d = 2*(d//2) + (d+1)%2
        self.pawns[pawn][2] = d
        
    def _check_over(self):
        for i in range(self.N):
            for j in range(self.N):
                if len(self.state[i][j]) >= 4:
                    return True
        return False
        
game = Game(is_print=False)
game.run()