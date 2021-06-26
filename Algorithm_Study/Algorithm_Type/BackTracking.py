# N-Queen
def solution(n):
    def check(queen, n): # n번째 행에 놓은 Queen에 대한 검증
        # 이전 행에 놓았던 모든 Queen들을 확인해야함
        for i in range(n):
            # 수직과 대각선 확인
            if queen[i] == queen[n]:
                return False
            if abs(queen[n]-queen[i]) == n-i:
                return False
        return True

    def dfs(queen, row, n):
        answer = 0
        if row == n: # 마지막 줄까지 확인했으면 가능한 것으로 판단, 1추가
            return 1
        else:
            for i in range(n):
                queen[row] = i
                if check(queen, row):
                    answer += dfs(queen, row+1, n)
        return answer

    return dfs([0] * n, 0, n)
print(solution(8))
# ================================================================

# 알파벳
def solution(r,c,alpha): # bfs
    answer = 0
    q = [(0,0, alpha[0][0])]
    #       상 하 좌 우
    move = [[1,0],[-1,0],[0,-1],[0,1]]
    while q:
        x, y, step = q.pop()
        answer = max(answer, len(step))

        for m in move:
            nx = x + m[0]
            ny = y + m[1]
            if 0 <= nx < r and 0 <= ny < c and alpha[nx][ny] not in step:
                q.append((nx,ny,step+alpha[nx][ny]))
    return answer


print(solution(2, 4, [['C','A','A','B'],['A','D','C','B']]))
# ================================================================

# 암호 만들기
def solution(l,c,password): # combinations(조합)을 사용할 때
    from itertools import combinations
    password.sort()
    answer = set()
    vowels = ['a','e','i','o','u']
    for i in combinations(password, 4):
        cnt = 0
        for j in i:
            if j in vowels:
                cnt += 1
        if 1 <= cnt <= l-2:
            answer.add("".join(i))

    return answer

print(solution(4,6,['a','t','c','i','s','w']))

def solutoin(l, c, password): # combinations(조합)을 사용하지 않을 때
    result = []
    string = []
    visited = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    answer = set()

    def combination(array, length, index): # DFS 사용
        # 길이가 length인 모든 조합찾기
        if len(string) == length:
            result.append(string[:])
            return

        # 각 원소를 한 번씩만 뽑도록 구성
        for i in range(index, len(array)):
            if i in visited: # 한 번 뽑았으면 다시 뽑지 않도록
                continue
            string.append(array[i])
            visited.append(i)
            combination(array, length, i+1) # 재귀
            string.pop()
            visited.pop()

    combination(password, l, 0)

    for r in result:
        cnt = 0
        for i in r:
            if i in vowels:
                cnt += 1
        if 1<= cnt <= l-2:
            answer.add(r)
    return answer

print(solution(4,6,['a','t','c','i','s','w']))