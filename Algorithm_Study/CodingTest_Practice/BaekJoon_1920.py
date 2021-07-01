# 수 찾기
def solution(n,arr,m, find):
    answer = []
    for f in find:
        if f in arr:
            answer.append(1)
        else:
            answer.append(0)
    return answer
    pass

print(solution(5, [4,1,5,2,3], 5, [1,3,7,9,5]))

def solution(arr, find):
    answer = []
    array = {i:1 for i in arr}

    for f in find:
        answer.append(array.get(f, 0))
    # dictionary.get()
    # get(x)은 x라는 key에 대응되는 value를 가져온다
    # get(x, default)를 주면
    # x라는 key가 없을때 default를 대신 가져온다.
    return answer

print(solution([4,1,5,2,3], [1,3,7,9,5]))