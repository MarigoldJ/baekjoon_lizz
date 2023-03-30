"""
연산자 끼워넣기
https://www.acmicpc.net/problem/14888
4:09pm ~ 4:37pm
"""
# 입력받기
_ = int(input())
num_list = list(map(int, input().split()))
oper_num_list = list(map(int, input().split()))

# 알고리즘 수행하는 클래스
class Main():
    def __init__(self, num_list, oper_num_list):
        self.num_list = num_list
        self.oper_num_list = oper_num_list
        self.oper_list = ["+"]
        
    
    def run(self):
        # 최댓값 출력하기
        print(self._dfs_max(self.num_list, self.oper_num_list))
        
        # 최솟값 출력하기
        print(self._dfs_min(self.num_list, self.oper_num_list))

    def _dfs_max(self, num_list, oper_num_list):
        # 마지막 탐색이면 값 반환하기
        if len(num_list) == 2:
            for oper, oper_num in enumerate(oper_num_list):
                if oper_num > 0:
                    return self._operate(num_list[0], num_list[1], oper)
        # 마지막 탐색이 아니면 dfs 계속 진행.
        else:
            result_list = []
            for oper, oper_num in enumerate(oper_num_list):
                if oper_num > 0:
                    front = self._operate(num_list[0], num_list[1], oper)
                    new_num_list = num_list.copy()
                    new_oper_num_list = oper_num_list.copy()
                    new_num_list = [front] + new_num_list[2:]
                    new_oper_num_list[oper] -= 1
                    
                    result = self._dfs_max(new_num_list, new_oper_num_list)
                    result_list.append(result)
            return max(result_list)
        
    def _dfs_min(self, num_list, oper_num_list):
        # 마지막 탐색이면 값 반환하기
        if len(num_list) == 2:
            for oper, oper_num in enumerate(oper_num_list):
                if oper_num > 0:
                    return self._operate(num_list[0], num_list[1], oper)
        # 마지막 탐색이 아니면 dfs 계속 진행.
        else:
            result_list = []
            for oper, oper_num in enumerate(oper_num_list):
                if oper_num > 0:
                    front = self._operate(num_list[0], num_list[1], oper)
                    new_num_list = num_list.copy()
                    new_oper_num_list = oper_num_list.copy()
                    new_num_list = [front] + new_num_list[2:]
                    new_oper_num_list[oper] -= 1
                    
                    result = self._dfs_min(new_num_list, new_oper_num_list)
                    result_list.append(result)
            return min(result_list)
        
    def _operate(self, num1, num2, oper):
        if oper == 0:
            return num1 + num2
        elif oper == 1:
            return num1 - num2
        elif oper == 2:
            return num1 * num2
        elif oper == 3:
            if num1 >= 0:
                return num1 // num2
            else:
                return -((-num1) // num2)

main = Main(num_list, oper_num_list)
main.run()