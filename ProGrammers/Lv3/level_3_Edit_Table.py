def solution(n, k, cmd): # 이중연결리스트, 245MB, 시간은 힙보다 적게걸린다
    stack = []
    linked = {i: [i - 1, i + 1] for i in range(1, n + 1)}
    answer = ["O" for _ in range(n)]
    k += 1

    for c in cmd:
        if len(c) > 1: # D, U
            du, x = c.split(' ')
            if du == 'D':
                for _ in range(int(x)):
                    k = linked[k][1] # 아래로
            else:
                for _ in range(int(x)):
                    k = linked[k][0] # 위로
        else:
            if c == 'C':
                prev, nxt = linked[k]
                stack.append([prev, nxt, k])
                answer[k - 1] = 'X'

                if nxt == n + 1:
                    k = linked[k][0]  # 마지막 행 삭제 시 바로 위 행
                else:
                    k = linked[k][1]  # 바로 아래 행 선택

                if prev == 0:
                    linked[nxt][0] = prev
                elif nxt == n + 1:
                    linked[prev][1] = nxt
                else:
                    linked[prev][1] = nxt
                    linked[nxt][0] = prev
            elif c == 'Z':
                prev, nxt, location = stack.pop()
                answer[location - 1] = 'O'

                if prev == 0:
                    linked[nxt][0] = location
                elif nxt == n + 1:
                    linked[prev][1] = location
                else:
                    linked[prev][1] = location
                    linked[nxt][0] = location

    return "".join(answer)
# "OOOOXOOO"
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
# "OOXOXOOO"
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))

def solution(n, k, cmd): # 힙, 최고 103MB, 시간은 오래걸리네??뭐지
    import heapq
    answer = set()
    left, right, stack = [], [], []

    for i in range(n):
        heapq.heappush(right, i) # 현재 위치는 right 첫번째원소
    for i in range(k):
        heapq.heappush(left, -heapq.heappop(right))

    for c in cmd:
        if len(c) > 1:
            du, x = c.split(' ')
            if du == 'D':
                for _ in range(int(x)):
                    if right: # right에서 left로 옮김
                        heapq.heappush(left, -heapq.heappop(right))
            else:
                for _ in range(int(x)):
                    if left:
                        heapq.heappush(right, -heapq.heappop(left))
        else:
            if c == 'C':
                stack.append(heapq.heappop(right))
                if not right: # 삭제한 행이 마지막 행이면 바로 윗 행 선택
                    heapq.heappush(right, -heapq.heappop(left))
            else:
                data = stack.pop() # 복구
                if data < right[0]: # 복구를 해도 현재 내 위치는 변경되면 안됨
                    heapq.heappush(left, -data)
                else:
                    heapq.heappush(right, data)
    while left:
        answer.add(-heapq.heappop(left))
    while right:
        answer.add(heapq.heappop(right))
    return ''.join(["O" if i in answer else "X" for i in range(n)])



# "OOOOXOOO"
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
# "OOXOXOOO"
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
