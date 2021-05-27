def solution(arr): # 통과는 가능하나, 아래 솔루션보다 시간이 2배 이상 걸림
    answer = [0,0]
    N = len(arr)
    def split(x, y, n):
        tmp = [arr[i][j] for i in range(x, x+n) for j in range(y,y+n)]
        zero = tmp.count(0)
        one = tmp.count(1)
        if zero == n*n:
            answer[0] += 1
        elif one == n*n:
            answer[1] += 1
        else:
            split(x, y, n // 2)
            split(x, y + n // 2, n // 2)
            split(x + n // 2, y, n // 2)
            split(x + n // 2, y + n // 2, n // 2)
    split(0,0,N)
    return answer

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])) # [4,9]
print(solution([[1,1,1,1,1,1,1,1],
                [0,1,1,1,1,1,1,1],
                [0,0,0,0,1,1,1,1],
                [0,1,0,0,1,1,1,1],
                [0,0,0,0,0,0,1,1],
                [0,0,0,0,0,0,0,1],
                [0,0,0,0,1,0,0,1],
                [0,0,0,0,1,1,1,1]])) # [10,15]


def solution(arr):
    answer = [0, 0]
    N = len(arr)
    def split(x, y, n):
        start = arr[x][y]
        for i in range(x, x+n):
            for j in range(y, y+n):
                if start != arr[i][j]:
                    split(x, y, n//2)
                    split(x, y+n//2, n//2)
                    split(x+n//2, y, n//2)
                    split(x+n//2, y+n//2, n//2)
                    return
        answer[start] += 1
    split(0, 0, N)
    return answer

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])) # [4,9]
print(solution([[1,1,1,1,1,1,1,1],
                [0,1,1,1,1,1,1,1],
                [0,0,0,0,1,1,1,1],
                [0,1,0,0,1,1,1,1],
                [0,0,0,0,0,0,1,1],
                [0,0,0,0,0,0,0,1],
                [0,0,0,0,1,0,0,1],
                [0,0,0,0,1,1,1,1]])) # [10,15]