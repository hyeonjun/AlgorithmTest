def Binary_Search(data, n):
    count = 1
    current = len(data)//2
    front = 0
    back = len(data)-1
    while count < len(data):
        tmp = current
        if data[current] == n:
            return [True, count]
        elif data[current] > n:
            back = current
            current = (current + front)//2
            count+=1
        else:
            front = current
            current = (current + back)//2
            count+=1
        if tmp == current:
            return [False, count]
    return [False, count]

"""
다음 1~30번째 병뚜껑에는 각각 1~100 사이의 번호가 표시되어있다
이 중에 70이 있을지 없을지를 확인하는 방법
조건:
 - 가장 적게 병을 따야함 
 - 각 병뚜껑에 씌여진 번호는 낮은 번호 순으로 기입되어 있다
"""

import random
data = random.sample(range(1,21), 10)
data.sort()
print(data)
print(Binary_Search(data, 12))
print(Binary_Search(data, 7))

def Binary_search(data, search, count): # 재귀
    if len(data) == 1:
        return [True, count] if search == data[0] else [False, count]
    if len(data) == 0:
        return [False, count]

    medium = len(data)//2
    if search == data[medium]:
        return [True, count]
    else:
        if search > data[medium]:
            return Binary_search(data[medium:], search, count+1)
        else:
            return Binary_search(data[:medium], search, count+1)

print(Binary_search(data, 12, 1))
print(Binary_search(data, 7, 1))






















