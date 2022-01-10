def mul(arr):
    result = 1
    for i in arr:
        result *= i
    return result
num = input()
flag = False
for i in range(1, len(num)):
    if mul(list(map(int, num[:i]))) == mul(list(map(int, num[i:]))):
        flag = True
        break
print('YES' if flag else 'NO')