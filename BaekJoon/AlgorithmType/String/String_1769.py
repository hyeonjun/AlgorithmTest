num = input()
cnt = 0

def recursive(sumV):
    global cnt
    if len(sumV) == 1:
        if int(sumV) % 3 == 0:
            return 'YES'
        else:
            return 'NO'
    tmp = 0
    for sv in sumV:
        tmp += int(sv)
    cnt += 1
    return recursive(str(tmp))


answer = recursive(num)
print(cnt)
print(answer)
