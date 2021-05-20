def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            answer[i] = j-i
            if prices[i] > prices[j]:
                break
    return answer

print(solution([1,2,3,2,3])) # [4,3,1,1,0]

def solution(prices):
    answer = [len(prices)-i-1 for i in range(len(prices))]
    # [4,3,2,1,0]
    tmp = [0] # prices 인덱스를 차례로 담는 배열
    for i in range(1, len(prices)):
        while tmp:
            idx = tmp[-1]
            if prices[idx] > prices[i]: # 주식가격이 떨어짐
                answer[idx] = i-idx
                tmp.pop()
            else:
                break
        tmp.append(i)
    return answer

print(solution([1,2,3,2,3])) # [4,3,1,1,0]

def solution(prices):
    answer = [len(prices)-i-1 for i in range(len(prices))]
    tmp = []
    for i in range(len(prices)):
        # tmp가 비어있지않고, 가격이 떨어지지 않았으면
        while tmp and prices[i] < prices[tmp[-1]]:
            j = tmp.pop()
            answer[j] = i-j
        tmp.append(i)
    return answer

print(solution([1,2,3,2,3])) # [4,3,1,1,0]

