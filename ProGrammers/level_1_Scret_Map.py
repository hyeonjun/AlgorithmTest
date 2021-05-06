def solution(n, arr1, arr2):
    answer = []
    for i in zip(arr1, arr2):
        a1 = str(bin(i[0])[2:2+n]) if len(str(bin(i[0])[2:])) >= n else "0"*(n-len(str(bin(i[0])[2:])))+str(bin(i[0])[2:])
        a2 = str(bin(i[1])[2:2+n]) if len(str(bin(i[1])[2:])) >= n else "0"*(n-len(str(bin(i[1])[2:])))+str(bin(i[1])[2:])
        tmp = ""
        for j in zip(a1, a2):
            if int(j[0])+int(j[1]) in [1, 2]:
                tmp+="1"
            else:
                tmp+="0"
        answer.append(tmp)
    for i in range(len(answer)):
        answer[i] = answer[i].replace("1", "#")
        answer[i] = answer[i].replace("0", " ")
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))

def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        a = str(bin(i|j)[2:])
        a = a.rjust(n, '0')
        a = a.replace('1', '#')
        a = a.replace('0', ' ')
        answer.append(a)
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))

